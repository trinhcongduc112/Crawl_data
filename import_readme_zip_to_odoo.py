# =============================================================
# File: import_readme_zip_to_odoo.py
# Import trực tiếp từ ReadMe ZIP export vào Odoo
# =============================================================

import os
import re
import yaml
import json
import base64
import markdown
import sys
import xmlrpc.client
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ===================== CẤU HÌNH =====================
README_EXPORT_DIR = r"C:\Abivin\data_docs03\abivin-v4.0-2025-11-03T16-58-05_8cddcbc"
ODOO_BASE_URL = "https://test018.odoo.com"
ODOO_DB_NAME = "test018"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "3f623d85508792f81af911610db742d67a5d1845"
SPACE_NAME = "Tài liệu Abivin 03"
MODEL_ARTICLE = "knowledge.article"
MODEL_ATTACHMENT = "ir.attachment"
# ====================================================

# Section priority mapping
SECTION_PRIORITY = {
    "Getting Started": 0,
    "Data Dictionary": 1,
    "Web App Tutorials": 2,
    "HDSD Ứng Dụng Web": 3,
    "Mobile App Tutorials": 4,
    "WMS and TMS Processes": 5,
    "Processes & Policies": 6,
    "Miscellaneous Support": 7,
    "FAQs": 8,
    "reference": 9,  # Developer Guide / API Reference
    "recipes": 10,  # Recipes
}

# Cache upload ảnh để tránh upload trùng
IMAGE_UPLOAD_CACHE: Dict[str, str] = {}

# ---------------- ATTACHMENT UTILS -------------------
def guess_mimetype(name: str) -> str:
    ext = os.path.splitext(name.lower())[1]
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
        ".webp": "image/webp"
    }.get(ext, "application/octet-stream")


def upload_attachment(models, uid, path: str, public=True) -> Tuple[Optional[int], Optional[str]]:
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
            import time
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
        "body": "<p>Không gian chứa tài liệu imported từ ReadMe ZIP export</p>"
    })
    print(f"  ✓ Đã tạo mới space (ID: {space_id})")
    return space_id


