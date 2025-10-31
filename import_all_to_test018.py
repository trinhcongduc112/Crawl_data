# =============================================================
# File: import_all_to_test018.py
# Import đầy đủ tất cả dữ liệu (357 files) vào môi trường chính test018.odoo.com
# =============================================================

import os
import re
import json
import base64
import glob
import time
import sys
import xmlrpc.client
from typing import Dict, List

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ===================== CẤU HÌNH =====================
BASE_OUTPUT_DIR = r"C:\Abivin\data_docs03"

ODOO_BASE_URL = "https://test018.odoo.com"
ODOO_DB_NAME = "test018"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "3f623d85508792f81af911610db742d67a5d1845"

SPACE_NAME = "Tài liệu Abivin"
MODEL_ARTICLE = "knowledge.article"
MODEL_ATTACHMENT = "ir.attachment"
# ====================================================


# ---------------- XML-RPC CORE ----------------------
def odoo_login():
    print("\n🔐 Đang kết nối với Odoo (test018.odoo.com)...")
    common = xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/common")
    
    try:
        version_info = common.version()
        print(f"  ✓ Server version: {version_info.get('server_version', 'Unknown')}")
    except Exception as e:
        print(f"  ✗ Lỗi kiểm tra phiên bản: {e}")
    
    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if not uid:
        raise SystemExit("❌ Xác thực Odoo thất bại.")
    print(f"  ✓ Đã đăng nhập vào Odoo với user ID: {uid}")
    return xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/object"), uid


def odoo_call(models, uid, model, method, *args, **kwargs):
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
            if attempt < 2:
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
    return odoo_call(models, uid, model, "create", vals)


def odoo_write(models, uid, model, ids, vals):
    if not isinstance(ids, list):
        ids = [ids]
    if not isinstance(vals, dict):
        raise TypeError("Giá trị truyền vào write() phải là dict.")
    return odoo_call(models, uid, model, "write", ids, vals)


def ensure_space(models, uid, space_name: str) -> int:
    print(f"\n📁 Kiểm tra không gian làm việc: '{space_name}'...")
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name", "=", space_name)], ["id"], limit=1)
    if rec:
        print(f"  ✓ Đã tìm thấy không gian làm việc (ID: {rec[0]['id']})")
        return rec[0]['id']
    print(f"  → Không tìm thấy, đang tạo mới...")
    sid = odoo_create(models, uid, MODEL_ARTICLE, {"name": space_name, "is_article": True})
    print(f"  ✓ Đã tạo không gian làm việc (ID: {sid})")
    return sid


def upload_attachment(models, uid, file_path: str, public: bool = True) -> tuple:
    with open(file_path, "rb") as f:
        file_data = base64.b64encode(f.read()).decode()
    
    fn = os.path.basename(file_path)
    vals = {
        "name": fn,
        "datas": file_data,
        "public": public,
        "res_model": "knowledge.article",
    }
    
    aid = odoo_create(models, uid, MODEL_ATTACHMENT, vals)
    url = f"/web/content/{aid}?download=true"
    return aid, url


def replace_local_assets(html_content: str, asset_map: Dict[str, str], asset_prefix: str) -> str:
    """Thay thế local asset paths bằng Odoo URLs"""
    if not asset_map or not html_content:
        return html_content
    
    result = html_content
    for local_path, odoo_url in asset_map.items():
        pattern = rf"{re.escape(asset_prefix)}{re.escape(local_path)}"
        result = re.sub(pattern, odoo_url, result)
    return result


