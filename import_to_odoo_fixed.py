# =============================================================
# File: import_to_odoo_fixed.py
# Fix all 4 issues mentioned by supervisor
# =============================================================

import os
import re
import json
import base64
import glob
import time
import sys
import html
import xmlrpc.client
from typing import Dict, Tuple, Any, List
from pathlib import Path

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


# ===================== HELPER FUNCTIONS =====================

def escape_xml_content(text: str) -> str:
    """Escape special XML characters"""
    return html.escape(text, quote=False)


def clean_html_for_xml(html_content: str) -> str:
    """Clean HTML để hiển thị đúng trên Odoo + thêm zoom cho ảnh"""
    if not html_content:
        return ""
    
    from bs4 import BeautifulSoup
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Loại bỏ các elements không cần thiết
    for tag in soup.find_all(['script', 'style', 'link']):
        tag.decompose()
    
    # Loại bỏ tất cả attributes không cần thiết
    for tag in soup.find_all():
        # Chỉ giữ lại một số attributes hữu ích
        allowed_attrs = {'src', 'alt', 'href', 'title', 'width', 'height', 'class'}
        attrs_to_keep = {}
        for attr in allowed_attrs:
            if tag.has_attr(attr):
                attrs_to_keep[attr] = tag[attr]
        tag.attrs = attrs_to_keep
    
    # FIX ZOOM ẢNH: 1 click để zoom
    for img in soup.find_all('img'):
        # Loại bỏ onclick cũ nếu có
        if 'onclick' in img.attrs:
            del img['onclick']
        
        # Thêm style và onclick mới
        img['style'] = 'max-width: 100%; height: auto; cursor: zoom-in; transition: transform 0.3s ease;'
        # onclick: toggle zoom với 1 click
        img['onclick'] = 'var tf = this.style.transform || "scale(1)"; this.style.transform = (tf === "scale(2)") ? "scale(1)" : "scale(2)";'
    
    return str(soup)


def odoo_login() -> Tuple[xmlrpc.client.ServerProxy, int]:
    """Đăng nhập vào Odoo"""
    print("\n🔐 Đang kết nối với Odoo...")
    common = xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/common")
    
    try:
        version_info = common.version()
        print(f"  ✓ Server version: {version_info.get('server_version', 'Unknown')}")
    except Exception as e:
        print(f"  ⚠️  Không thể kiểm tra phiên bản: {e}")
    
    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if not uid:
        raise SystemExit("❌ Xác thực Odoo thất bại. Kiểm tra lại API key hoặc quyền truy cập.")
    print(f"  ✓ Đã đăng nhập vào Odoo với user ID: {uid}")
    return xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/object"), uid


def odoo_call(models, uid, model, method, *args, **kwargs):
    """Gọi RPC chuẩn cho Odoo với retry"""
    args = list(args) if args else []
    kwargs = kwargs or {}
    for attempt in range(3):
        try:
            return models.execute_kw(
                ODOO_DB_NAME, uid, ODOO_API_KEY,
                model, method, args, kwargs
            )
        except Exception as e:
            print(f"  [RPC ERROR] {model}.{method} attempt {attempt+1}/3: {str(e)[:100]}")
            if attempt < 2:
                time.sleep(2)
    raise RuntimeError(f"❌ Gọi RPC {model}.{method} thất bại sau 3 lần.")


def odoo_search(models, uid, model, domain, fields=None, limit=0):
    """Search records trong Odoo"""
    kwargs = {}
    if fields:
        kwargs["fields"] = fields
    if limit:
        kwargs["limit"] = limit
    return odoo_call(models, uid, model, "search_read", domain, **kwargs)


def odoo_create(models, uid, model, vals):
    """Tạo record mới trong Odoo"""
    if not isinstance(vals, dict):
        raise TypeError("Giá trị truyền vào create() phải là dict.")
    return odoo_call(models, uid, model, "create", vals)


def odoo_write(models, uid, model, ids, vals):
    """Cập nhật record trong Odoo"""
    if not isinstance(ids, list):
        ids = [ids]
    if not isinstance(vals, dict):
        raise TypeError("Giá trị truyền vào write() phải là dict.")
    return odoo_call(models, uid, model, "write", ids, vals)


