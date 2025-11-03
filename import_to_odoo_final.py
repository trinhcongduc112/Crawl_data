# =============================================================
# File: import_to_odoo_final.py
# Phiên bản ổn định - Import docs vào Odoo
# =============================================================

import os
import re
import json
import base64
import glob
import time
import sys
import xmlrpc.client
from typing import Dict, Tuple, Any

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ===================== CẤU HÌNH =====================
BASE_OUTPUT_DIR = r"C:\Abivin\data_docs03"

ODOO_BASE_URL = "https://test018.odoo.com"
ODOO_DB_NAME = "test018"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "3f623d85508792f81af911610db742d67a5d1845"

SPACE_NAME = "Tài liệu Abivin 02"
MODEL_ARTICLE = "knowledge.article"
MODEL_ATTACHMENT = "ir.attachment"
LOCAL_ASSET_REF = "../assets_"
# ====================================================

# Tùy chọn đánh ID tuần tự (chỉ dùng để sort, không hiển thị trong tiêu đề)
APPEND_ID_TO_TITLE = False  # Tắt hiển thị ID trong tiêu đề trên Odoo
ID_TITLE_FORMAT = " [#%04d]"  # Format không dùng, chỉ để tham khảo


# ---------------- XML-RPC CORE ----------------------
def odoo_login() -> Tuple[xmlrpc.client.ServerProxy, int]:
    print("\n🔐 Đang kết nối với Odoo...")
    common = xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/common")
    
    try:
        version_info = common.version()
        print(f"  ✓ Server version: {version_info.get('server_version', 'Unknown')}")
    except Exception as e:
        print(f"  ✗ Lỗi kiểm tra phiên bản: {e}")
    
    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if not uid:
        raise SystemExit("❌ Xác thực Odoo thất bại. Kiểm tra lại API key hoặc quyền truy cập.")
    print(f"  ✓ Đã đăng nhập vào Odoo với user ID: {uid}")
    return xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/object"), uid


def odoo_call(models, uid, model, method, *args, **kwargs):
    """Gọi RPC chuẩn cho Odoo (sửa để tương thích cả search_read & write)"""
    args = list(args) if args else []
    kwargs = kwargs or {}
    for attempt in range(3):
        try:
            return models.execute_kw(
                ODOO_DB_NAME, uid, ODOO_API_KEY,
                model, method, args, kwargs
            )
        except Exception as e:
            print(f"  [RPC ERROR] {model}.{method} attempt {attempt+1}/3: {e}")
            time.sleep(2)
    raise RuntimeError(f"❌ Gọi RPC {model}.{method} thất bại sau 3 lần.")


def odoo_search(models, uid, model, domain, fields=None, limit=0):
    kwargs = {}
    if fields:
        kwargs["fields"] = fields
    if limit:
        kwargs["limit"] = limit
    return odoo_call(models, uid, model, "search_read", domain, **kwargs)


def odoo_create(models, uid, model, vals):
    if not isinstance(vals, dict):
        raise TypeError("Giá trị truyền vào create() phải là dict.")
    # SỬA LỖI: Không bọc [vals]
    return odoo_call(models, uid, model, "create", vals)


def odoo_write(models, uid, model, ids, vals):
    """Đảm bảo ids và vals đúng định dạng"""
    if not isinstance(ids, list):
        ids = [ids]
    if not isinstance(vals, dict):
        raise TypeError("Giá trị truyền vào write() phải là dict.")
    # SỬA LỖI: Không bọc [ids, vals]
    return odoo_call(models, uid, model, "write", ids, vals)


# ---------------- HELPER FUNCTIONS -------------------
def ensure_space(models, uid, space_name: str) -> int:
    """Tìm hoặc tạo space trong Odoo"""
    print(f"\n📁 Kiểm tra không gian làm việc: '{space_name}'...")
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name", "=", space_name)], ["id"], limit=1)
    if rec:
        print(f"  ✓ Đã tìm thấy không gian làm việc: '{space_name}' (ID: {rec[0]['id']})")
        return rec[0]['id']
    print(f"  + Tạo mới không gian '{space_name}'...")
    space_id = odoo_create(models, uid, MODEL_ARTICLE, {
        "name": space_name,
        "body": "<p>Không gian chứa tài liệu imported từ docs.abivin.com</p>"
    })
    print(f"  ✓ Đã tạo mới space (ID: {space_id})")
    return space_id


