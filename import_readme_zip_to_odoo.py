# =============================================================
# File: import_readme_zip_to_odoo.py (Odoo 19, ready-to-run)
# Import ReadMe ZIP export -> Odoo Knowledge (mirror images)
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
SPACE_NAME = "Tài liệu Abivin 01"
MODEL_ARTICLE = "knowledge.article"
MODEL_ATTACHMENT = "ir.attachment"
MODEL_SPACE = None  # auto-detect for Odoo 19
# ====================================================

IMAGE_UPLOAD_CACHE: Dict[str, str] = {}

# ---------------- ATTACHMENT UTILS -------------------
def guess_mimetype(name: str) -> str:
    ext = os.path.splitext(name.lower())[1]
    return {
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".gif": "image/gif", ".svg": "image/svg+xml", ".webp": "image/webp",
        ".avif": "image/avif"
    }.get(ext, "application/octet-stream")


# ---------------- XML-RPC CORE ----------------------
def odoo_login() -> Tuple[xmlrpc.client.ServerProxy, int]:
    print("\n🔐 Kết nối Odoo...")
    common = xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/common")
    try:
        version_info = common.version()
        print(f"  ✓ Server version: {version_info.get('server_version', 'Unknown')}")
    except Exception as e:
        print(f"  ✗ Lỗi check version: {e}")

    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if not uid:
        raise SystemExit("❌ Auth Odoo fail. Kiểm tra API key/quyền.")
    print(f"  ✓ Đăng nhập ID: {uid}")
    return xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/object"), uid


def odoo_call(models, uid, model, method, *args, **kwargs):
    args = list(args) if args else []
    kwargs = kwargs or {}
    for attempt in range(3):
        try:
            return models.execute_kw(ODOO_DB_NAME, uid, ODOO_API_KEY, model, method, args, kwargs)
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


# ---------------- HELPERS -------------------
def _detect_space_model(models, uid):
    global MODEL_SPACE
    if MODEL_SPACE: return MODEL_SPACE
    candidates = ['knowledge.space', 'knowledge.collection']
    res = odoo_search(models, uid, 'ir.model', [('model','in',candidates)], ['model'])
    found = {r['model'] for r in res}
    for m in candidates:
        if m in found:
            MODEL_SPACE = m
            return MODEL_SPACE
    raise RuntimeError("Không tìm thấy model Space (knowledge.space/knowledge.collection).")


def ensure_space(models, uid, space_name: str) -> int:
    space_model = _detect_space_model(models, uid)
    rec = odoo_search(models, uid, space_model, [("name","=",space_name)], ["id"], limit=1)
    if rec:
        print(f"  ✓ Dùng Space '{space_name}' (ID {rec[0]['id']})")
        return rec[0]['id']
    sid = odoo_create(models, uid, space_model, {"name": space_name})
    print(f"  ✓ Tạo Space '{space_name}' (ID {sid})")
    return sid


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
            # fallthrough
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
                            print(f"    ⚠️  OpenAPI parse lỗi {api_file}: {e}")

        if body:
            md = markdown.Markdown(extensions=['fenced_code','tables','nl2br'])
            html = md.convert(body)
        else:
            html = f"<p>Nội dung cho <strong>{title}</strong></p>"

        return {'title': title, 'html_content': html, 'front_matter': front_matter, 'slug': md_path.stem}
    except Exception as e:
        print(f"  ⚠️  Lỗi parse {md_path}: {e}")
        return None