def ensure_space(models, uid, space_name: str) -> int:
    """Tìm hoặc tạo space trong Odoo"""
    print(f"\n📁 Kiểm tra không gian làm việc: '{space_name}'...")
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name", "=", space_name)], ["id"], limit=1)
    if rec:
        print(f"  ✓ Đã tìm thấy không gian làm việc (ID: {rec[0]['id']})")
        return rec[0]['id']
    print(f"  + Tạo mới không gian...")
    space_id = odoo_create(models, uid, MODEL_ARTICLE, {
        "name": space_name,
        "body": "<p>Không gian chứa tài liệu imported từ docs.abivin.com</p>"
    })
    print(f"  ✓ Đã tạo mới space (ID: {space_id})")
    return space_id


def ensure_category(models, uid, parent_id: int, category_name: str) -> int:
    """Tìm hoặc tạo category trong Odoo"""
    # Tìm category đã tồn tại
    existing = odoo_search(models, uid, MODEL_ARTICLE, 
                           [("name", "=", category_name), ("parent_id", "=", parent_id)], 
                           ["id"], limit=1)
    if existing:
        return existing[0]['id']
    
    # Tạo mới category
    cat_id = odoo_create(models, uid, MODEL_ARTICLE, {
        "name": category_name,
        "parent_id": parent_id
    })
    return cat_id


def guess_mimetype(name: str) -> str:
    """Xác định MIME type từ tên file"""
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
        # URL đúng format cho Odoo - dùng /web/content/
        url = f"{ODOO_BASE_URL}/web/content/{att_id}"
        return att_id, url
    except Exception as e:
        print(f"  ✗ Lỗi upload ảnh '{path}': {e}")
        return None, None


def replace_local_assets(html_content: str, asset_map: Dict[str, str]) -> str:
    """Thay thế đường dẫn ảnh local bằng URL Odoo"""
    if not html_content:
        return ""
    
    # Pattern mới: tìm ../assets_[section]/filename
    def replace_func(match):
        full_path = match.group(1)  # ../assets_user_guide/filename.png
        filename = match.group(2)   # filename.png
        if filename in asset_map:
            return f'src="{asset_map[filename]}"'
        return match.group(0)
    
    # Tìm src="../assets_..."
    pattern = r'src="(\.\./assets_[^/]+/([^"]+))"'
    result = re.sub(pattern, replace_func, html_content)
    return result