def guess_mimetype(name: str) -> str:
    ext = os.path.splitext(name.lower())[1]
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml"
    }.get(ext, "application/octet-stream")


def upload_attachment(models, uid, path: str, public=True) -> Tuple[int, str]:
    """Upload ảnh lên Odoo và trả về URL"""
    try:
        with open(path, "rb") as f:
            datas_b64 = base64.b64encode(f.read()).decode()
        att_id = odoo_create(models, uid, MODEL_ATTACHMENT, {
            "name": os.path.basename(path),
            "datas": datas_b64,
            "mimetype": guess_mimetype(path),
            "public": public
        })
        url = f"/web/content/{att_id}"
        return att_id, url
    except Exception as e:
        print(f"  ✗ Lỗi upload ảnh '{path}': {e}")
        return None, None


def replace_local_assets(html: str, asset_map: Dict[str, str]) -> str:
    """Thay thế đường dẫn ảnh local bằng URL Odoo"""
    if not html:
        return ""
    # Tìm các ảnh có đường dẫn local
    pat = re.compile(rf"{re.escape(LOCAL_ASSET_REF)}([A-Za-z0-9_.\-]+)")
    result = pat.sub(lambda m: asset_map.get(m.group(1), m.group(0)), html)
    return result


def load_sorted_docs():
    """Load tất cả JSON, gom kèm assets_dir, sắp xếp theo order_index và gán id_seq nếu thiếu."""
    all_content_dirs = [d for d in glob.glob(os.path.join(BASE_OUTPUT_DIR, "*", "content_*")) if os.path.isdir(d)]
    if not all_content_dirs:
        raise SystemExit(f"❌ LỖI: Không tìm thấy thư mục 'content_*' trong '{BASE_OUTPUT_DIR}'.")

    print(f"📂 Tìm thấy {len(all_content_dirs)} thư mục content:")
    for content_dir in all_content_dirs:
        print(f"  - {os.path.basename(content_dir)}")

    items = []  # (slug, doc, assets_dir)
    for content_dir in all_content_dirs:
        assets_dir = os.path.join(
            os.path.dirname(content_dir),
            os.path.basename(content_dir).replace("content_", "assets_")
        )
        for jp in glob.glob(os.path.join(content_dir, "*.json")):
            try:
                with open(jp, "r", encoding="utf-8") as f:
                    d = json.load(f)
                slug = d.get("new_slug") or d.get("old_slug") or os.path.splitext(os.path.basename(jp))[0]
                items.append((slug, d, assets_dir if os.path.isdir(assets_dir) else None))
            except Exception as e:
                print(f"  ⚠️  Bỏ qua file lỗi '{jp}': {e}")

    # Sắp xếp theo ưu tiên section cố định, sau đó order_index -> title
    section_priority = {
        "user_guide": 0,
        "developer_guide": 1,
        "release_notes": 2,
    }
    def sort_key(tup):
        _slug, _doc, _ = tup
        section = _doc.get("section", "unknown")
        order_idx = _doc.get("order_index", 999999)
        title = (_doc.get("title") or _slug).lower()
        pri = section_priority.get(section, 10)
        return (pri, order_idx, title)

    items.sort(key=sort_key)

    # Sau khi sắp xếp xong, gán lại _id_seq THEO TỪNG NHÓM CHA (parent_slug)
    # để đảm bảo thứ tự hiển thị trong mỗi nhóm giống sidebar
    parent_to_next_seq: Dict[str, int] = {}
    for slug, doc, assets_dir in items:
        parent_key = doc.get("parent_slug") or "__root__"
        seq = parent_to_next_seq.get(parent_key, 1)
        doc["_id_seq"] = seq
        parent_to_next_seq[parent_key] = seq + 1

    return items


