# =============================================================
# File: import_missing_release_notes.py
# Import các release notes còn thiếu với xử lý lỗi tốt hơn
# =============================================================

import os
import re
import json
import base64
import glob
import time
import sys
import xmlrpc.client
from typing import Dict, Tuple

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ===================== CẤU HÌNH =====================
BASE_OUTPUT_DIR = r"C:\Abivin\data_docs03"

ODOO_BASE_URL = "https://abivindocs1.odoo.com"
ODOO_DB_NAME = "abivindocs1"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "06f44edc309a7c6d558321f8809d2c72509e41df"

SPACE_NAME = "[NHÁP] Dữ liệu Docs Import"
MODEL_ARTICLE = "knowledge.article"
MODEL_ATTACHMENT = "ir.attachment"
LOCAL_ASSET_REF = "../assets_release_notes/"
# ====================================================


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
        raise SystemExit("❌ Xác thực Odoo thất bại.")
    print(f"  ✓ Đã đăng nhập vào Odoo với user ID: {uid}")
    return xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/object"), uid


def odoo_call(models, uid, model, method, *args, **kwargs):
    """Gọi RPC với timeout dài hơn"""
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
                time.sleep(3)
    raise RuntimeError(f"❌ Gọi RPC {model}.{method} thất bại sau 3 lần.")


def odoo_search(models, uid, model, domain, fields=None, limit=0):
    kwargs = {}
    if fields:
        kwargs["fields"] = fields
    if limit:
        kwargs["limit"] = limit
    return odoo_call(models, uid, model, "search_read", domain, **kwargs)


def odoo_create(models, uid, model, vals):
    return odoo_call(models, uid, model, "create", vals)


def odoo_write(models, uid, model, ids, vals):
    if not isinstance(ids, list):
        ids = [ids]
    return odoo_call(models, uid, model, "write", ids, vals)


def ensure_space(models, uid, space_name: str) -> int:
    """Tìm hoặc tạo space trong Odoo"""
    print(f"\n📁 Kiểm tra không gian làm việc: '{space_name}'...")
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name", "=", space_name)], ["id"], limit=1)
    if rec:
        print(f"  ✓ Đã tìm thấy không gian làm việc (ID: {rec[0]['id']})")
        return rec[0]['id']
    print(f"  → Không tìm thấy, đang tạo mới...")
    sid = odoo_create(models, uid, MODEL_ARTICLE, {"name": space_name, "is_article": True})
    print(f"  ✓ Đã tạo không gian làm việc (ID: {sid})")
    return sid


def upload_attachment(models, uid, file_path: str, public: bool = True) -> Tuple[int, str]:
    """Upload file lên Odoo attachment"""
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


def replace_local_assets(html_content: str, asset_map: Dict[str, str]) -> str:
    """Thay thế local asset paths bằng Odoo URLs"""
    if not asset_map:
        return html_content
    
    result = html_content
    for local_path, odoo_url in asset_map.items():
        result = result.replace(f"{LOCAL_ASSET_REF}{local_path}", odoo_url)
    return result


def main():
    """Import các release notes còn thiếu"""
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)
    
    uploaded_cache = {}
    success_count = 0
    
    # List các release notes còn thiếu
    missing_files = [
        "changelog__dec-21-2022-release-notes.json",
        "changelog__dec-29-2022.json",
        "changelog__nov-29-2022-release-notes.json",
        "changelog__oct-04m-2022-release-notes.json",
        "changelog__oct-11-2022-release-notes.json",
        "changelog__oct-18-2022-release-notes.json",
        "changelog__oct-25-2022-release-notes.json",
        "changelog__sep-13-2022-release-notes.json",
        "changelog__sep-14-2022-release-notes.json",
        "changelog__sep-27-2022-release-notes.json",
        "changelog__changelog.json",
    ]
    
    print("\n" + "="*60)
    print(f"🚀 ĐANG IMPORT {len(missing_files)} RELEASE NOTES CÒN THIẾU...")
    print("="*60 + "\n")
    
    for idx, filename in enumerate(missing_files, 1):
        json_file = os.path.join(BASE_OUTPUT_DIR, "release_notes", "content_release_notes", filename)
        
        if not os.path.exists(json_file):
            print(f"[{idx}/{len(missing_files)}] ❌ Không tìm thấy: {filename}")
            continue
        
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                doc = json.load(f)
            
            title = doc.get("title") or filename
            slug = doc.get("new_slug") or doc.get("old_slug", "")
            
            print(f"\n[{idx}/{len(missing_files)}] 📄 {title[:80]}")
            
            # Xử lý ảnh
            asset_map = {}
            assets_dir = os.path.join(BASE_OUTPUT_DIR, "release_notes", "assets_release_notes")
            
            if os.path.isdir(assets_dir):
                cache = uploaded_cache.setdefault(assets_dir, {})
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
                        print(f"    ⬆️  Upload: {fn}")
                        att_id, url = upload_attachment(models, uid, local_path, public=True)
                        if url:
                            cache[fn] = url
                            asset_map[fn] = url
                    else:
                        print(f"    ⚠️  Không tìm thấy: {local_path}")
            
            # Thay thế URL ảnh trong HTML
            body = replace_local_assets(doc.get("html_content", ""), asset_map)
            
            # Tạo hoặc cập nhật article
            vals = {
                "name": doc.get("title") or slug,
                "body": body,
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
            print(f"\n❌ LỖI: {e}\n")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*60)
    print(f"✅✅✅ HOÀN TẤT!")
    print(f"   Thành công: {success_count}/{len(missing_files)}")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Đã hủy!")
    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback
        traceback.print_exc()