def build_doc_tree(base_dir: Path) -> List[Dict[str, Any]]:
    all_docs = []
    file_counter = {'user_guide':0, 'developer_guide':0, 'release_notes':0}

    def process_directory_recursive(current_dir: Path, parent_slug: str, section_key: str, base_path: Path, root_base_dir: Path):
        order_items = read_order_yaml(current_dir / '_order.yaml')
        processed = set()
        for item in order_items:
            item_path = current_dir / item
            if item_path.is_dir():
                process_directory_recursive(item_path, parent_slug, section_key, base_path, root_base_dir)
                index_md = item_path / 'index.md'
                if index_md.exists() and index_md not in processed:
                    doc_data = parse_markdown_file(index_md, root_base_dir)
                    if doc_data:
                        file_counter[section_key]+=1
                        doc_data.update({
                            'parent_slug': parent_slug,
                            'order_index': file_counter[section_key],
                            'section': section_key,
                            'slug': str(index_md.relative_to(base_path)).replace('\\','/').replace('.md','').replace('/','-')
                        })
                        all_docs.append(doc_data); processed.add(index_md)
            elif (current_dir / f"{item}.md").exists():
                md_file = current_dir / f"{item}.md"
                if md_file not in processed:
                    doc_data = parse_markdown_file(md_file, root_base_dir)
                    if doc_data:
                        file_counter[section_key]+=1
                        doc_data.update({
                            'parent_slug': parent_slug,
                            'order_index': file_counter[section_key],
                            'section': section_key,
                            'slug': str(md_file.relative_to(base_path)).replace('\\','/').replace('.md','').replace('/','-')
                        })
                        all_docs.append(doc_data); processed.add(md_file)
        for md_file in sorted(current_dir.glob('*.md')):
            if md_file.name!='_order.yaml' and md_file not in processed:
                doc_data = parse_markdown_file(md_file, root_base_dir)
                if doc_data:
                    file_counter[section_key]+=1
                    doc_data.update({
                        'parent_slug': parent_slug,
                        'order_index': file_counter[section_key],
                        'section': section_key,
                        'slug': str(md_file.relative_to(base_path)).replace('\\','/').replace('.md','').replace('/','-')
                    })
                    all_docs.append(doc_data); processed.add(md_file)

    docs_dir = base_dir / 'docs'
    if docs_dir.exists(): print("  📂 docs/..."); process_directory_recursive(docs_dir, 'user-guide', 'user_guide', docs_dir, base_dir)
    reference_dir = base_dir / 'reference'
    if reference_dir.exists(): print("  📂 reference/..."); process_directory_recursive(reference_dir, 'developer-guide', 'developer_guide', reference_dir, base_dir)
    recipes_dir = base_dir / 'recipes'
    if recipes_dir.exists(): print("  📂 recipes/..."); process_directory_recursive(recipes_dir, 'release-notes', 'release_notes', recipes_dir, base_dir)

    parent_order = 1
    if file_counter['user_guide']>0:
        all_docs.insert(0, {'title':'User Guide','html_content':'<p>Tài liệu hướng dẫn sử dụng</p>','section':'user_guide','order_index':parent_order,'parent_slug':None,'slug':'user-guide','is_parent':True}); parent_order+=1
    if file_counter['developer_guide']>0:
        insert_pos = 1 if file_counter['user_guide']>0 else 0
        all_docs.insert(insert_pos, {'title':'Developer Guide','html_content':'<p>Tài liệu API & dev</p>','section':'developer_guide','order_index':parent_order,'parent_slug':None,'slug':'developer-guide','is_parent':True}); parent_order+=1
    if file_counter['release_notes']>0:
        insert_pos = (1 if file_counter['user_guide']>0 else 0) + (1 if file_counter['developer_guide']>0 else 0)
        all_docs.insert(insert_pos, {'title':'Release Notes','html_content':'<p>Ghi chú phiên bản</p>','section':'release_notes','order_index':parent_order,'parent_slug':None,'slug':'release-notes','is_parent':True})
    return all_docs


def replace_image_urls(models, uid, html: str, base_zip_dir: Path) -> str:
    if not html: return ""

    IMG_TAG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
    SRC_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
    SRCSET_RE = re.compile(r'(srcset)=["\']([^"\']+)["\']', re.IGNORECASE)
    SOURCE_SRCSET_RE = re.compile(r'(<source[^>]+srcset=["\'])([^"\']+)(["\'])', re.IGNORECASE)
    URL_IN_STYLE_RE = re.compile(r'url\((["\']?)([^)\'"]+)\1\)', re.IGNORECASE)

    def add_attrs(tag_html: str) -> str:
        style_attrs = 'style="max-width:800px!important;height:auto!important;display:block!important;object-fit:contain!important;"'
        if ' style=' not in tag_html:
            tag_html = tag_html.replace('<img', f'<img {style_attrs}', 1)
        else:
            tag_html = re.sub(r'style="[^"]*"', style_attrs, tag_html)
        if ' loading=' not in tag_html:
            tag_html = tag_html.replace('<img', '<img loading="lazy"', 1)
        return tag_html

    def wrap_img(m):
        return f'<figure style="max-width:800px;margin:12px auto;display:block;text-align:center;">{add_attrs(m.group(0))}</figure>'

    def _upload_local(local_rel: str) -> Optional[str]:
        local_rel_norm = re.sub(r'^(\.\./|\./|/)', '', local_rel)
        local_path = (base_zip_dir / local_rel_norm).resolve()
        if local_path.exists():
            key = str(local_path)
            if key in IMAGE_UPLOAD_CACHE:
                return IMAGE_UPLOAD_CACHE[key]
            print(f"    ⬆️  Upload ảnh: {local_rel_norm}")
            _, new_url = upload_attachment(models, uid, str(local_path), public=True)
            if new_url:
                IMAGE_UPLOAD_CACHE[key] = new_url
                return new_url
        else:
            print(f"    ⚠️  Không thấy ảnh: {local_path}")
        return None

    def replacer_src(m):
        original_src, full_tag = m.group(1), m.group(0)
        if original_src in IMAGE_UPLOAD_CACHE:
            return full_tag.replace(original_src, IMAGE_UPLOAD_CACHE[original_src])

        if re.match(r'(\.\./|\./|/)?(assets|files)[/\\]', original_src, re.IGNORECASE):
            new_url = _upload_local(original_src)
            if new_url:
                IMAGE_UPLOAD_CACHE[original_src] = new_url
                return full_tag.replace(original_src, new_url)

        if original_src.startswith(("http://","https://")):
            IMAGE_UPLOAD_CACHE[original_src] = original_src
        return full_tag

    def replacer_srcset_match(attr, srcset_val):
        parts = [p.strip() for p in srcset_val.split(',')]
        new_parts = []
        for p in parts:
            if not p: continue
            url_part = p.split()[0]
            rest = p[len(url_part):]
            mapped = IMAGE_UPLOAD_CACHE.get(url_part)
            if not mapped and re.match(r'(\.\./|\./|/)?(assets|files)[/\\]', url_part, re.IGNORECASE):
                mapped = _upload_local(url_part)
                if mapped: IMAGE_UPLOAD_CACHE[url_part] = mapped
            new_parts.append(f"{(mapped or url_part)}{rest}")
        return f'{attr}="' + ", ".join(new_parts) + '"'

    html = re.sub(SRC_RE, replacer_src, html)
    html = re.sub(IMG_TAG_RE, wrap_img, html)
    html = SRCSET_RE.sub(lambda m: replacer_srcset_match(m.group(1), m.group(2)), html)
    html = SOURCE_SRCSET_RE.sub(lambda m: m.group(1) + replacer_srcset_match('srcset', m.group(2)).split('=',1)[1].strip('"\'') + m.group(3), html)

    def css_url_replacer(m):
        quote, u = m.group(1), m.group(2)
        new_u = IMAGE_UPLOAD_CACHE.get(u)
        if not new_u and re.match(r'(\.\./|\./|/)?(assets|files)[/\\]', u, re.IGNORECASE):
            new_u = _upload_local(u)
            if new_u: IMAGE_UPLOAD_CACHE[u] = new_u
        return f"url({quote}{(new_u or u)}{quote})"
    html = URL_IN_STYLE_RE.sub(css_url_replacer, html)

    return html