def read_order_yaml(order_path: Path) -> List[str]:
    """Đọc _order.yaml và trả về danh sách slug/folder theo thứ tự"""
    if not order_path.exists():
        return []
    try:
        with open(order_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Parse YAML list format: "- item1\n- item2\n"
        items = []
        for line in lines:
            line = line.strip()
            if line.startswith('- '):
                items.append(line[2:].strip())
        return items
    except Exception as e:
        print(f"  ⚠️  Lỗi đọc {order_path}: {e}")
        return []


def operation_id_to_path_method(operation_id: str) -> Tuple[Optional[str], Optional[str]]:
    """Convert operationId như 'post_customers-create' thành path và method"""
    if not operation_id:
        return None, None
    
    # Format: {method}_{path-with-dashes}
    # Ví dụ: post_customers-create -> method=post, path=/customers/create
    parts = operation_id.split('_', 1)
    if len(parts) != 2:
        return None, None
    
    method = parts[0].lower()
    path_part = parts[1].replace('-', '/')
    
    # Tạo path với leading slash
    path = f"/{path_part}"
    
    return path, method


def parse_openapi_endpoint(openapi_spec: dict, operation_id: str, title: str = None) -> str:
    """Parse một endpoint từ OpenAPI spec dựa trên operationId hoặc title"""
    html_parts = []
    found_endpoint = None
    found_path = None
    found_method = None
    
    # Thử tìm bằng operationId trước (nếu có)
    if operation_id:
        for path, methods in openapi_spec.get("paths", {}).items():
            for method, details in methods.items():
                if method.lower() in ["get", "post", "put", "patch", "delete", "head", "options"]:
                    if details.get("operationId") == operation_id:
                        found_endpoint = details
                        found_path = path
                        found_method = method
                        break
            if found_endpoint:
                break
    
    # Nếu không tìm thấy bằng operationId, thử convert operationId sang path+method
    if not found_endpoint and operation_id:
        path_pattern, method_pattern = operation_id_to_path_method(operation_id)
        if path_pattern and method_pattern:
            for path, methods in openapi_spec.get("paths", {}).items():
                # So khớp path (có thể có params như {id})
                if path_pattern in path or path == path_pattern:
                    if method_pattern in methods:
                        found_endpoint = methods[method_pattern]
                        found_path = path
                        found_method = method_pattern
                        break
                if found_endpoint:
                    break
    
    # Nếu vẫn không tìm thấy và có title, thử tìm bằng title
    # Title thường có format: /customers/create
    if not found_endpoint and title:
        # Title có thể là path luôn
        title_path = title.strip()
        if title_path.startswith('/'):
            for path, methods in openapi_spec.get("paths", {}).items():
                if path == title_path or title_path in path:
                    # Thử tìm method phù hợp (ưu tiên post nếu có)
                    for method in ['post', 'get', 'put', 'patch', 'delete']:
                        if method in methods:
                            found_endpoint = methods[method]
                            found_path = path
                            found_method = method
                            break
                    if found_endpoint:
                        break
    
    if found_endpoint:
        summary = found_endpoint.get("summary", found_path or title or "API Endpoint")
        description = found_endpoint.get("description", "")
        
        html_parts.append(f"<h2>{summary}</h2>")
        if description:
            md = markdown.Markdown(extensions=['fenced_code', 'tables', 'nl2br'])
            html_parts.append(md.convert(description))
        
        if found_method:
            html_parts.append(f"<p><strong>Method:</strong> <code>{found_method.upper()}</code></p>")
        if found_path:
            html_parts.append(f"<p><strong>Path:</strong> <code>{found_path}</code></p>")
        
        # Parameters
        params = found_endpoint.get("parameters", [])
        if params:
            html_parts.append("<h3>Parameters</h3><ul>")
            for param in params:
                param_name = param.get("name", "")
                param_in = param.get("in", "")
                param_desc = param.get("description", "")
                param_req = param.get("required", False)
                html_parts.append(f"<li><code>{param_name}</code> ({param_in})")
                if param_req:
                    html_parts.append(" <strong>[Required]</strong>")
                if param_desc:
                    html_parts.append(f": {param_desc}")
                html_parts.append("</li>")
            html_parts.append("</ul>")
        
        # Request Body
        request_body = found_endpoint.get("requestBody", {})
        if request_body:
            html_parts.append("<h3>Request Body</h3>")
            req_desc = request_body.get("description", "")
            if req_desc:
                md = markdown.Markdown(extensions=['fenced_code', 'tables', 'nl2br'])
                html_parts.append(md.convert(req_desc))
        
        # Responses
        responses = found_endpoint.get("responses", {})
        if responses:
            html_parts.append("<h3>Responses</h3>")
            for status, resp in responses.items():
                html_parts.append(f"<h4>HTTP {status}</h4>")
                resp_desc = resp.get("description", "")
                if resp_desc:
                    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'nl2br'])
                    html_parts.append(md.convert(resp_desc))
        
        return "".join(html_parts)
    
    return "<p>API endpoint documentation not found in OpenAPI spec.</p>"