def load_all_docs() -> List[Dict]:
    """Load tất cả docs từ 3 sections"""
    all_docs = []
    
    sections = {
        "user_guide": {
            "content": os.path.join(BASE_OUTPUT_DIR, "user_guide", "content_user_guide"),
            "assets": os.path.join(BASE_OUTPUT_DIR, "user_guide", "assets_user_guide"),
        },
        "release_notes": {
            "content": os.path.join(BASE_OUTPUT_DIR, "release_notes", "content_release_notes"),
            "assets": os.path.join(BASE_OUTPUT_DIR, "release_notes", "assets_release_notes"),
        },
        "developer_guide": {
            "content": os.path.join(BASE_OUTPUT_DIR, "developer_guide", "content_developer_guide"),
            "assets": None,
        }
    }
    
    print(f"\n📂 Đang load dữ liệu từ 3 sections...")
    
    for section_key, section_info in sections.items():
        content_dir = section_info["content"]
        
        if not os.path.exists(content_dir):
            print(f"  ⚠️  Không tìm thấy: {content_dir}")
            continue
        
        json_files = sorted(glob.glob(os.path.join(content_dir, "*.json")))
        
        for jp in json_files:
            try:
                with open(jp, "r", encoding="utf-8") as f:
                    doc = json.load(f)
                
                doc["_section_key"] = section_key
                doc["_assets_dir"] = section_info["assets"] if section_info["assets"] else None
                doc["_json_file"] = jp
                all_docs.append(doc)
            except Exception as e:
                print(f"  ⚠️  Lỗi load file {jp}: {e}")
    
    print(f"  ✓ Đã load {len(all_docs)} docs")
    return all_docs


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
    
    all_docs = load_all_docs()
    
    for idx, doc in enumerate(all_docs, 1):
        total_files += 1
        try:
            title = doc.get("title") or "Unknown"
            slug = doc.get("new_slug") or doc.get("old_slug", "")
            
            print(f"\n[{idx}/{len(all_docs)}] {title[:70]}")
            
            # Xử lý ảnh
            asset_map = {}
            assets_dir = doc.get("_assets_dir")
            section = doc.get("_section_key", "")
            
            if assets_dir and os.path.isdir(assets_dir):
                cache = uploaded_cache.setdefault(assets_dir, {})
                
                # Determine asset prefix
                if section == "user_guide":
                    asset_prefix = "../assets_user_guide/"
                elif section == "release_notes":
                    asset_prefix = "../assets_release_notes/"
                else:
                    asset_prefix = "../assets_"
                
                needed_assets = set(re.findall(
                    rf"{re.escape(asset_prefix)}([A-Za-z0-9_.\-]+)",
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
                        print(f"    ⬆️  Upload: {fn}")
                        att_id, url = upload_attachment(models, uid, local_path, public=True)
                        if url:
                            cache[fn] = url
                            asset_map[fn] = url
                    else:
                        print(f"    ⚠️  Không tìm thấy: {local_path}")
            
            # Thay thế URL ảnh trong HTML
            html_content = doc.get("html_content", "")
            if asset_map and assets_dir:
                if section == "user_guide":
                    html_content = replace_local_assets(html_content, asset_map, "../assets_user_guide/")
                elif section == "release_notes":
                    html_content = replace_local_assets(html_content, asset_map, "../assets_release_notes/")
            
            # Tạo hoặc cập nhật article
            vals = {
                "name": doc.get("title") or slug,
                "body": html_content,
                "parent_id": space_id
            }
            
            # Kiểm tra article đã tồn tại
            existing_article = odoo_search(
                models, uid, MODEL_ARTICLE,
                [("name", "=", vals["name"]), ("parent_id", "=", space_id)],
                ["id"], limit=1
            )
            
            if existing_article:
                rid = existing_article[0]["id"]
                odoo_write(models, uid, MODEL_ARTICLE, [rid], vals)
                print(f"  ✓ Cập nhật bài viết (ID: {rid})")
            else:
                aid = odoo_create(models, uid, MODEL_ARTICLE, vals)
                print(f"  ✓ Tạo mới bài viết (ID: {aid})")
            
            success_count += 1
            
        except Exception as e:
            print(f"\n❌ LỖI: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*60)
    print(f"✅✅✅ IMPORT HOÀN TẤT!")
    print(f"   Tổng số file: {total_files}")
    print(f"   Thành công: {success_count}")
    print(f"   Thất bại: {total_files - success_count}")
    print(f"\n📋 Kiểm tra tại: https://test018.odoo.com")
    print(f"   Space: '{SPACE_NAME}'")
    print("="*60)


if __name__ == "__main__":
    try:
        import_all()
    except KeyboardInterrupt:
        print("\n\n⚠️  Người dùng hủy bỏ!")
    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback
        traceback.print_exc()