def load_all_docs() -> List[Dict]:
    """Load tất cả docs và sắp xếp theo order_index"""
    all_docs = []
    
    # PHÂN BIỆT RÕ RÀNG: Load theo section riêng biệt
    sections = {
        "user_guide": {
            "content": os.path.join(BASE_OUTPUT_DIR, "user_guide", "content_user_guide"),
            "assets": os.path.join(BASE_OUTPUT_DIR, "user_guide", "assets_user_guide"),
            "category": "User Guide"
        },
        "release_notes": {
            "content": os.path.join(BASE_OUTPUT_DIR, "release_notes", "content_release_notes"),
            "assets": os.path.join(BASE_OUTPUT_DIR, "release_notes", "assets_release_notes"),
            "category": "Release Notes"
        },
        "developer_guide": {
            "content": os.path.join(BASE_OUTPUT_DIR, "developer_guide", "content_developer_guide"),
            "assets": None,  # Developer guide không có ảnh
            "category": "Developer Guide"
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
                doc["_section_category"] = section_info["category"]
                doc["_assets_dir"] = section_info["assets"] if section_info["assets"] else None
                doc["_json_file"] = jp
                all_docs.append(doc)
            except Exception as e:
                print(f"  ⚠️  Lỗi load file {jp}: {e}")
    
    # Sắp xếp theo order_index
    all_docs.sort(key=lambda x: x.get("order_index", 999999))
    
    print(f"  ✓ Đã load {len(all_docs)} docs")
    
    return all_docs


# ===================== MAIN IMPORT FUNCTION =====================

def import_all():
    """Import tất cả docs vào Odoo với categorization"""
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)
    
    # Load tất cả docs
    all_docs = load_all_docs()
    
    # Cache để tránh upload lại ảnh
    uploaded_cache: Dict[str, Dict[str, str]] = {}
    
    # Map slug -> article_id để set parent
    article_map: Dict[str, int] = {}
    
    # Map section -> category_id để tạo categories
    category_map: Dict[str, int] = {}
    
    total_files = len(all_docs)
    success_count = 0
    failed_count = 0
    
    print("\n" + "="*60)
    print("🚀 BẮT ĐẦU QUÁ TRÌNH IMPORT...")
    print("="*60 + "\n")
    
    for idx, doc in enumerate(all_docs, 1):
        try:
            slug = doc.get("old_slug") or doc.get("new_slug", "")
            title = doc.get("title") or slug
            section_key = doc.get("_section_key", "unknown")
            section_category = doc.get("_section_category", "Unknown")
            assets_dir = doc.get("_assets_dir")
            
            print(f"\n[{idx}/{total_files}] {title[:60]}")
            print(f"  📂 Section: {section_category}")
            
            # Đảm bảo category tồn tại cho section này
            if section_category not in category_map:
                category_id = ensure_category(models, uid, space_id, section_category)
                category_map[section_category] = category_id
                print(f"  ✓ Category: {section_category}")
            else:
                category_id = category_map[section_category]
            
            # 1. Xử lý ảnh
            asset_map: Dict[str, str] = {}
            if assets_dir:
                # Tìm tất cả các ảnh được tham chiếu
                html_content = doc.get("html_content", "")
                # Pattern mới: tìm src="../assets_.../filename"
                pattern = r'src="\.\./assets_[^/]+/([^"]+)"'
                needed_assets = set(re.findall(pattern, html_content))
                
                if needed_assets:
                    print(f"  📸 Tìm thấy {len(needed_assets)} ảnh")
                    
                    # Cache per assets directory
                    cache_key = assets_dir
                    cache = uploaded_cache.setdefault(cache_key, {})
                    
                    for filename in needed_assets:
                        if filename in cache:
                            asset_map[filename] = cache[filename]
                            continue
                        
                        local_path = os.path.join(assets_dir, filename)
                        if os.path.exists(local_path):
                            print(f"    ⬆️  Upload: {filename}")
                            att_id, url = upload_attachment(models, uid, local_path, public=True)
                            if url:
                                cache[filename] = url
                                asset_map[filename] = url
                        else:
                            print(f"    ⚠️  Không tìm thấy: {filename}")
            
            # 2. Xử lý content
            html_content = doc.get("html_content", "")
            body = replace_local_assets(html_content, asset_map)
            body = clean_html_for_xml(body)  # Thêm zoom cho ảnh
            body = f'<div style="padding: 20px;">{body}</div>'
            
            # 3. Tạo hoặc cập nhật article (với category)
            vals = {
                "name": title,
                "body": body,
                "parent_id": category_id  # Parent là category, không phải space
            }
            
            # Kiểm tra article đã tồn tại
            existing = odoo_search(
                models, uid, MODEL_ARTICLE,
                [("name", "=", title), ("parent_id", "=", category_id)],
                ["id"], limit=1
            )
            
            if existing:
                rid = existing[0]["id"]
                try:
                    odoo_write(models, uid, MODEL_ARTICLE, [rid], vals)
                    print(f"  ✓ Cập nhật bài viết (ID: {rid})")
                    article_map[slug] = rid
                    success_count += 1
                except Exception as e:
                    print(f"  ✗ Lỗi khi cập nhật: {str(e)[:100]}")
                    failed_count += 1
            else:
                try:
                    aid = odoo_create(models, uid, MODEL_ARTICLE, vals)
                    print(f"  ✓ Tạo mới bài viết (ID: {aid})")
                    article_map[slug] = aid
                    success_count += 1
                except Exception as e:
                    print(f"  ✗ Lỗi khi tạo mới: {str(e)[:100]}")
                    failed_count += 1
            
        except Exception as e:
            print(f"  ✗ Lỗi: {str(e)[:100]}")
            failed_count += 1
    
    # Summary
    print("\n" + "="*60)
    print(f"✅✅✅ IMPORT HOÀN TẤT! ✅✅✅")
    print(f"   Tổng số file: {total_files}")
    print(f"   Thành công: {success_count}")
    print(f"   Thất bại: {failed_count}")
    print(f"\n📋 Hãy kiểm tra kết quả trong Odoo:")
    print(f"   Không gian: '{SPACE_NAME}'")
    print(f"   Categories: User Guide, Release Notes, Developer Guide")
    print("="*60)


# ===================== MAIN =====================

if __name__ == "__main__":
    try:
        import_all()
    except KeyboardInterrupt:
        print("\n\n⚠️  Người dùng hủy bỏ quá trình import!")
    except Exception as e:
        print(f"\n❌ LỖI NGHIÊM TRỌNG: {e}")
        import traceback
        traceback.print_exc()