def parse_markdown_file(md_path: Path, base_dir: Path = None) -> Dict[str, Any]:
    """Parse markdown file và trả về dict với title, content, metadata"""
    if not md_path.exists():
        return None
    
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse front matter
        front_matter = {}
        body = content
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    front_matter = yaml.safe_load(parts[1]) or {}
                    body = parts[2].strip()
                except:
                    body = content
        
        title = front_matter.get('title') or md_path.stem.replace('-', ' ').title()
        
        # Nếu body rỗng và có thông tin API trong front matter, parse từ OpenAPI JSON
        if not body and base_dir and front_matter.get('api'):
            api_file = front_matter['api'].get('file')
            operation_id = front_matter['api'].get('operationId')
            
            if api_file and operation_id:
                # Tìm file OpenAPI JSON - thử nhiều vị trí
                possible_paths = [
                    base_dir / 'reference' / api_file,  # Root của reference
                    md_path.parent / api_file,  # Cùng thư mục với file .md
                    base_dir / api_file,  # Root của export
                ]
                
                openapi_path = None
                for path in possible_paths:
                    if path.exists():
                        openapi_path = path
                        break
                
                if openapi_path:
                    try:
                        with open(openapi_path, 'r', encoding='utf-8-sig') as f:
                            openapi_spec = json.load(f)
                        html = parse_openapi_endpoint(openapi_spec, operation_id, title)
                        if html and html != "<p>API endpoint documentation not found in OpenAPI spec.</p>":
                            return {
                                'title': title,
                                'html_content': html,
                                'front_matter': front_matter,
                                'slug': md_path.stem
                            }
                        else:
                            print(f"    ⚠️  Không tìm thấy endpoint cho operationId '{operation_id}' hoặc title '{title}' trong {api_file}")
                    except json.JSONDecodeError as e:
                        print(f"    ⚠️  Lỗi parse JSON từ {api_file}: {e}")
                    except Exception as e:
                        print(f"    ⚠️  Không thể parse OpenAPI từ {api_file}: {e}")
                else:
                    print(f"    ⚠️  Không tìm thấy file OpenAPI: {api_file} (đã thử: {[str(p) for p in possible_paths]})")
        
        # Convert markdown to HTML (nếu có body)
        if body:
            md = markdown.Markdown(extensions=['fenced_code', 'tables', 'nl2br'])
            html = md.convert(body)
        else:
            # Nếu không có body và không parse được từ OpenAPI, tạo placeholder
            html = f"<p>Nội dung cho <strong>{title}</strong></p>"
        
        return {
            'title': title,
            'html_content': html,
            'front_matter': front_matter,
            'slug': md_path.stem
        }
    except Exception as e:
        print(f"  ⚠️  Lỗi parse {md_path}: {e}")
        return None


def find_md_files(directory: Path) -> List[Path]:
    """Tìm tất cả file .md trong directory (recursive)"""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file != '_order.yaml':
                md_files.append(Path(root) / file)
    return md_files


