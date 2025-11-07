# =============================================================
# File: import_readme_zip_to_odoo.py (Odoo 19, final VI)
# Import ReadMe ZIP export -> Odoo Knowledge (mirror ảnh, fallback Space)
# ĐÃ SỬA LỖI: Xử lý HTML (<table>) và thẻ <Image> tùy chỉnh
# =============================================================

import os
import re
import yaml
import json
import base64
import markdown
import sys
import argparse
import xmlrpc.client
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

# Fix encoding cho Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ===================== CẤU HÌNH MẶC ĐỊNH =====================
# ⚠️ THAY THẾ ĐƯỜNG DẪN NÀY
README_EXPORT_DIR = r"C:\Abivin\data_docs03\abivin-v4.0-2025-11-03T16-58-05_8cddcbc" 
ODOO_BASE_URL = "https://test018.odoo.com"
ODOO_DB_NAME = "test018"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "3f623d85508792f81af911610db742d67a5d1845"
SPACE_NAME = "Tài liệu Abivin 05" # Tên Workspace mới Anh muốn

MODEL_ARTICLE = "knowledge.article"
MODEL_ATTACHMENT = "ir.attachment"

# Tự phát hiện Space
SPACE_FIELD = None
SPACE_MODEL_NAME = None
# =============================================================

# Cache upload ảnh để tránh trùng
IMAGE_UPLOAD_CACHE: Dict[str, str] = {}

# ---------------- XML-RPC CORE ----------------------
def odoo_login() -> Tuple[xmlrpc.client.ServerProxy, int]:
    print("\n🔐 Kết nối Odoo...")
    common = xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/common")
    try:
        version_info = common.version()
        print(f"  ✓ Server version: {version_info.get('server_version', 'Unknown')}")
    except Exception as e:
        print(f"  ✗ Lỗi kiểm tra phiên bản: {e}")

    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if not uid:
        raise SystemExit("❌ Xác thực Odoo thất bại. Kiểm tra API key/quyền.")
    print(f"  ✓ Đăng nhập ID: {uid}")
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
            import time; time.sleep(2)
    raise RuntimeError(f"❌ RPC {model}.{method} failed x3.")


def odoo_search(models, uid, model, domain, fields=None, limit=0):
    kwargs = {}
    if fields: kwargs["fields"] = fields
    if limit: kwargs["limit"] = limit
    return odoo_call(models, uid, model, "search_read", domain, **kwargs)


def odoo_create(models, uid, model, vals):
    if not isinstance(vals, dict):
        raise TypeError("create() expects dict")
    return odoo_call(models, uid, model, "create", vals)


def odoo_write(models, uid, model, ids, vals):
    if not isinstance(ids, list):
        ids = [ids]
    if not isinstance(vals, dict):
        raise TypeError("write() expects dict")
    return odoo_call(models, uid, model, "write", ids, vals)

