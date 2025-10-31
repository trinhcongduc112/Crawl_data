"""
Import User Guide articles to Odoo with proper categorization
Based on the actual structure from docs.abivin.com
"""

import os
import json
import glob
import xmlrpc.client
import time
import sys
import base64
import re
from typing import Dict, Tuple, List
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ===================== CẤU HÌNH =====================
BASE_OUTPUT_DIR = r"C:\Abivin\data_docs03"
USER_GUIDE_CONTENT_DIR = os.path.join(BASE_OUTPUT_DIR, "user_guide", "content_user_guide")
USER_GUIDE_ASSETS_DIR = os.path.join(BASE_OUTPUT_DIR, "user_guide", "assets_user_guide")

ODOO_BASE_URL = "https://test018.odoo.com"
ODOO_DB_NAME = "test018"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "3f623d85508792f81af911610db742d67a5d1845"

SPACE_NAME = "Tài liệu Abivin"
MODEL_ARTICLE = "knowledge.article"
MODEL_ATTACHMENT = "ir.attachment"
# ====================================================

# ===================== HELPER FUNCTIONS =====================

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
    return odoo_call(models, uid, model, "create", vals)


def odoo_write(models, uid, model, ids, vals):
    """Cập nhật record trong Odoo"""
    if not isinstance(ids, list):
        ids = [ids]
    return odoo_call(models, uid, model, "write", ids, vals)


def odoo_delete(models, uid, model, ids):
    """Xóa record trong Odoo"""
    if not isinstance(ids, list):
        ids = [ids]
    return odoo_call(models, uid, model, "unlink", ids)


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
    existing = odoo_search(models, uid, MODEL_ARTICLE, 
                           [("name", "=", category_name), ("parent_id", "=", parent_id)], 
                           ["id"], limit=1)
    if existing:
        return existing[0]['id']
    
    cat_id = odoo_create(models, uid, MODEL_ARTICLE, {
        "name": category_name,
        "parent_id": parent_id
    })
    return cat_id


def upload_attachment(models, uid, path: str, public=True):
    """Upload ảnh lên Odoo và trả về URL"""
    try:
        with open(path, "rb") as f:
            datas_b64 = base64.b64encode(f.read()).decode()
        
        ext = os.path.splitext(path.lower())[1]
        mimetype_map = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
        }
        mimetype = mimetype_map.get(ext, "application/octet-stream")
        
        att_id = odoo_create(models, uid, MODEL_ATTACHMENT, {
            "name": os.path.basename(path),
            "datas": datas_b64,
            "mimetype": mimetype,
            "public": public
        })
        url = f"{ODOO_BASE_URL}/web/content/{att_id}"
        return att_id, url
    except Exception as e:
        return None, None


def clean_html_for_xml(html_content: str) -> str:
    """Clean HTML để hiển thị đúng trên Odoo"""
    if not html_content:
        return ""
    
    try:
        from bs4 import BeautifulSoup
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Loại bỏ các elements không cần thiết
        for tag in soup.find_all(['script', 'style', 'link']):
            tag.decompose()
        
        # Loại bỏ tất cả attributes không cần thiết
        for tag in soup.find_all():
            allowed_attrs = {'src', 'alt', 'href', 'title', 'width', 'height', 'class'}
            attrs_to_keep = {}
            for attr in allowed_attrs:
                if tag.has_attr(attr):
                    attrs_to_keep[attr] = tag[attr]
            tag.attrs = attrs_to_keep
        
        # Thêm zoom cho ảnh
        for img in soup.find_all('img'):
            img['style'] = 'max-width: 100%; height: auto; cursor: zoom-in;'
            img['onclick'] = 'this.style.transform = this.style.transform === "scale(2)" ? "scale(1)" : "scale(2)"; this.style.transition = "transform 0.3s ease";'
        
        return str(soup)
    except:
        return html_content


def replace_local_assets(html_content: str, asset_map: Dict[str, str]) -> str:
    """Thay thế đường dẫn ảnh local bằng URL Odoo"""
    if not html_content:
        return ""
    
    def replace_func(match):
        full_path = match.group(1)
        filename = match.group(2)
        if filename in asset_map:
            return f'src="{asset_map[filename]}"'
        return match.group(0)
    
    pattern = r'src="(\.\./assets_user_guide/([^"]+))"'
    result = re.sub(pattern, replace_func, html_content)
    return result


# ===================== DELETE EXISTING ARTICLES =====================

def delete_existing_user_guide(models, uid, space_id: int):
    """Xóa tất cả articles trong User Guide"""
    print("\n🗑️  Đang xóa các bài viết User Guide cũ...")
    
    # Tìm tất cả articles trong space
    articles = odoo_search(models, uid, MODEL_ARTICLE, 
                          [("parent_path", "=like", f"{space_id}/%")], 
                          ["id", "name"])
    
    if articles:
        print(f"  Tìm thấy {len(articles)} articles")
        # Xóa tất cả
        for article in articles:
            try:
                odoo_delete(models, uid, MODEL_ARTICLE, [article['id']])
                print(f"  ✓ Đã xóa: {article['name']}")
            except:
                pass
        print(f"  ✓ Đã xóa tất cả articles cũ")
    else:
        print(f"  ✓ Không có articles cũ để xóa")