def build_doc_tree(base_dir: Path) -> List[Dict[str, Any]]:
    """Xây dựng cây tài liệu từ ReadMe export, tạo parent chỉ khi có dữ liệu"""
    all_docs = []
    file_counter = {'user_guide': 0, 'developer_guide': 0, 'release_notes': 0}
    
    def process_directory_recursive(current_dir: Path, parent_slug: str, section_key: str, base_path: Path, root_base_dir: Path):
        """Đọc TẤT CẢ file .md trong thư mục (recursive) và đặt dưới parent_slug, giữ thứ tự từ _order.yaml"""
        # Đọc _order.yaml ở level hiện tại
        order_path = current_dir / '_order.yaml'
        order_items = read_order_yaml(order_path)
        
        # Tạo danh sách file đã xử lý để tránh trùng
        processed = set()
        
        # Xử lý theo thứ tự trong _order.yaml
        for idx, item in enumerate(order_items):
            item_path = current_dir / item
            
            # Nếu là thư mục
            if item_path.is_dir():
                # Đệ quy xử lý thư mục con (giữ thứ tự từ _order.yaml của nó)
                process_directory_recursive(item_path, parent_slug, section_key, base_path, root_base_dir)
                
                # Nếu có index.md trong thư mục này, cũng xử lý
                index_md = item_path / 'index.md'
                if index_md.exists() and index_md not in processed:
                    doc_data = parse_markdown_file(index_md, root_base_dir)
                    if doc_data:
                        file_counter[section_key] += 1
                        doc_data['parent_slug'] = parent_slug
                        doc_data['order_index'] = file_counter[section_key]
                        doc_data['section'] = section_key
                        rel_path = index_md.relative_to(base_path)
                        doc_data['slug'] = str(rel_path).replace('\\', '/').replace('.md', '').replace('/', '-')
                        all_docs.append(doc_data)
                        processed.add(index_md)
            
            # Nếu là file .md trực tiếp
            elif (current_dir / f"{item}.md").exists():
                md_file = current_dir / f"{item}.md"
                if md_file not in processed:
                    doc_data = parse_markdown_file(md_file, root_base_dir)
                    if doc_data:
                        file_counter[section_key] += 1
                        doc_data['parent_slug'] = parent_slug
                        doc_data['order_index'] = file_counter[section_key]
                        doc_data['section'] = section_key
                        rel_path = md_file.relative_to(base_path)
                        doc_data['slug'] = str(rel_path).replace('\\', '/').replace('.md', '').replace('/', '-')
                        all_docs.append(doc_data)
                        processed.add(md_file)
        
        # Xử lý các file .md còn lại trong thư mục hiện tại (không có trong _order.yaml)
        for md_file in sorted(current_dir.glob('*.md')):
            if md_file.name != '_order.yaml' and md_file not in processed:
                doc_data = parse_markdown_file(md_file, root_base_dir)
                if doc_data:
                    file_counter[section_key] += 1
                    doc_data['parent_slug'] = parent_slug
                    doc_data['order_index'] = file_counter[section_key]
                    doc_data['section'] = section_key
                    rel_path = md_file.relative_to(base_path)
                    doc_data['slug'] = str(rel_path).replace('\\', '/').replace('.md', '').replace('/', '-')
                    all_docs.append(doc_data)
                    processed.add(md_file)
    
    # Process từng thư mục TRƯỚC để đếm số documents
    # Process docs/ -> User Guide
    docs_dir = base_dir / 'docs'
    if docs_dir.exists() and docs_dir.is_dir():
        print(f"  📂 Đang đọc thư mục docs/...")
        process_directory_recursive(docs_dir, 'user-guide', 'user_guide', docs_dir, base_dir)
    
    # Process reference/ -> Developer Guide
    reference_dir = base_dir / 'reference'
    if reference_dir.exists() and reference_dir.is_dir():
        print(f"  📂 Đang đọc thư mục reference/...")
        process_directory_recursive(reference_dir, 'developer-guide', 'developer_guide', reference_dir, base_dir)
    
    # Process recipes/ -> Release Notes
    recipes_dir = base_dir / 'recipes'
    if recipes_dir.exists() and recipes_dir.is_dir():
        print(f"  📂 Đang đọc thư mục recipes/...")
        process_directory_recursive(recipes_dir, 'release-notes', 'release_notes', recipes_dir, base_dir)
    
    # CHỈ tạo parent khi có ít nhất 1 document trong section đó
    parent_order = 1
    
    # 1. Tạo parent "User Guide" nếu có documents
    if file_counter['user_guide'] > 0:
        user_guide_parent = {
            'title': 'User Guide',
            'html_content': '<p>Tài liệu hướng dẫn sử dụng cho người dùng</p>',
            'section': 'user_guide',
            'order_index': parent_order,
            'parent_slug': None,
            'slug': 'user-guide',
            'is_parent': True
        }
        all_docs.insert(0, user_guide_parent)  # Insert ở đầu để parent luôn đứng trước children
        parent_order += 1
        print(f"  ✓ Tạo parent 'User Guide' với {file_counter['user_guide']} documents")
    else:
        print(f"  ⚠️  Bỏ qua 'User Guide' vì không có documents")
    
    # 2. Tạo parent "Developer Guide" nếu có documents
    if file_counter['developer_guide'] > 0:
        dev_guide_parent = {
            'title': 'Developer Guide',
            'html_content': '<p>Tài liệu API và hướng dẫn cho developer</p>',
            'section': 'developer_guide',
            'order_index': parent_order,
            'parent_slug': None,
            'slug': 'developer-guide',
            'is_parent': True
        }
        # Tìm vị trí insert: sau User Guide (nếu có) hoặc đầu list
        insert_pos = 1 if file_counter['user_guide'] > 0 else 0
        all_docs.insert(insert_pos, dev_guide_parent)
        parent_order += 1
        print(f"  ✓ Tạo parent 'Developer Guide' với {file_counter['developer_guide']} documents")
    else:
        print(f"  ⚠️  Bỏ qua 'Developer Guide' vì không có documents")
    
    # 3. Tạo parent "Release Notes" nếu có documents
    if file_counter['release_notes'] > 0:
        release_notes_parent = {
            'title': 'Release Notes',
            'html_content': '<p>Ghi chú phiên bản và cập nhật</p>',
            'section': 'release_notes',
            'order_index': parent_order,
            'parent_slug': None,
            'slug': 'release-notes',
            'is_parent': True
        }
        # Tìm vị trí insert: sau các parent khác
        insert_pos = sum(1 for k in ['user_guide', 'developer_guide'] if file_counter[k] > 0)
        all_docs.insert(insert_pos, release_notes_parent)
        print(f"  ✓ Tạo parent 'Release Notes' với {file_counter['release_notes']} documents")
    else:
        print(f"  ⚠️  Bỏ qua 'Release Notes' vì không có documents")
    
    return all_docs