# ------------------- IMPORTER CHÍNH -------------------
def import_all():
    """Import tất cả docs vào Odoo"""
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)
    uploaded_cache: Dict[str, Dict[str, str]] = {}
    total_files = 0
    success_count = 0

    print("\n" + "="*60)
    print("🚀 BẮT ĐẦU QUÁ TRÌNH IMPORT...")
    print("="*60 + "\n")

    # Load & sort, đồng thời gán _id_seq
    sorted_items = load_sorted_docs()

    article_ids: Dict[str, int] = {}

    for slug, doc, assets_dir in sorted_items:
        total_files += 1
        try:
            base_title = doc.get("title") or slug
            id_seq = doc.get("_id_seq")
            title = f"{base_title}{(ID_TITLE_FORMAT % id_seq) if (APPEND_ID_TO_TITLE and id_seq) else ''}"
            print(f"\n[{total_files}] Đang xử lý: {title[:60]}")
            
            # Xử lý ảnh
            asset_map: Dict[str, str] = {}
            if assets_dir:
                cache = uploaded_cache.setdefault(assets_dir, {})
                # Tìm tất cả các ảnh được tham chiếu trong HTML
                needed_assets = set(re.findall(
                    rf"{re.escape(LOCAL_ASSET_REF)}([A-Za-z0-9_.\-]+)",
                    doc.get("html_content", "")
                ))
                
                if needed_assets:
                    print(f"  📸 Tìm thấy {len(needed_assets)} ảnh")
                    
                for fn in needed_assets:
                    if fn in cache:
                        asset_map[fn] = cache[fn]
                        continue
                    local_path = os.path.join(assets_dir, fn)
                    if os.path.exists(local_path):
                        print(f"    ⬆️  Đang upload: {fn}")
                        att_id, url = upload_attachment(models, uid, local_path, public=True)
                        if url:
                            cache[fn] = url
                            asset_map[fn] = url
                    else:
                        print(f"    ⚠️  Không tìm thấy file: {local_path}")

            # Thay thế URL ảnh trong HTML
            body = replace_local_assets(doc.get("html_content", ""), asset_map)

            # Tạo hoặc cập nhật article
            vals = {
                "name": title,
                "body": body,
                "parent_id": space_id
            }
            # Thêm sequence nếu có _id_seq để Odoo sort đúng thứ tự
            if id_seq is not None:
                vals["sequence"] = id_seq

            # Kiểm tra article đã tồn tại
            # 1) Tìm theo tên chính xác
            existing_article = odoo_search(
                models, uid, MODEL_ARTICLE,
                [("name", "=", vals["name"]), ("parent_id", "=", space_id)],
                ["id"], limit=1
            )
            # 2) Nếu không thấy (trường hợp phiên bản cũ có tên kèm [#ID]) thì tìm gần đúng theo tiền tố
            if not existing_article:
                existing_article = odoo_search(
                    models, uid, MODEL_ARTICLE,
                    [("name", "ilike", f"{base_title}%"), ("parent_id", "=", space_id)],
                    ["id"], limit=1
                )

            if existing_article:
                rid = existing_article[0]["id"]
                odoo_write(models, uid, MODEL_ARTICLE, [rid], vals)
                article_ids[slug] = rid
                print(f"  ✓ Cập nhật bài viết (ID: {rid})")
            else:
                aid = odoo_create(models, uid, MODEL_ARTICLE, vals)
                article_ids[slug] = aid
                print(f"  ✓ Tạo mới bài viết (ID: {aid})")
            
            success_count += 1

        except Exception as e:
            print(f"\n❌ LỖI khi xử lý '{slug}': {e}\n")

    # Lượt 2: Set parent_id theo parent_slug
    print("\n🔗 Đang thiết lập quan hệ cha-con...")
    fixed = 0
    for slug, doc, _assets_dir in sorted_items:
        try:
            parent_slug = doc.get("parent_slug")
            if not parent_slug:
                continue
            child_id = article_ids.get(slug)
            parent_id = article_ids.get(parent_slug)
            if child_id and parent_id:
                odoo_write(models, uid, MODEL_ARTICLE, [child_id], {"parent_id": parent_id})
                fixed += 1
        except Exception as e:
            print(f"  ⚠️  Không thể set parent cho '{slug}': {e}")

    if fixed:
        print(f"  ✓ Đã set parent cho {fixed} bài viết")

    print("\n" + "="*60)
    print(f"✅✅✅ IMPORT HOÀN TẤT! ✅✅✅")
    print(f"   Tổng số file: {total_files}")
    print(f"   Thành công: {success_count}")
    print(f"   Thất bại: {total_files - success_count}")
    print(f"\n📋 Hãy kiểm tra kết quả trong Odoo, không gian: '{SPACE_NAME}'")
    print("="*60)


# -------------------- MAIN ---------------------------
if __name__ == "__main__":
    try:
        import_all()
    except KeyboardInterrupt:
        print("\n\n⚠️  Người dùng hủy bỏ quá trình import!")
    except Exception as e:
        print(f"\n❌ LỖI NGHIÊM TRỌNG: {e}")
        import traceback
        traceback.print_exc()