# ===================== CATEGORY MAPPING =====================

def get_article_category(doc: Dict) -> List[str]:
    """
    Xác định category cho article
    Returns: List of category path, e.g. ["User Guide", "Getting Started"]
    """
    origin_url = doc.get("origin_url", "").lower()
    title = doc.get("title", "").lower()
    
    # Getting Started
    getting_started_keywords = [
        "how-to-use-this-user-guide",
        "abivin-vroute-glossary",
        "abivin-vroute-system-resources",
        "system-requirements",
        "user-register",
        "first-time-user-setup",
        "system-operations",
        "search-and-filter-functions",
        "page-display-and-navigation-functions",
        "how-to-get-coordinates-of-places",
        "api-key"
    ]
    
    for keyword in getting_started_keywords:
        if keyword in origin_url:
            return ["User Guide", "Getting Started"]
    
    # Web App Tutorials - VRP/DC Model
    if "vrp-dc" in origin_url or ("vrp" in origin_url and ("dc" in origin_url or "depot" in origin_url)):
        return ["User Guide", "Web App Tutorials", "VRP/DC Model"]
    
    # Web App Tutorials - VRP - Carrier Plan for Shipper
    if "carrier" in origin_url or ("vrp" in origin_url and "shipper" in origin_url):
        return ["User Guide", "Web App Tutorials", "VRP - Carrier Plan for Shipper"]
    
    # Web App Tutorials - PDP Model
    if "pdp" in origin_url:
        if "in-house" in origin_url or "inhouse" in origin_url:
            return ["User Guide", "Web App Tutorials", "PDP Model - In-House Fleet"]
        elif "outsourcing" in origin_url:
            return ["User Guide", "Web App Tutorials", "PDP Model - Outsourcing Fleet"]
        else:
            return ["User Guide", "Web App Tutorials", "PDP Model"]
    
    # Web App Tutorials - International Logistics
    if "international-logistics" in origin_url or "freight-transport" in origin_url:
        if "inland" in origin_url:
            return ["User Guide", "Web App Tutorials", "International Logistics - Inland"]
        else:
            return ["User Guide", "Web App Tutorials", "International Logistics"]
    
    # Web App Tutorials - Route Plan Optimization
    if "route-plan" in origin_url and "optimization" in origin_url:
        return ["User Guide", "Web App Tutorials", "Route Plan Optimization"]
    
    # Mobile App Tutorials
    if "mobile-app" in origin_url or "delivery-app" in origin_url or "consumer-app" in origin_url:
        if "vrp" in origin_url or "dc" in origin_url:
            return ["User Guide", "Mobile App Tutorials", "VRP/DC Model"]
        elif "pdp" in origin_url:
            return ["User Guide", "Mobile App Tutorials", "PDP Model"]
        elif "freight" in origin_url or "sea" in origin_url or "road" in origin_url or "barge" in origin_url:
            return ["User Guide", "Mobile App Tutorials", "Intermodal Container Transport"]
        else:
            return ["User Guide", "Mobile App Tutorials", "Delivery App - General Instruction"]
    
    # WMS and TMS Processes
    if any(kw in origin_url for kw in ["inbound-logistics", "outbound-logistics", "pick-and-pack", "shipping-action", "inventory", "tms"]):
        return ["User Guide", "WMS and TMS Processes"]
    
    # Processes & Policies
    if any(kw in origin_url for kw in ["privacy-policy", "terms-and-conditions", "sla"]):
        return ["User Guide", "Processes & Policies"]
    
    # FAQs
    if any(kw in origin_url for kw in ["why-", "are-the-", "cant-", "missing-order", "configuration-", "i-cannot-", "i-cant-", "is-there-"]):
        if "customer" in origin_url or "customers" in origin_url:
            return ["User Guide", "FAQs", "Customer"]
        elif "product" in origin_url or "products" in origin_url:
            return ["User Guide", "FAQs", "Product"]
        elif "organization" in origin_url or "organizations" in origin_url:
            return ["User Guide", "FAQs", "Organization"]
        else:
            return ["User Guide", "FAQs", "General"]
    
    # Miscellaneous Support
    if any(kw in origin_url for kw in ["online-support", "install-", "how-to-install-", "teamviewer", "apk", "support"]):
        return ["User Guide", "Miscellaneous Support"]
    
    # Default - xử lý các articles còn lại
    return ["User Guide", "Other Articles"]


# ===================== MAIN IMPORT FUNCTION =====================