def replace_image_urls(models, uid, html: str, base_zip_dir: Path) -> str:
    """Thay thế ảnh:
    1) Ưu tiên ảnh cục bộ trong ZIP (../assets/... hoặc ../files/...), upload lên Odoo và thay src.
    2) Link ngoài https:// giữ nguyên.
    3) Wrap ảnh trong <figure> với CSS để ảnh hiển thị gọn: max-width:100%; height:auto; display:block; margin.
    """
    if not html:
        return ""

    pattern = r'<img\b[^>]*>'

    def add_attrs_to_img(tag_html: str) -> str:
        """Thêm width, height, loading vào img tag nếu chưa có"""
        attrs = tag_html
        if ' width=' not in attrs:
            attrs = attrs.replace('<img', '<img width="100%"', 1)
        if ' height=' not in attrs:
            attrs = attrs.replace('<img', '<img height="auto"', 1)
        if ' loading=' not in attrs:
            attrs = attrs.replace('<img', '<img loading="lazy"', 1)
        return attrs

    def wrap_img(m):
        img_tag = m.group(0)
        # Wrap trong figure (không cần check vì đã xử lý src trước)
        img_tag = add_attrs_to_img(img_tag)
        return f'<figure style="max-width:100%;margin:12px 0">{img_tag}</figure>'

    # Tìm và thay thế src cho ảnh local trước
    src_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
    
    def replacer_src(m):
        original_src = m.group(1)
        full_tag = m.group(0)

        # Cache
        if original_src in IMAGE_UPLOAD_CACHE:
            return full_tag.replace(original_src, IMAGE_UPLOAD_CACHE[original_src])

        # Local in ZIP
        if original_src.startswith(("../assets/", "../files/")):
            rel = original_src[3:]  # drop ../
            local_path = base_zip_dir / rel
            if local_path.exists():
                print(f"    ⬆️  Upload ảnh: {rel}")
                _, url = upload_attachment(models, uid, str(local_path), public=True)
                if url:
                    IMAGE_UPLOAD_CACHE[original_src] = url
                    return full_tag.replace(original_src, url)
            else:
                print(f"    ⚠️  Không thấy ảnh: {local_path}")

        # External link: keep và cache
        if original_src.startswith(("http://", "https://")):
            IMAGE_UPLOAD_CACHE[original_src] = original_src

        return full_tag

    # Thay thế src trước
    html = re.sub(src_pattern, replacer_src, html, flags=re.IGNORECASE)
    
    # Sau đó wrap tất cả img trong figure
    return re.sub(pattern, wrap_img, html, flags=re.IGNORECASE)