# ------------------- IMPORTER CHÍNH -------------------
def import_all():
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)

    print("\n📚 Đọc ReadMe export...")
    base_dir = Path(README_EXPORT_DIR)
    if not base_dir.exists():
        raise SystemExit(f"❌ Không thấy thư mục export: {README_EXPORT_DIR}")

    all_docs = build_doc_tree(base_dir)
    print(f"  ✓ Tìm thấy {len(all_docs)} tài liệu")

    def sort_key(doc):
        is_parent = doc.get('is_parent', False)
        section = doc.get('section','unknown')
        order_idx = doc.get('order_index', 999999)
        section_order = {'user_guide':1,'developer_guide':2,'release_notes':3}.get(section, 999)
        return (section_order, 0 if is_parent else 1, order_idx)

    all_docs.sort(key=sort_key)

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

    for doc in all_docs:
        total_files += 1
        try:
            title = doc.get('title','Untitled')
            slug = doc.get('slug', f'doc_{total_files}')
            html_content = replace_image_urls(models, uid, doc.get('html_content',''), base_dir)
            id_seq = doc.get('_id_seq')

            if total_files % 10 == 0 or doc.get('is_parent'):
                print(f"\n[{total_files}] {title[:60]}")

            vals = {"name": title, "body": html_content, "space_id": space_id, "parent_id": False}
            if id_seq is not None: vals["sequence"] = id_seq

            existing = odoo_search(models, uid, MODEL_ARTICLE,
                [("name","=",title), ("space_id","=",space_id), ("parent_id","=",False)], ["id"], limit=1)

            if existing:
                rid = existing[0]["id"]
                odoo_write(models, uid, MODEL_ARTICLE, [rid], vals)
                article_ids[slug] = rid
                print(f"  ✓ Update (ID: {rid})")
            else:
                aid = odoo_create(models, uid, MODEL_ARTICLE, vals)
                article_ids[slug] = aid
                print(f"  ✓ Create (ID: {aid})")

            success_count += 1
        except Exception as e:
            print(f"\n❌ Lỗi '{doc.get('slug')}': {e}\n")

    print("\n🔗 Set parent...")
    fixed = 0
    for doc in all_docs:
        parent_slug = doc.get('parent_slug')
        if not parent_slug: continue
        child_id = article_ids.get(doc.get('slug'))
        parent_id = article_ids.get(parent_slug)
        if child_id and parent_id:
            odoo_write(models, uid, MODEL_ARTICLE, [child_id], {"parent_id": parent_id})
            fixed += 1
    if fixed: print(f"  ✓ Set parent cho {fixed} bài")

    print("\n📊 Cập nhật sequence...")
    seq_updated = 0
    for doc in all_docs:
        aid = article_ids.get(doc.get('slug'))
        if aid and doc.get('_id_seq') is not None:
            odoo_write(models, uid, MODEL_ARTICLE, [aid], {"sequence": doc.get('_id_seq')})
            seq_updated += 1
    if seq_updated: print(f"  ✓ Sequence updated: {seq_updated}")

    print("\n" + "="*60)
    print(f"✅ HOÀN TẤT")
    print(f"   Tổng: {total_files} | Thành công: {success_count} | Thất bại: {total_files - success_count}")
    print(f"   Space: '{SPACE_NAME}' (ID {space_id})")
    print("="*60)


# -------------------- MAIN ---------------------------
if __name__ == "__main__":
    try:
        import_all()
    except KeyboardInterrupt:
        print("\n⚠️ Hủy bởi người dùng")
    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback; traceback.print_exc()