# ---------------- ATTACHMENT UTILS -------------------
def guess_mimetype(name: str) -> str:
    ext = os.path.splitext(name.lower())[1]
    return {
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".gif": "image/gif", ".svg": "image/svg+xml", ".webp": "image/webp",
        ".avif": "image/avif"
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
        att = odoo_search(models, uid, MODEL_ATTACHMENT, [("id","=",att_id)], ["checksum","name"], limit=1)
        qs = f"?unique={att[0]['checksum']}" if att and att[0].get("checksum") else ""
        url = f"/web/image/{att_id}/{att[0].get('name')}{qs}"
        return att_id, url
    except Exception as e:
        print(f"  ✗ Lỗi upload ảnh '{path}': {e}")
        return None, None

# ---------------- SPACE/FALLBACK ---------------------
def detect_space_field(models, uid):
    """Phát hiện article có field 'space-like' không."""
    global SPACE_FIELD, SPACE_MODEL_NAME
    if SPACE_FIELD is not None:
        return SPACE_FIELD, SPACE_MODEL_NAME

    fields = odoo_call(models, uid, MODEL_ARTICLE, "fields_get", [], {"attributes": ["string", "type", "relation"]})
    candidates = ["space_id", "collection_id", "workspace_id"]
    for f in candidates:
        if f in fields and fields[f].get("type") == "many2one":
            SPACE_FIELD = f
            SPACE_MODEL_NAME = fields[f].get("relation")
            print(f"  ✓ Phát hiện field Space: {SPACE_FIELD} -> {SPACE_MODEL_NAME}")
            return SPACE_FIELD, SPACE_MODEL_NAME

    SPACE_FIELD, SPACE_MODEL_NAME = None, None
    print("  • Không có field Space trên knowledge.article. Sẽ dùng 1 bài gốc làm 'Space giả'.")
    return None, None


def ensure_space(models, uid, space_name: str) -> int:
    """Nếu có Space thật -> trả về id Space. Nếu không -> trả về id Article gốc (root) làm 'Space giả'."""
    space_field, space_model = detect_space_field(models, uid)

    if space_field and space_model:
        rec = odoo_search(models, uid, space_model, [("name","=",space_name)], ["id"], limit=1)
        if rec:
            print(f"  ✓ Dùng {space_model} '{space_name}' (ID {rec[0]['id']})")
            return rec[0]["id"]
        sid = odoo_create(models, uid, space_model, {"name": space_name})
        print(f"  ✓ Tạo {space_model} '{space_name}' (ID {sid})")
        return sid

    # Fallback: tạo article gốc
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name","=",space_name), ("parent_id","=",False)], ["id"], limit=1)
    if rec:
        print(f"  ✓ Dùng bài gốc làm 'Space': '{space_name}' (ID {rec[0]['id']})")
        return rec[0]["id"]
    aid = odoo_create(models, uid, MODEL_ARTICLE, {
        "name": space_name,
        "body": "<p>Root node cho tài liệu import</p>",
        "parent_id": False,
    })
    print(f"  ✓ Tạo bài gốc làm 'Space': '{space_name}' (ID {aid})")
    return aid

# ---------------- PARSE MARKDOWN/OPENAPI (ĐÃ SỬA) -------------
def read_order_yaml(order_path: Path) -> List[str]:
    if not order_path.exists(): return []
    try:
        with open(order_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or []
        items = []
        for x in data:
            s = str(x).strip()
            if s.endswith('.md'): s = s[:-3]
            items.append(s)
        return items
    except Exception as e:
        print(f"  ⚠️  Lỗi đọc {order_path}: {e}")
        return []


def operation_id_to_path_method(operation_id: str) -> Tuple[Optional[str], Optional[str]]:
    if not operation_id: return None, None
    parts = operation_id.split('_', 1)
    if len(parts) != 2: return None, None
    method = parts[0].lower()
    path_part = parts[1].replace('-', '/')
    path = f"/{path_part}"
    return path, method


def parse_openapi_endpoint(openapi_spec: dict, operation_id: str, title: str = None) -> str:
    """
    Chuyển đổi OpenAPI endpoint (Swagger) thành HTML tĩnh.
    Đây là lý do "format xấu" (mất tương tác) nhưng dữ liệu vẫn đủ.
    """
    html_parts, found_endpoint, found_path, found_method = [], None, None, None
    if operation_id:
        for path, methods in openapi_spec.get("paths", {}).items():
            for method, details in methods.items():
                if method.lower() in ["get","post","put","patch","delete","head","options"]:
                    if details.get("operationId") == operation_id:
                        found_endpoint, found_path, found_method = details, path, method; break
            if found_endpoint: break
    if not found_endpoint and operation_id:
        path_pattern, method_pattern = operation_id_to_path_method(operation_id)
        if path_pattern and method_pattern:
            for path, methods in openapi_spec.get("paths", {}).items():
                if path_pattern in path or path == path_pattern:
                    if method_pattern in methods:
                        found_endpoint, found_path, found_method = methods[method_pattern], path, method_pattern; break
    if not found_endpoint and title:
        title_path = title.strip()
        if title_path.startswith('/'):
            for path, methods in openapi_spec.get("paths", {}).items():
                if path == title_path or title_path in path:
                    for method in ['post','get','put','patch','delete']:
                        if method in methods:
                            found_endpoint, found_path, found_method = methods[method], path, method; break
                    if found_endpoint: break
    if found_endpoint:
        summary = found_endpoint.get("summary", found_path or title or "API Endpoint")
        description = found_endpoint.get("description", "")
        html_parts.append(f"<h2>{summary}</h2>")
        if description:
            md = markdown.Markdown(extensions=['fenced_code','tables','nl2br'])
            html_parts.append(md.convert(description))
        if found_method: html_parts.append(f"<p><strong>Method:</strong> <code>{found_method.upper()}</code></p>")
        if found_path: html_parts.append(f"<p><strong>Path:</strong> <code>{found_path}</code></p>")
        params = found_endpoint.get("parameters", [])
        if params:
            html_parts.append("<h3>Parameters</h3><ul>")
            for p in params:
                nm = p.get("name",""); pin = p.get("in",""); desc = p.get("description",""); req = p.get("required",False)
                html_parts.append(f"<li><code>{nm}</code> ({pin}){' <strong>[Required]</strong>' if req else ''}{(': '+desc) if desc else ''}</li>")
            html_parts.append("</ul>")
        request_body = found_endpoint.get("requestBody", {})
        if request_body:
            html_parts.append("<h3>Request Body</h3>")
            req_desc = request_body.get("description","")
            if req_desc:
                md = markdown.Markdown(extensions=['fenced_code','tables','nl2br'])
                html_parts.append(md.convert(req_desc))
        responses = found_endpoint.get("responses",{})
        if responses:
            html_parts.append("<h3>Responses</h3>")
            for status, resp in responses.items():
                html_parts.append(f"<h4>HTTP {status}</h4>")
                resp_desc = resp.get("description","")
                if resp_desc:
                    md = markdown.Markdown(extensions=['fenced_code','tables','nl2br'])
                    html_parts.append(md.convert(resp_desc))
        return "".join(html_parts)
    return "<p>API endpoint documentation not found in OpenAPI spec.</p>"


def parse_markdown_file(md_path: Path, base_dir: Path = None) -> Optional[Dict[str, Any]]:
    """
    SỬA LỖI: Hàm này đã được sửa để xử lý cả HTML (<table>) và Markdown
    """
    if not md_path.exists(): return None
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        front_matter, body = {}, content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    front_matter = yaml.safe_load(parts[1]) or {}
                    body = parts[2].strip()
                except:
                    body = content
        title = front_matter.get('title') or md_path.stem.replace('-', ' ').title()

        # Xử lý API Reference (Developer Guide)
        if not body and base_dir and front_matter.get('api'):
            api_file = front_matter['api'].get('file')
            operation_id = front_matter['api'].get('operationId')
            if api_file and operation_id:
                for candidate in [base_dir/'reference'/api_file, md_path.parent/api_file, base_dir/api_file]:
                    if candidate.exists():
                        try:
                            with open(candidate, 'r', encoding='utf-8-sig') as f:
                                spec = json.load(f)
                            html = parse_openapi_endpoint(spec, operation_id, title)
                            if html and html != "<p>API endpoint documentation not found in OpenAPI spec.</p>":
                                return {'title': title, 'html_content': html, 'front_matter': front_matter, 'slug': md_path.stem}
                        except Exception as e:
                            print(f"    ⚠️  Lỗi parse OpenAPI {api_file}: {e}")

        if body:
            # === PHẦN SỬA LỖI QUAN TRỌNG (FIX LỖI MẤT XUỐNG DÒNG) ===
            
            # 1. Chuyển đổi thẻ <Image> tùy chỉnh sang <img> HTML chuẩn
            def replace_custom_image(match):
                attrs_str = match.group(1)
                caption = match.group(2).strip()
                
                src = re.search(r'src="([^"]+)"', attrs_str, re.IGNORECASE)
                alt = re.search(r'alt=\{?([^"}\s]+)\}?', attrs_str, re.IGNORECASE)
                title_attr = re.search(r'title="([^"]+)"', attrs_str, re.IGNORECASE)

                src_val = src.group(1) if src else ""
                alt_val = alt.group(1) if alt else caption
                title_val = title_attr.group(1) if title_attr else ""

                # Chuyển thành HTML <img> chuẩn
                img_tag = f'<img src="{src_val}" alt="{alt_val}" title="{title_val}">'
                if caption:
                    return f'<figure>{img_tag}<figcaption>{caption}</figcaption></figure>'
                else:
                    return f'<figure>{img_tag}</figure>'
            
            # Áp dụng Regex để sửa thẻ <Image ...>
            body = re.sub(r'<Image([^>]+)>(.*?)</Image>', replace_custom_image, body, flags=re.DOTALL | re.IGNORECASE)

            # 2. Kiểm tra xem nội dung CÓ PHẢI LÀ HTML không
            # Nếu nó chứa các thẻ HTML phức tạp (như <table>), giữ nguyên
            if re.search(r'<(table|div|figure|blockquote|img)\b', body, re.IGNORECASE):
                html = body # Giữ nguyên HTML (FIX LỖI MẤT BẢNG)
            else:
                # Nếu là Markdown thuần (không có HTML phức tạp), convert
                md = markdown.Markdown(extensions=['fenced_code','tables','nl2br'])
                html = md.convert(body)
            # === KẾT THÚC PHẦN SỬA LỖI ===
        else:
            html = f"<p>Nội dung cho <strong>{title}</strong></p>"

        return {'title': title, 'html_content': html, 'front_matter': front_matter, 'slug': md_path.stem}
    except Exception as e:
        print(f"  ⚠️  Lỗi parse {md_path}: {e}")
        return None

# ---------------- DỰNG CÂY DOC ----------------------
def build_doc_tree(base_dir: Path) -> List[Dict[str, Any]]:
    all_docs = []
    file_counter = {'user_guide':0, 'developer_guide':0, 'release_notes':0}

    def process_directory_recursive(current_dir: Path, parent_slug: str, section_key: str, base_path: Path, root_base_dir: Path):
        order_items = read_order_yaml(current_dir / '_order.yaml')
        processed = set()
        for item in order_items:
            item_path = current_dir / item
            
            # --- LOGIC MỚI: Ưu tiên xử lý thư mục con trước ---
            if item_path.is_dir():
                # Tạo slug cho thư mục con (ví dụ: 'web-app-tutorials')
                dir_slug = str(item_path.relative_to(base_path)).replace('\\','/').replace('/','-')
                
                # Tìm index.md (trang chính của thư mục)
                index_md = item_path / 'index.md'
                
                # Mặc định, parent_slug mới là slug của thư mục này
                new_parent_slug = dir_slug

                if index_md.exists() and index_md not in processed:
                    doc_data = parse_markdown_file(index_md, root_base_dir)
                    if doc_data:
                        file_counter[section_key]+=1
                        doc_data.update({
                            'parent_slug': parent_slug, # Gán nó vào cha hiện tại
                            'order_index': file_counter[section_key],
                            'section': section_key,
                            'slug': dir_slug # Slug của nó là tên thư mục
                        })
                        all_docs.append(doc_data); processed.add(index_md)
                else:
                    # Nếu không có index.md, tạo một bài viết giả (placeholder)
                    file_counter[section_key]+=1
                    doc_data = {
                        'title': item_path.name.replace('-',' ').title(),
                        'html_content': f'<p>Tổng quan về {item_path.name}</p>',
                        'front_matter': {},
                        'parent_slug': parent_slug,
                        'order_index': file_counter[section_key],
                        'section': section_key,
                        'slug': dir_slug,
                        'is_placeholder_parent': True # Đánh dấu đây là mục cha
                    }
                    all_docs.append(doc_data)

                # Đệ quy vào thư mục con, SỬ DỤNG SLUG MỚI LÀM CHA
                process_directory_recursive(item_path, new_parent_slug, section_key, base_path, root_base_dir)

            # --- Xử lý file .md ---
            elif (current_dir / f"{item}.md").exists():
                md_file = current_dir / f"{item}.md"
                if md_file not in processed:
                    doc_data = parse_markdown_file(md_file, root_base_dir)
                    if doc_data:
                        file_counter[section_key]+=1
                        doc_data.update({
                            'parent_slug': parent_slug, # Gán vào cha hiện tại
                            'order_index': file_counter[section_key],
                            'section': section_key,
                            'slug': str(md_file.relative_to(base_path)).replace('\\','/').replace('.md','').replace('/','-')
                        })
                        all_docs.append(doc_data); processed.add(md_file)
        
        # Xử lý các file .md còn sót lại (không có trong _order.yaml)
        for md_file in sorted(current_dir.glob('*.md')):
            if md_file.name!='_order.yaml' and md_file not in processed:
                doc_data = parse_markdown_file(md_file, root_base_dir)
                if doc_data:
                    file_counter[section_key]+=1
                    doc_data.update({
                        'parent_slug': parent_slug,
                        'order_index': file_counter[section_key] + 999, # Đẩy xuống cuối
                        'section': section_key,
                        'slug': str(md_file.relative_to(base_path)).replace('\\','/').replace('.md','').replace('/','-')
                    })
                    all_docs.append(doc_data); processed.add(md_file)

    # --- Bắt đầu xử lý 3 thư mục gốc ---
    docs_dir = base_dir / 'docs'
    if docs_dir.exists(): 
        print("  📂 Đọc docs/ (User Guide)...")
        process_directory_recursive(docs_dir, 'user-guide', 'user_guide', docs_dir, base_dir)
    
    reference_dir = base_dir / 'reference'
    if reference_dir.exists(): 
        print("  📂 Đọc reference/ (Developer Guide)...")
        process_directory_recursive(reference_dir, 'developer-guide', 'developer_guide', reference_dir, base_dir)
        
    recipes_dir = base_dir / 'recipes'
    if recipes_dir.exists(): 
        print("  📂 Đọc recipes/ (Release Notes)...")
        process_directory_recursive(recipes_dir, 'release-notes', 'release_notes', recipes_dir, base_dir)

    # --- Tạo 3 mục cha cấp cao nhất ---
    parent_order = 1
    if file_counter['user_guide']>0:
        all_docs.insert(0, {'title':'User Guide','html_content':'<p>Tài liệu hướng dẫn sử dụng</p>','section':'user_guide','order_index':parent_order,'parent_slug':None,'slug':'user-guide','is_parent':True}); parent_order+=1
    if file_counter['developer_guide']>0:
        insert_pos = 1 if file_counter['user_guide']>0 else 0
        all_docs.insert(insert_pos, {'title':'Developer Guide','html_content':'<p>Tài liệu API & Dev</p>','section':'developer_guide','order_index':parent_order,'parent_slug':None,'slug':'developer-guide','is_parent':True}); parent_order+=1
    if file_counter['release_notes']>0:
        insert_pos = (1 if file_counter['user_guide']>0 else 0) + (1 if file_counter['developer_guide']>0 else 0)
        all_docs.insert(insert_pos, {'title':'Release Notes','html_content':'<p>Ghi chú phiên bản</p>','section':'release_notes','order_index':parent_order,'parent_slug':None,'slug':'release-notes','is_parent':True})
    
    return all_docs

# ---------------- XỬ LÝ ẢNH -------------------------
def replace_image_urls(models, uid, html: str, base_zip_dir: Path) -> str:
    """
    SỬA LỖI: Hàm này đã được sửa để xử lý cả link ảnh HTTP (readme.io) 
    và link ảnh cục bộ (assets/)
    """
    if not html: return ""

    IMG_TAG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
    SRC_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
    SRCSET_RE = re.compile(r'(srcset)=["\']([^"\']+)["\']', re.IGNORECASE)
    SOURCE_SRCSET_RE = re.compile(r'(<source[^>]+srcset=["\'])([^"\']+)(["\'])', re.IGNORECASE)
    URL_IN_STYLE_RE = re.compile(r'url\((["\']?)([^)\'"]+)\1\)', re.IGNORECASE)

    # Regex mới để tìm các link ảnh bên ngoài (README CDN)
    README_CDN_RE = re.compile(r'https?://files\.readme\.io/[^"\')]+')

    def add_attrs(tag_html: str) -> str:
        """SỬA LỖI: Sử dụng logic fix ảnh (responsive) từ file fix_images_in_space.py"""
        # Nếu đã xử lý trước đó thì giữ nguyên
        if re.search(r'\bdata-abivin-img="1"\b', tag_html, flags=re.IGNORECASE):
            return tag_html

        # Xoá width/height/style cũ
        tag_html = re.sub(r'\swidth="[^"]*"', '', tag_html, flags=re.IGNORECASE)
        tag_html = re.sub(r"\swidth='[^']*'", '', tag_html, flags=re.IGNORECASE)
        tag_html = re.sub(r'\sheight="[^"]*"', '', tag_html, flags=re.IGNORECASE)
        tag_html = re.sub(r"\sheight='[^']*'", '', tag_html, flags=re.IGNORECASE)
        tag_html = re.sub(
            r'style="[^"]*"',
            lambda m: re.sub(r'(?:^|\s)(?:max-)?(?:width|height)\s*:[^;]*;?', '', m.group(0), flags=re.IGNORECASE),
            tag_html
        )
        
        # SỬA LỖI: Thêm margin:auto để căn giữa ảnh nhỏ, bỏ width:100%
        style_attrs = (
            'style="max-width:100%!important;height:auto!important;display:block!important;'
            'object-fit:contain!important;margin-left:auto!important;margin-right:auto!important;"'
        )
        
        if ' style=' not in tag_html:
            tag_html = tag_html.replace('<img', f'<img {style_attrs}', 1)
        else:
            tag_html = re.sub(r'style="[^"]*"', style_attrs, tag_html)

        if ' loading=' not in tag_html:
            tag_html = tag_html.replace('<img', '<img loading="lazy"', 1)
        
        tag_html = tag_html.replace('<img', '<img data-abivin-img="1" data-abivin-zoom="1"', 1)
        return tag_html

    def wrap_img(m):
        """SỬA LỖI: Bọc <img> trong <figure> với max-width 960px"""
        img_tag = m.group(0)
        # Tránh bọc lặp nếu đã ở trong figure
        # (Logic kiểm tra context đơn giản, có thể không hoàn hảo)
        start_ctx = max(0, m.start() - 100)
        end_ctx = min(len(html), m.end() + 100)
        before = html[start_ctx:m.start()]
        after  = html[m.end():end_ctx]
        if re.search(r'<figure\b[^>]*>[^<]*$', before, flags=re.IGNORECASE) \
           or re.search(r'^[^>]*</figure>', after, flags=re.IGNORECASE):
            return add_attrs(img_tag) # Chỉ thêm attrs, không bọc
            
        return (
            f'<figure style="max-width:960px;margin:12px auto;display:block;text-align:center;">'
            f'{add_attrs(img_tag)}'
            f'</figure>'
        )

    def _upload_local(local_rel: str) -> Optional[str]:
        """Tải ảnh từ đường dẫn CỤC BỘ trong file ZIP"""
        local_rel_norm = re.sub(r'^(\.\./|\./|/)', '', local_rel)
        
        # File ảnh có thể nằm trong thư mục 'assets' hoặc 'files'
        candidates = [
            (base_zip_dir / local_rel_norm).resolve(),
            (base_zip_dir / 'assets' / local_rel_norm).resolve(),
            (base_zip_dir / 'files' / local_rel_norm).resolve()
        ]
        
        local_path = None
        for path in candidates:
            if path.exists():
                local_path = path
                break
        
        if local_path:
            key = str(local_path)
            if key in IMAGE_UPLOAD_CACHE:
                return IMAGE_UPLOAD_CACHE[key]
            print(f"    ⬆️  Upload ảnh CỤC BỘ: {local_rel_norm}")
            _, new_url = upload_attachment(models, uid, str(local_path), public=True)
            if new_url:
                IMAGE_UPLOAD_CACHE[key] = new_url
                return new_url
        else:
            print(f"    ⚠️  Không thấy ảnh CỤC BỘ: {local_rel_norm} (Đã thử {len(candidates)} vị trí)")
        return None

    def _upload_remote(remote_url: str) -> Optional[str]:
        """Tải ảnh từ đường dẫn BÊN NGOÀI (Readme CDN)"""
        key = remote_url
        if key in IMAGE_UPLOAD_CACHE:
            return IMAGE_UPLOAD_CACHE[key]
        
        try:
            print(f"    ⬆️  Upload ảnh BÊN NGOÀI: {remote_url.split('/')[-1]}...")
            r = requests.get(remote_url, timeout=20)
            r.raise_for_status()
            content = r.content
            
            att_id = odoo_create(models, uid, MODEL_ATTACHMENT, {
                "name": os.path.basename(urlparse(remote_url).path) or "image",
                "datas": base64.b64encode(content).decode(),
                "mimetype": guess_mimetype(remote_url),
                "public": True
            })
            att = odoo_search(models, uid, MODEL_ATTACHMENT, [("id","=",att_id)], ["checksum","name"], limit=1)
            qs = f"?unique={att[0]['checksum']}" if att and att[0].get("checksum") else ""
            new_url = f"/web/image/{att_id}/{att[0].get('name')}{qs}"
            
            IMAGE_UPLOAD_CACHE[key] = new_url
            return new_url
        except Exception as e:
            print(f"    ⚠️  Lỗi tải ảnh BÊN NGOÀI: {remote_url} -> {e}")
            return None # Trả về None nếu lỗi, giữ link gốc

    def replacer_src(m):
        """Xử lý thẻ <img>"""
        original_src, full_tag = m.group(1), m.group(0)
        
        # Nếu đã là Odoo URL, bỏ qua
        if original_src.startswith(('/web/image', '/web/content')):
            return full_tag

        # Nếu là link ngoài (Readme CDN)
        if original_src.startswith(("http://","https://")):
            new_url = _upload_remote(original_src)
            if new_url:
                return full_tag.replace(original_src, new_url)
        
        # Nếu là link cục bộ (assets/ files/)
        if re.match(r'(\.\./|\./|/)?(assets|files)[/\\]', original_src, re.IGNORECASE):
            new_url = _upload_local(original_src)
            if new_url:
                return full_tag.replace(original_src, new_url)

        return full_tag # Giữ nguyên nếu không xử lý được

    def replacer_srcset_match(attr, srcset_val):
        """Xử lý srcset"""
        parts = [p.strip() for p in srcset_val.split(',')]
        new_parts = []
        for p in parts:
            if not p: continue
            url_part = p.split()[0]
            rest = p[len(url_part):]
            
            new_url = url_part
            if url_part.startswith(("http://","https://")):
                new_url = _upload_remote(url_part) or url_part
            elif re.match(r'(\.\./|\./|/)?(assets|files)[/\\]', url_part, re.IGNORECASE):
                new_url = _upload_local(url_part) or url_part
                
            new_parts.append(f"{new_url}{rest}")
        return f'{attr}="' + ", ".join(new_parts) + '"'

    # --- Bắt đầu quá trình sửa HTML ---
    
    # 1. Thay thế <img> src (Cả link ngoài và link cục bộ)
    html = re.sub(SRC_RE, replacer_src, html)
    
    # 2. Bọc <img> trong <figure> và fix CSS (responsive, căn giữa)
    html = re.sub(IMG_TAG_RE, wrap_img, html)
    
    # 3. Thay thế srcset (Cả link ngoài và link cục bộ)
    html = SRCSET_RE.sub(lambda m: replacer_srcset_match(m.group(1), m.group(2)), html)
    html = SOURCE_SRCSET_RE.sub(lambda m: m.group(1) + replacer_srcset_match('srcset', m.group(2)).split('=',1)[1].strip('"\'') + m.group(3), html)

    # 4. Thay thế background-image: url(...)
    def css_url_replacer(m):
        quote, u = m.group(1), m.group(2)
        new_u = u
        if u.startswith(("http://","https://")):
            new_u = _upload_remote(u) or u
        elif re.match(r'(\.\./|\./|/)?(assets|files)[/\\]', u, re.IGNORECASE):
            new_u = _upload_local(u) or u
        return f"url({quote}{new_u}{quote})"
    html = URL_IN_STYLE_RE.sub(css_url_replacer, html)

    return html

# ---------------- IMPORT CHÍNH -----------------------
def import_all():
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)

    print("\n📚 Đọc ReadMe export...")
    base_dir = Path(README_EXPORT_DIR)
    if not base_dir.exists():
        raise SystemExit(f"❌ Không thấy thư mục export: {README_EXPORT_DIR}")

    all_docs = build_doc_tree(base_dir)
    print(f"  ✓ Tìm thấy {len(all_docs)} tài liệu")

    # Sắp xếp theo thứ tự (section, parent, order_index)
    def sort_key(doc):
        is_parent = doc.get('is_parent', False)
        section = doc.get('section','unknown')
        order_idx = doc.get('order_index', 999999)
        section_order = {'user_guide':1,'developer_guide':2,'release_notes':3}.get(section, 999)
        return (section_order, 0 if is_parent else 1, order_idx)

    all_docs.sort(key=sort_key)

    # Gán sequence (thứ tự hiển thị)
    parent_to_next_seq: Dict[str,int] = {}
    for doc in all_docs:
        if doc.get('is_parent') or not doc.get('parent_slug'):
            seq = parent_to_next_seq.get('__root__', 1)
            doc['_id_seq'] = seq; parent_to_next_seq['__root__'] = seq+1
    for doc in all_docs:
        if not doc.get('is_parent') and doc.get('parent_slug'):
            pk = doc.get('parent_slug'); seq = parent_to_next_seq.get(pk, 1)
            doc['_id_seq'] = seq; parent_to_next_seq[pk] = seq+1

    print("\n" + "="*60)
    print("🚀 BẮT ĐẦU IMPORT...")
    print("="*60 + "\n")

    article_ids: Dict[str,int] = {}
    total_files = 0; success_count = 0

    # ----- VÒNG 1: TẠO TẤT CẢ BÀI VIẾT (chưa gán cha) -----
    print("--- Giai đoạn 1: Tạo/Cập nhật bài viết (Chưa gán cha) ---")
    for doc in all_docs:
        total_files += 1
        try:
            title = doc.get('title','Untitled')
            slug = doc.get('slug', f'doc_{total_files}')
            
            # Xử lý HTML VÀ UPLOAD ẢNH
            html_content = replace_image_urls(models, uid, doc.get('html_content',''), base_dir)
            
            id_seq = doc.get('_id_seq')

            if total_files % 10 == 0 or doc.get('is_parent'):
                print(f"\n[{total_files}/{len(all_docs)}] {title[:60]}")

            # Domain tìm bài cũ (idempotent)
            domain = [("name","=",title)]
            if SPACE_FIELD:
                domain.append((SPACE_FIELD,"=",space_id))
            else:
                # Tìm trong bài gốc
                domain.append(("parent_id","=",space_id))
            
            # --- SỬA LỖI: Tách biệt logic tìm kiếm và logic gán parent_id ---
            # Vals ban đầu (luôn là cấp cao nhất hoặc thuộc Space)
            vals = {
                "name": title, 
                "body": html_content,
                "sequence": id_seq or 99
            }
            if SPACE_FIELD:
                vals[SPACE_FIELD] = space_id
            else:
                vals["parent_id"] = space_id # Gán tạm vào Space giả

            existing = odoo_search(models, uid, MODEL_ARTICLE, domain, ["id"], limit=1)
            
            if existing:
                rid = existing[0]["id"]
                odoo_write(models, uid, MODEL_ARTICLE, [rid], vals)
                article_ids[slug] = rid
                print(f"  ✓ Cập nhật (ID: {rid})")
            else:
                aid = odoo_create(models, uid, MODEL_ARTICLE, vals)
                article_ids[slug] = aid
                print(f"  ✓ Tạo mới (ID: {aid})")

            success_count += 1
        except Exception as e:
            print(f"\n❌ Lỗi '{doc.get('slug')}': {e}\n")

    # ----- VÒNG 2: THIẾT LẬP QUAN HỆ CHA-CON -----
    print("\n--- Giai đoạn 2: Thiết lập quan hệ cha–con ---")
    fixed = 0
    for doc in all_docs:
        parent_slug = doc.get('parent_slug')
        if not parent_slug: continue
        
        child_id = article_ids.get(doc.get('slug'))
        parent_id = article_ids.get(parent_slug)
        
        if child_id and parent_id:
            try:
                odoo_write(models, uid, MODEL_ARTICLE, [child_id], {"parent_id": parent_id})
                fixed += 1
            except Exception as e:
                print(f"  ❌ Lỗi set parent cho {child_id}: {e}")
                
    if fixed: print(f"  ✓ Đã set parent cho {fixed} bài")

    # ----- VÒNG 3: GOM BÀI GỐC (NẾU DÙNG SPACE GIẢ) -----
    if not SPACE_FIELD:
        print("\n--- Giai đoạn 3: Gom bài top-level vào dưới bài gốc (Space giả) ---")
        gom = 0
        for doc in all_docs:
            if doc.get('is_parent') or not doc.get('parent_slug'): # Là bài cấp cao nhất
                aid = article_ids.get(doc.get('slug'))
                if aid and aid != space_id: # Đảm bảo không tự gán chính nó
                    odoo_write(models, uid, MODEL_ARTICLE, [aid], {"parent_id": space_id})
                    gom += 1
        if gom: print(f"  ✓ Đã gom {gom} mục cha vào Space giả")

    print("\n" + "="*60)
    print(f"✅ HOÀN TẤT")
    print(f"   Tổng: {total_files} | Thành công: {success_count} | Thất bại: {total_files - success_count}")
    print(f"   Không gian: '{SPACE_NAME}' (ID {space_id}) {'(Space thật)' if SPACE_FIELD else '(bài gốc)'}")
    print("="*60)

# -------------------- MAIN ---------------------------
if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Import ReadMe export vào Odoo Knowledge (mirror ảnh).")
        parser.add_argument("--space", help="Tên Space mới (vd: 'Tài liệu Abivin 04')")
        parser.add_argument("--src", help="Đường dẫn thư mục ReadMe export")
        parser.add_argument("--url", help="Odoo base URL (vd: https://your.odoo.com)")
        parser.add_argument("--db", help="Tên database Odoo")
        parser.add_argument("--user", help="User đăng nhập Odoo")
        parser.add_argument("--apikey", help="API key Odoo")

        args = parser.parse_args()
        if args.space: SPACE_NAME = args.space
        if args.src: README_EXPORT_DIR = args.src
        if args.url: ODOO_BASE_URL = args.url.rstrip("/")
        if args.db: ODOO_DB_NAME = args.db
        if args.user: ODOO_USER = args.user
        if args.apikey: ODOO_API_KEY = args.apikey

        import_all()
    except KeyboardInterrupt:
        print("\n⚠️ Hủy bởi người dùng")
    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback; traceback.print_exc()