# ------------------- IMPORTER CHÍNH -------------------
def import_all():
    """Import tất cả docs từ ReadMe export vào Odoo"""
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)
    
    print("\n📚 Đang đọc cấu trúc từ ReadMe export...")
    base_dir = Path(README_EXPORT_DIR)
    if not base_dir.exists():
        raise SystemExit(f"❌ Không tìm thấy thư mục export: {README_EXPORT_DIR}")
    
    all_docs = build_doc_tree(base_dir)
    print(f"  ✓ Tìm thấy {len(all_docs)} tài liệu")
    
    # Sắp xếp: parent articles trước (theo order_index), sau đó là children (theo order_index)
    def sort_key(doc):
        is_parent = doc.get('is_parent', False)
        section = doc.get('section', 'unknown')
        order_idx = doc.get('order_index', 999999)
        # Parent articles có order_index 1, 2, 3 nên sẽ được sort trước
        # Children có order_index tăng dần trong từng section
        section_order = {'user_guide': 1, 'developer_guide': 2, 'release_notes': 3}.get(section, 999)
        return (section_order, order_idx)
    
    all_docs.sort(key=sort_key)
    
    # Gán sequence theo parent
    parent_to_next_seq: Dict[str, int] = {}
    for doc in all_docs:
        parent_key = doc.get('parent_slug') or '__root__'
        seq = parent_to_next_seq.get(parent_key, 1)
        doc['_id_seq'] = seq
        parent_to_next_seq[parent_key] = seq + 1
    
    print("\n" + "="*60)
    print("🚀 BẮT ĐẦU QUÁ TRÌNH IMPORT...")
    print("="*60 + "\n")
    
    article_ids: Dict[str, int] = {}
    total_files = 0
    success_count = 0
    
    for doc in all_docs:
        total_files += 1
        try:
            title = doc.get('title', 'Untitled')
            slug = doc.get('slug', f'doc_{total_files}')
            html_content = doc.get('html_content', '')
            # Mirror ảnh vào Odoo và thêm CSS hiển thị gọn
            html_content = replace_image_urls(models, uid, html_content, base_dir)
            id_seq = doc.get('_id_seq')
            
            print(f"\n[{total_files}] Đang xử lý: {title[:60]}")
            
            # Tạo hoặc cập nhật article
            vals = {
                "name": title,
                "body": html_content,
                "parent_id": space_id
            }
            if id_seq is not None:
                vals["sequence"] = id_seq
            
            # Tìm article đã tồn tại
            existing_article = odoo_search(
                models, uid, MODEL_ARTICLE,
                [("name", "=", title), ("parent_id", "=", space_id)],
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
    
    # Set parent relationships
    print("\n🔗 Đang thiết lập quan hệ cha-con...")
    fixed = 0
    for doc in all_docs:
        try:
            parent_slug = doc.get('parent_slug')
            if not parent_slug:
                continue
            child_id = article_ids.get(doc.get('slug'))
            parent_id = article_ids.get(parent_slug)
            if child_id and parent_id:
                odoo_write(models, uid, MODEL_ARTICLE, [child_id], {"parent_id": parent_id})
                fixed += 1
        except Exception as e:
            print(f"  ⚠️  Không thể set parent cho '{doc.get('slug')}': {e}")
    
    if fixed:
        print(f"  ✓ Đã set parent cho {fixed} bài viết")
    
    print("\n" + "="*60)
    print(f"✅✅✅ IMPORT HOÀN TẤT! ✅✅✅")
    print(f"   Tổng số file: {total_files}")
    print(f"   Thành công: {success_count}")
    print(f"   Thất bại: {total_files - success_count}")
    print(f"\n📋 Hãy kiểm tra kết quả trong Odoo, không gian: '{SPACE_NAME}'")
    print("="*60)


# ------------------- UPLOAD RELEASE NOTES FROM JSON -------------------
def load_release_notes_from_json(base_dir: Path) -> List[Dict[str, Any]]:
    """Load các Release Notes từ JSON files đã scrape"""
    release_notes_dir = base_dir / 'release_notes' / 'content_release_notes'
    if not release_notes_dir.exists():
        print(f"  ⚠️  Không tìm thấy thư mục: {release_notes_dir}")
        return []
    
    all_docs = []
    json_files = sorted(release_notes_dir.glob('*.json'))
    
    print(f"\n📂 Đang đọc Release Notes từ JSON files...")
    print(f"  📁 Thư mục: {release_notes_dir}")
    print(f"  📄 Tìm thấy {len(json_files)} file JSON")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                doc_data = json.load(f)
            
            # Bỏ qua file changelog.json nếu chỉ là listing page (không có nội dung chi tiết)
            if json_file.name == 'changelog.json' and not doc_data.get('html_content', '').strip():
                print(f"  ⏭️  Bỏ qua {json_file.name} (listing page)")
                continue
            
            # Đảm bảo có đầy đủ thông tin cần thiết
            if not doc_data.get('title'):
                doc_data['title'] = json_file.stem.replace('_', ' ').title()
            
            if not doc_data.get('slug'):
                doc_data['slug'] = json_file.stem
            
            # Set section và parent_slug
            doc_data['section'] = 'release_notes'
            doc_data['parent_slug'] = 'release-notes'  # Tất cả release notes đều dưới parent này
            
            all_docs.append(doc_data)
            
        except Exception as e:
            print(f"  ⚠️  Lỗi đọc {json_file.name}: {e}")
    
    # Sắp xếp theo order_index (nếu có), sau đó theo title
    all_docs.sort(key=lambda x: (
        x.get('order_index', 999999),
        x.get('title', '').lower()
    ))
    
    print(f"  ✓ Đã load {len(all_docs)} release notes")
    return all_docs


def replace_release_notes_images(models, uid, html: str, assets_dir: Path) -> str:
    """Thay thế đường dẫn ảnh trong release notes bằng URL Odoo"""
    if not assets_dir.exists():
        return html
    
    # Pattern để tìm các ảnh từ files.readme.io hoặc local assets
    # Tìm ảnh từ files.readme.io (external) - giữ nguyên
    # Tìm ảnh local trong ../assets_release_notes/
    asset_pattern = r'src=["\']([^"\']*\.(?:png|jpg|jpeg|gif|svg|webp))["\']'
    
    def replace_img(match):
        original_url = match.group(1)
        img_tag = match.group(0)
        
        # Nếu là external URL (files.readme.io), giữ nguyên nhưng cache
        if original_url.startswith(('http://', 'https://')):
            if original_url not in IMAGE_UPLOAD_CACHE:
                IMAGE_UPLOAD_CACHE[original_url] = original_url
            return img_tag
        
        # Nếu là local asset (../assets_release_notes/...)
        if '../assets_release_notes/' in original_url or original_url.startswith('assets_release_notes/'):
            # Lấy tên file
            filename = os.path.basename(original_url)
            local_path = assets_dir / filename
            
            if filename in IMAGE_UPLOAD_CACHE:
                new_url = IMAGE_UPLOAD_CACHE[filename]
                return img_tag.replace(original_url, new_url)
            
            if local_path.exists():
                print(f"    ⬆️  Upload ảnh: {filename}")
                _, url = upload_attachment(models, uid, str(local_path), public=True)
                if url:
                    IMAGE_UPLOAD_CACHE[filename] = url
                    return img_tag.replace(original_url, url)
            else:
                print(f"    ⚠️  Không tìm thấy ảnh: {local_path}")
        
        return img_tag
    
    html = re.sub(asset_pattern, replace_img, html, flags=re.IGNORECASE)
    return html


def import_release_notes():
    """Upload các Release Notes đã scrape từ JSON files lên Odoo"""
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)
    
    print("\n" + "="*60)
    print("📋 UPLOAD RELEASE NOTES TỪ JSON FILES")
    print("="*60)
    
    base_dir = Path(r"C:\Abivin\data_docs03")
    release_notes_dir = base_dir / 'release_notes' / 'content_release_notes'
    assets_dir = base_dir / 'release_notes' / 'assets_release_notes'
    
    if not release_notes_dir.exists():
        raise SystemExit(f"❌ Không tìm thấy thư mục: {release_notes_dir}")
    
    # Load các release notes từ JSON
    all_docs = load_release_notes_from_json(base_dir)
    
    if not all_docs:
        print("  ⚠️  Không có release notes nào để upload")
        return
    
    # Tìm hoặc tạo parent "Release Notes"
    print("\n📁 Kiểm tra parent 'Release Notes'...")
    release_notes_parent_id = None
    existing_parent = odoo_search(
        models, uid, MODEL_ARTICLE,
        [("name", "=", "Release Notes"), ("parent_id", "=", space_id)],
        ["id"], limit=1
    )
    
    if existing_parent:
        release_notes_parent_id = existing_parent[0]["id"]
        print(f"  ✓ Tìm thấy parent 'Release Notes' (ID: {release_notes_parent_id})")
    else:
        # Tạo parent mới
        release_notes_parent_id = odoo_create(models, uid, MODEL_ARTICLE, {
            "name": "Release Notes",
            "body": "<p>Ghi chú phiên bản và cập nhật</p>",
            "parent_id": space_id,
            "sequence": 1000  # Đặt ở cuối
        })
        print(f"  ✓ Tạo mới parent 'Release Notes' (ID: {release_notes_parent_id})")
    
    print("\n" + "="*60)
    print("🚀 BẮT ĐẦU UPLOAD RELEASE NOTES...")
    print("="*60 + "\n")
    
    article_ids: Dict[str, int] = {}
    total_files = 0
    success_count = 0
    
    # Gán sequence cho mỗi release note
    seq_counter = 1
    
    for doc in all_docs:
        total_files += 1
        try:
            title = doc.get('title', 'Untitled')
            slug = doc.get('slug', f'release_note_{total_files}')
            html_content = doc.get('html_content', '')
            
            # Xử lý ảnh
            if assets_dir.exists():
                html_content = replace_release_notes_images(models, uid, html_content, assets_dir)
            
            print(f"\n[{total_files}/{len(all_docs)}] Đang xử lý: {title[:60]}")
            
            # Tạo hoặc cập nhật article
            vals = {
                "name": title,
                "body": html_content,
                "parent_id": release_notes_parent_id,  # Tất cả đều dưới parent "Release Notes"
                "sequence": seq_counter
            }
            
            # Tìm article đã tồn tại
            existing_article = odoo_search(
                models, uid, MODEL_ARTICLE,
                [("name", "=", title), ("parent_id", "=", release_notes_parent_id)],
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
            
            seq_counter += 1
            success_count += 1
            
        except Exception as e:
            print(f"\n❌ LỖI khi xử lý '{slug}': {e}\n")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*60)
    print(f"✅✅✅ UPLOAD RELEASE NOTES HOÀN TẤT! ✅✅✅")
    print(f"   Tổng số file: {total_files}")
    print(f"   Thành công: {success_count}")
    print(f"   Thất bại: {total_files - success_count}")
    print(f"\n📋 Hãy kiểm tra kết quả trong Odoo, section: 'Release Notes'")
    print("="*60)


# -------------------- MAIN ---------------------------
if __name__ == "__main__":
    try:
        # Chọn function cần chạy:
        # - import_all() : Import từ ReadMe ZIP export
        # - import_release_notes() : Upload Release Notes từ JSON files đã scrape
        
        import_release_notes()  # Upload Release Notes từ JSON
        # import_all()  # Hoặc import từ ZIP export
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Người dùng hủy bỏ quá trình import!")
    except Exception as e:
        print(f"\n❌ LỖI NGHIÊM TRỌNG: {e}")
        import traceback
        traceback.print_exc()