def import_user_guide():
    """Import User Guide vào Odoo với categorization chi tiết"""
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)
    
    # Xóa các articles cũ trong User Guide
    delete_existing_user_guide(models, uid, space_id)
    
    # Load tất cả user guide docs
    print(f"\n📂 Đang load dữ liệu từ user_guide...")
    json_files = sorted(glob.glob(os.path.join(USER_GUIDE_CONTENT_DIR, "*.json")))
    
    all_docs = []
    for jp in json_files:
        try:
            with open(jp, "r", encoding="utf-8") as f:
                doc = json.load(f)
                doc["_json_file"] = jp
                all_docs.append(doc)
        except Exception as e:
            pass
    
    # Sắp xếp theo order_index
    all_docs.sort(key=lambda x: x.get("order_index", 999999))
    
    print(f"  ✓ Đã load {len(all_docs)} docs")
    
    # Cache để tránh upload lại ảnh
    uploaded_cache: Dict[str, str] = {}
    
    # Map để tạo categories
    category_path_map: Dict[str, int] = {}
    
    total_files = len(all_docs)
    success_count = 0
    failed_count = 0
    
    print("\n" + "="*60)
    print("🚀 BẮT ĐẦU QUÁ TRÌNH IMPORT USER GUIDE...")
    print("="*60 + "\n")
    
    for idx, doc in enumerate(all_docs, 1):
        try:
            title = doc.get("title", "Untitled")
            origin_url = doc.get("origin_url", "")
            
            print(f"\n[{idx}/{total_files}] {title}")
            
            # Xác định category path
            category_path = get_article_category(doc)
            print(f"  📂 Category: {' > '.join(category_path)}")
            
            # Đảm bảo tất cả categories được tạo (tạo từ "User Guide" down)
            current_parent_id = space_id
            
            # Tạo từng level category
            for category_name in category_path:
                cache_key = f"{current_parent_id}:{category_name}"
                if cache_key not in category_path_map:
                    cat_id = ensure_category(models, uid, current_parent_id, category_name)
                    category_path_map[cache_key] = cat_id
                    print(f"    ✓ Category: {category_name} (ID: {cat_id})")
                else:
                    cat_id = category_path_map[cache_key]
                current_parent_id = cat_id
            
            # Parent ID của article là category cuối cùng
            article_parent_id = current_parent_id
            
            # 1. Xử lý ảnh
            html_content = doc.get("html_content", "")
            pattern = r'src="\.\./assets_user_guide/([^"]+)"'
            needed_assets = set(re.findall(pattern, html_content))
            
            asset_map: Dict[str, str] = {}
            if needed_assets:
                print(f"  📸 Tìm thấy {len(needed_assets)} ảnh")
                for filename in needed_assets:
                    if filename in uploaded_cache:
                        asset_map[filename] = uploaded_cache[filename]
                        continue
                    
                    local_path = os.path.join(USER_GUIDE_ASSETS_DIR, filename)
                    if os.path.exists(local_path):
                        print(f"    ⬆️  Upload: {filename}")
                        att_id, url = upload_attachment(models, uid, local_path, public=True)
                        if url:
                            uploaded_cache[filename] = url
                            asset_map[filename] = url
                    else:
                        print(f"    ⚠️  Không tìm thấy: {filename}")
            
            # 2. Xử lý content
            body = replace_local_assets(html_content, asset_map)
            body = clean_html_for_xml(body)
            body = f'<div style="padding: 20px;">{body}</div>'
            
            # 3. Tạo article
            vals = {
                "name": title,
                "body": body,
                "parent_id": article_parent_id
            }
            
            try:
                aid = odoo_create(models, uid, MODEL_ARTICLE, vals)
                print(f"  ✓ Tạo bài viết (ID: {aid})")
                success_count += 1
            except Exception as e:
                print(f"  ✗ Lỗi: {str(e)[:100]}")
                failed_count += 1
            
        except Exception as e:
            print(f"  ✗ Lỗi: {str(e)[:100]}")
            failed_count += 1
            import traceback
            traceback.print_exc()
    
    # Summary
    print("\n" + "="*60)
    print(f"✅✅✅ IMPORT HOÀN TẤT! ✅✅✅")
    print(f"   Tổng số file: {total_files}")
    print(f"   Thành công: {success_count}")
    print(f"   Thất bại: {failed_count}")
    print(f"\n📋 Hãy kiểm tra kết quả trong Odoo:")
    print(f"   Không gian: '{SPACE_NAME}'")
    print(f"   User Guide với categories: Getting Started, Web App Tutorials, Mobile App Tutorials, etc.")
    print("="*60)


# ===================== MAIN =====================

if __name__ == "__main__":
    try:
        import_user_guide()
    except KeyboardInterrupt:
        print("\n\n⚠️  Người dùng hủy bỏ quá trình import!")
    except Exception as e:
        print(f"\n❌ LỖI NGHIÊM TRỌNG: {e}")
        import traceback
        traceback.print_exc()






