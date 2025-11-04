"""
ReadMe.io Web Scraper - Improved version với:
1. Parse sidebar navigation để giữ nguyên cấu trúc cha-con
2. Lọc bỏ tags không liên quan (Google, analytics, etc)
3. Xác định parent-child relationships

Author: Abivin
Python: 3.8+
"""

import os
import re
import json
import time
import argparse
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from typing import Dict, List, Tuple, Set, Optional

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_HOST = "docs.abivin.com"

# Blacklist domains/tags cần lọc bỏ
BLACKLIST_DOMAINS = [
    'google.com', 'googleapis.com', 'gstatic.com', 'googletagmanager.com',
    'google-analytics.com', 'analytics.google.com', 'googlesyndication.com',
    'doubleclick.net', 'facebook.com', 'facebook.net', 
    'twitter.com', 'linkedin.com', 'pinterest.com',
    'hotjar.com', 'optimizely.com', 'segment.io',
    'mixpanel.com', 'newrelic.com', 'adobe.com',
    'amazon-adsystem.com', 'adsrvr.org', 'pubmatic.com',
    # Readme.io specific tracking nếu không cần
]
BLACKLIST_TAGS = ['script', 'style', 'noscript', 'iframe']  # Lọc các thẻ không cần thiết

# Blacklist classes/IDs để loại bỏ
BLACKLIST_CLASSES = [
    'advertisement', 'ad', 'ads', 'sidebar', 'advert',
    'tracking', 'analytics', 'gtm', 'fb-pixel',
    'cookie-banner', 'cookie-consent', 'cookiebot'
]


def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def write_json(path: str, obj: dict) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def path_to_slug(path: str) -> str:
    """Convert a URL-like path to a filesystem-safe slug."""
    base = (path or "/").strip("/").replace("/", "__")
    return base or "index"


def to_segments_from_path(path: str, section_root: str) -> List[str]:
    parts = [x for x in (path or "").strip("/").split("/") if x]
    if section_root in parts:
        i = parts.index(section_root)
        return parts[i:-1]  # bỏ segment cuối (doc slug)
    return parts[:-1]


def clean_html_content(soup: BeautifulSoup) -> str:
    """
    Clean HTML content: loại bỏ các thẻ không cần thiết và blacklisted domains
    """
    # 1. Remove unwanted tags
    for tag_name in BLACKLIST_TAGS:
        for tag in soup.find_all(tag_name):
            tag.decompose()
    
    # 2. Remove elements with blacklisted classes/IDs
    for class_name in BLACKLIST_CLASSES:
        # Remove by class
        for tag in soup.find_all(class_=lambda x: x and class_name in ' '.join(x)):
            tag.decompose()
        # Remove by ID
        for tag in soup.find_all(id=lambda x: x and class_name in x):
            tag.decompose()
    
    # 3. Remove links to blacklisted domains
    for link in soup.find_all('a', href=True):
        href = link.get('href', '')
        if any(domain in href for domain in BLACKLIST_DOMAINS):
            # Convert to plain text, giữ lại nội dung bên trong
            text = link.get_text()
            link.replace_with(text if text else '')
    
    # 4. Remove images from blacklisted domains
    for img in soup.find_all('img', src=True):
        src = img.get('src', '')
        if any(domain in src for domain in BLACKLIST_DOMAINS):
            img.decompose()
    
    # 5. Remove tracking pixels và invisible elements
    for tag in soup.find_all(['img', 'div', 'span']):
        # Check if very small size (likely tracking pixel)
        style = tag.get('style', '')
        if ('width:1px' in style or 'width:0' in style or 
            'height:1px' in style or 'height:0' in style):
            tag.decompose()
        
        # Check visibility hidden
        if 'visibility:hidden' in style or 'display:none' in style:
            tag.decompose()
    
    # 6. Clean up attributes không cần thiết (onclick, data-track, etc)
    for tag in soup.find_all():
        # Remove tracking attributes
        attrs_to_remove = []
        for attr in tag.attrs:
            if any(x in attr.lower() for x in ['onclick', 'data-track', 'data-analytics', 
                                                 'data-ga', 'data-gtm', 'data-fb', 
                                                 'data-tealium', 'data-optimize']):
                attrs_to_remove.append(attr)
        for attr in attrs_to_remove:
            del tag.attrs[attr]
    
    # 7. Normalize internal links and images to absolute URLs
    for tag in soup.find_all(['a', 'img'], href=True):
        href = tag.get('href')
        if href and href.startswith('/') and not href.startswith('//'):
            tag['href'] = f"https://{PROJECT_HOST}{href}"
    
    for tag in soup.find_all(['a', 'img'], src=True):
        src = tag.get('src')
        if src and src.startswith('/') and not src.startswith('//'):
            tag['src'] = f"https://{PROJECT_HOST}{src}"
    
    return str(soup)


def extract_title_and_content(soup: BeautifulSoup, url: str) -> Tuple[str, str]:
    """Extract title and cleaned content from page"""
    # Tìm title
    title = ""
    title_tag = soup.find('h1') or soup.find('title')
    if title_tag:
        title = title_tag.get_text(strip=True)
    
    # Lấy content từ main/article
    main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
    
    if main_content:
        # Loại bỏ header, footer, nav, aside trước khi clone
        for element in main_content.find_all(['header', 'footer', 'nav', 'aside']):
            element.decompose()
        
        # Loại bỏ breadcrumb, pagination, comments
        for element in main_content.find_all(class_=lambda x: x and any(
            kw in ' '.join(x).lower() for kw in ['breadcrumb', 'pagination', 'comment', 'social-share']
        )):
            element.decompose()
        
        # Clone để không ảnh hưởng đến soup gốc
        content_clone = BeautifulSoup(str(main_content), 'html.parser')
        content_html = clean_html_content(content_clone)
    else:
        # Fallback: lấy body và loại bỏ các phần không cần thiết
        body = soup.find('body')
        if body:
            # Loại bỏ nav, header, footer, aside
            for tag_name in ['header', 'footer', 'nav', 'aside', 'script', 'style']:
                for tag in body.find_all(tag_name):
                    tag.decompose()
            
            # Loại bỏ các phần UI không cần thiết
            for element in body.find_all(class_=lambda x: x and any(
                kw in ' '.join(x).lower() for kw in [
                    'header', 'footer', 'breadcrumb', 'pagination', 
                    'sidebar', 'menu', 'navigation', 'comment'
                ]
            )):
                element.decompose()
            
            content_html = clean_html_content(BeautifulSoup(str(body), 'html.parser'))
        else:
            content_html = ""
    
    return title or url.split("/")[-1], content_html


def scrape_page(url: str) -> Tuple[str, BeautifulSoup]:
    """Scrape a single page"""
    print(f"  Scraping: {url}")
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text, BeautifulSoup(r.text, 'html.parser')


def parse_sidebar_navigation(soup: BeautifulSoup, base_url: str) -> Dict[str, Dict]:
    """
    Parse sidebar navigation để tìm cấu trúc cha-con
    Returns: {url: {title, parent_url, level, children}}
    """
    nav_structure = {}
    
    # Tìm sidebar/navigation
    sidebar = soup.find('nav') or soup.find('aside') or soup.find('div', class_='sidebar')
    
    if not sidebar:
        return nav_structure
    
    # Parse navigation structure
    current_parent = None
    current_level = 0
    
    for element in sidebar.descendants:
        if element.name == 'a':
            href = element.get('href', '')
            if not href:
                continue
            
            # Convert relative URL to absolute
            if href.startswith('/'):
                full_url = f"https://{PROJECT_HOST}{href}"
            else:
                full_url = urljoin(base_url, href)
            
            title = element.get_text(strip=True)
            
            # Determine level based on indentation (check parent elements)
            level = 0
            parent = element.parent
            while parent:
                if parent.name in ['ul', 'ol']:
                    level += 1
                parent = parent.parent
            
            nav_structure[full_url] = {
                'title': title,
                'parent_url': None,  # Will be determined later
                'level': level,
            }
    
    # Build parent-child relationships
    sorted_urls = sorted(nav_structure.items(), key=lambda x: x[1]['level'])
    
    for i, (url, info) in enumerate(sorted_urls):
        # Find parent by looking at previous items with lower level
        for j in range(i-1, -1, -1):
            prev_url, prev_info = sorted_urls[j]
            if prev_info['level'] < info['level']:
                info['parent_url'] = prev_url
                break
    
    return nav_structure


def extract_links_in_order(element, base_url: str, category_slug: str) -> List[Tuple[str, str]]:
    """
    Extract links theo đúng thứ tự DOM traversal
    Returns: List of (url, title) tuples
    """
    links = []
    seen_hrefs = set()
    
    def traverse(node):
        """Recursive traversal để giữ đúng thứ tự"""
        if node.name == 'a':
            href = node.get('href', '')
            if href and href not in seen_hrefs:
                # Convert to absolute URL
                if href.startswith('/'):
                    full_url = f"https://{PROJECT_HOST}{href}"
                else:
                    full_url = urljoin(base_url, href)
                
                # Chỉ lấy links thuộc category này
                if category_slug in full_url:
                    title = node.get_text(strip=True)
                    if title:  # Chỉ lấy link có text
                        seen_hrefs.add(href)
                        links.append((full_url, title))
        
        # Tiếp tục traverse children
        if hasattr(node, 'children'):
            for child in node.children:
                if hasattr(child, 'name'):  # Chỉ process elements
                    traverse(child)
    
    traverse(element)
    return links


def find_all_pages_in_category(category_url: str, category_slug: str) -> Tuple[List[str], Dict]:
    """
    Tìm tất cả pages trong category BẰNG CÁCH:
    1. Lấy từ sidebar navigation THEO ĐÚNG THỨ TỰ DOM TRAVERSAL
    2. Lấy từ links trong page (nếu chưa có)
    """
    print(f"  Parsing navigation from: {category_url}")
    
    html, soup = scrape_page(category_url)
    
    # BƯỚC 1: Lấy cấu trúc cha-con (để dùng sau)
    nav_structure = parse_sidebar_navigation(soup, category_url)
    
    # BƯỚC 2: XÂY DỰNG DANH SÁCH CÓ THỨ TỰ (QUAN TRỌNG - SỬA LẠI)
    ordered_urls = []
    seen_urls = set()
    url_to_title = {}  # Map URL -> title để dùng sau

    # Hàm trợ giúp để thêm URL vào danh sách
    def add_url_if_new(url: str, title: str = ""):
        if url and url not in seen_urls and category_slug in url:
            seen_urls.add(url)
            ordered_urls.append(url)
            if title:
                url_to_title[url] = title

    # Thêm trang category gốc (trang chủ của section)
    add_url_if_new(category_url)

    # Lấy sidebar
    sidebar = soup.find('nav') or soup.find('aside') or soup.find('div', class_='sidebar') or soup.find('div', class_=lambda x: x and 'sidebar' in ' '.join(x).lower())
    
    # ƯU TIÊN 1: Lấy link từ sidebar TRƯỚC (theo đúng thứ tự DOM)
    if sidebar:
        print("  Processing sidebar links (in DOM order)...")
        sidebar_links = extract_links_in_order(sidebar, category_url, category_slug)
        for full_url, title in sidebar_links:
            add_url_if_new(full_url, title)
            # Cập nhật nav_structure với title chính xác
            if full_url in nav_structure:
                nav_structure[full_url]['title'] = title
            
    # ƯU TIÊN 2: Lấy tất cả các link khác từ nội dung chính
    # (Phòng trường hợp sidebar bị thiếu link)
    print("  Processing remaining page links...")
    main_content = soup.find('main') or soup.find('article') or soup.find('body')
    if main_content:
        content_links = extract_links_in_order(main_content, category_url, category_slug)
        for full_url, title in content_links:
            add_url_if_new(full_url, title)
    
    print(f"  Found {len(ordered_urls)} unique pages (in order)")
    
    # Trả về danh sách ĐÃ CÓ THỨ TỰ (không sorted alphabet)
    return ordered_urls, nav_structure


def parse_openapi_file(openapi_file: str, section_key: str, out_base: str) -> Tuple[int, int]:
    """
    Parse OpenAPI/Swagger JSON file và tạo article JSON files
    Đây là cách đúng để xử lý Developer Guide (Swagger) thay vì scrape HTML
    """
    print(f"\n{'='*60}")
    print(f"=== Parsing OpenAPI: {os.path.basename(openapi_file)} ===")
    print(f"{'='*60}\n")
    
    # Kiểm tra file size trước
    file_size = os.path.getsize(openapi_file)
    if file_size < 200:
        print(f"[WARN] File quá nhỏ ({file_size} bytes) - có thể là file không hợp lệ hoặc chỉ là placeholder")
        print(f"       Đang kiểm tra nội dung...")
    
    # Đọc file và kiểm tra format (tự động xử lý BOM)
    try:
        with open(openapi_file, "r", encoding="utf-8-sig") as f:
            file_content = f.read()
    except Exception as e:
        print(f"[ERR] Không thể đọc file: {e}")
        return 0, 0
    
    # Kiểm tra nếu file là JavaScript object (không phải JSON hợp lệ)
    # Dấu hiệu: có dấu hai chấm nhưng không có quotes quanh keys (hoặc rất ít)
    file_start = file_content.strip()[:300]
    has_colon = ':' in file_start
    has_quotes = '"' in file_start
    # Nếu có dấu hai chấm nhưng rất ít quotes, có thể là JavaScript object notation
    if has_colon and file_start.count('"') < 4:
        print(f"[ERR] File không phải JSON hợp lệ!")
        print(f"       File hiện tại có vẻ là JavaScript object notation (thiếu quotes)")
        print(f"       Ví dụ sai: {{ openapi:3.0.0, info: {{title:...}} }}")
        print(f"       Cần JSON hợp lệ: {{\"openapi\":\"3.0.0\",\"info\":{{\"title\":...}}}}")
        print(f"\n       Hướng dẫn sửa:")
        print(f"       1. Mở trang Developer Guide/API Reference trên docs.abivin.com")
        print(f"       2. Mở Developer Tools (F12) > Network tab")
        print(f"       3. Tải lại trang (F5)")
        print(f"       4. Tìm request có tên chứa 'openapi' hoặc 'swagger' (thường là .json)")
        print(f"       5. Right-click > Open in new tab > Copy URL")
        print(f"       6. Download file đầy đủ bằng curl/wget hoặc trình duyệt")
        print(f"       7. Đảm bảo file là JSON hợp lệ và có trường 'paths' chứa các endpoints")
        return 0, 0
    
    # Parse JSON
    try:
        openapi_spec = json.loads(file_content)
    except json.JSONDecodeError as e:
        print(f"[ERR] Lỗi parse JSON: {e}")
        print(f"       Dòng {e.lineno}, cột {e.colno}: {e.msg}")
        print(f"       File không phải JSON hợp lệ. Vui lòng kiểm tra lại.")
        return 0, 0
    except Exception as e:
        print(f"[ERR] Lỗi không xác định khi parse file: {e}")
        return 0, 0
    
    # Kiểm tra cấu trúc OpenAPI
    if not isinstance(openapi_spec, dict):
        print(f"[ERR] File không phải là OpenAPI spec hợp lệ (phải là object/dict)")
        return 0, 0
    
    # Kiểm tra trường bắt buộc
    if "openapi" not in openapi_spec and "swagger" not in openapi_spec:
        print(f"[WARN] File thiếu trường 'openapi' hoặc 'swagger' - có thể không phải OpenAPI spec")
    
    # Kiểm tra paths - đây là phần quan trọng nhất
    paths = openapi_spec.get("paths", {})
    if not paths or not isinstance(paths, dict):
        print(f"[ERR] File thiếu hoặc không có trường 'paths'!")
        print(f"       Đây là trường bắt buộc chứa định nghĩa các API endpoints")
        print(f"       File hiện tại chỉ có metadata, không có endpoints thực tế")
        print(f"\n       Cần tải lại file OpenAPI đầy đủ từ:")
        print(f"       - Network tab trong Developer Tools")
        print(f"       - Hoặc từ URL: https://docs.abivin.com/reference/openapi.json (nếu có)")
        return 0, 0
    
    # Lấy thông tin API trước khi thông báo
    info = openapi_spec.get("info", {})
    api_title = info.get("title", "API Documentation")
    api_version = info.get("version", "1.0.0")
    api_description = info.get("description", "")
    servers = openapi_spec.get("servers", [])
    base_url = servers[0].get("url", "") if servers else ""
    
    # Thông báo thành công
    num_endpoints = sum(len([m for m in p.keys() if m.lower() in ["get", "post", "put", "patch", "delete", "head", "options"]]) 
                        for p in paths.values())
    print(f"[OK] File OpenAPI hợp lệ!")
    print(f"     Title: {api_title}")
    print(f"     Version: {api_version}")
    print(f"     Paths: {len(paths)}")
    print(f"     Endpoints: {num_endpoints}")
    print(f"     Đang tạo articles...\n")
    
    base_folder = os.path.join(out_base, section_key)
    content_dir = os.path.join(base_folder, f"content_{section_key}")
    ensure_dir(content_dir)
    
    def escape_html(text):
        if not text:
            return ""
        return (str(text).replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace('"', "&quot;"))
    
    # Tạo index page
    index_html = f"<h1>{escape_html(api_title)}</h1>"
    index_html += f"<p>Version: <code>{escape_html(api_version)}</code></p>"
    if api_description:
        index_html += f"<p>{escape_html(api_description)}</p>"
    if base_url:
        index_html += f"<p>Base URL: <code>{escape_html(base_url)}</code></p>"
    index_html += "<h2>Available Endpoints</h2><ul>"
    
    articles = []
    idx = 2
    
    for path, path_item in sorted(paths.items()):
        for method, operation in path_item.items():
            if method.lower() not in ["get", "post", "put", "patch", "delete", "head", "options"]:
                continue
            
            op_id = operation.get("operationId", f"{method.upper()} {path}")
            summary = operation.get("summary", op_id)
            desc = operation.get("description", "")
            tags = operation.get("tags", [])
            params = operation.get("parameters", [])
            req_body = operation.get("requestBody", {})
            responses = operation.get("responses", {})
            
            # Build HTML
            html_parts = [f"<h1>{escape_html(summary)}</h1>"]
            html_parts.append(f"<p><strong>Method:</strong> <code>{method.upper()}</code></p>")
            html_parts.append(f"<p><strong>Path:</strong> <code>{escape_html(path)}</code></p>")
            
            if desc:
                html_parts.append(f"<p>{escape_html(desc)}</p>")
            if tags:
                html_parts.append(f"<p><strong>Tags:</strong> {', '.join([f'<code>{escape_html(t)}</code>' for t in tags])}</p>")
            
            # Parameters
            if params:
                html_parts.append("<h3>Parameters</h3><table border='1' style='border-collapse: collapse;'><tr><th>Name</th><th>In</th><th>Required</th><th>Type</th><th>Description</th></tr>")
                for p in params:
                    name = p.get("name", "")
                    p_in = p.get("in", "")
                    req = "Yes" if p.get("required", False) else "No"
                    schema = p.get("schema", {})
                    p_type = schema.get("type", "")
                    if schema.get("format"):
                        p_type += f" ({schema.get('format')})"
                    p_desc = p.get("description", "")
                    html_parts.append(f"<tr><td><code>{escape_html(name)}</code></td><td>{escape_html(p_in)}</td><td>{req}</td><td>{escape_html(p_type)}</td><td>{escape_html(p_desc)}</td></tr>")
                html_parts.append("</table>")
            
            # Request Body
            if req_body:
                html_parts.append("<h3>Request Body</h3>")
                content = req_body.get("content", {})
                if "application/json" in content:
                    schema = content["application/json"].get("schema", {})
                    example = content["application/json"].get("example")
                    if not example and "example" in schema:
                        example = schema.get("example")
                    if example:
                        html_parts.append(f"<pre><code>{json.dumps(example, indent=2, ensure_ascii=False)}</code></pre>")
                    elif "$ref" in schema:
                        html_parts.append(f"<p>Schema reference: <code>{schema['$ref']}</code></p>")
            
            # Responses
            if responses:
                html_parts.append("<h3>Responses</h3>")
                for status, resp in responses.items():
                    html_parts.append(f"<h4>HTTP {escape_html(status)}</h4>")
                    if resp.get("description"):
                        html_parts.append(f"<p>{escape_html(resp.get('description'))}</p>")
                    content = resp.get("content", {})
                    if "application/json" in content:
                        schema = content["application/json"].get("schema", {})
                        example = content["application/json"].get("example")
                        if example:
                            html_parts.append(f"<pre><code>{json.dumps(example, indent=2, ensure_ascii=False)}</code></pre>")
            
            # Create slug
            safe_path = path.strip("/").replace("/", "__")
            slug = f"reference__{method.lower()}_{safe_path}" if safe_path else f"reference__{method.lower()}"
            
            article = {
                "origin_url": f"https://{PROJECT_HOST}/reference/{op_id}",
                "origin_host": PROJECT_HOST,
                "collection": "abivin-docs",
                "section": section_key,
                "parents_segments": ["reference"],
                "parent_slug": "reference",
                "order_index": idx,
                "_id_seq": idx,
                "old_slug": slug,
                "new_slug": slug,
                "title": summary,
                "html_content": "".join(html_parts),
                "tags": tags,
                "lang": "en",
                "status": "ready",
                "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "scraped": False,
                "_readme_category": "reference",
                "_openapi_source": os.path.basename(openapi_file),
            }
            
            articles.append((slug, article))
            index_html += f'<li><a href="#{slug}">{escape_html(summary)}</a> - <code>{method.upper()} {escape_html(path)}</code></li>'
            idx += 1
    
    index_html += "</ul>"
    
    # Write index
    index_doc = {
        "origin_url": f"https://{PROJECT_HOST}/reference",
        "origin_host": PROJECT_HOST,
        "collection": "abivin-docs",
        "section": section_key,
        "parents_segments": [],
        "parent_slug": None,
        "order_index": 1,
        "_id_seq": 1,
        "old_slug": "reference",
        "new_slug": "reference",
        "title": api_title,
        "html_content": index_html,
        "tags": [],
        "lang": "en",
        "status": "ready",
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "scraped": False,
        "_readme_category": "reference",
        "_openapi_source": os.path.basename(openapi_file),
    }
    
    index_path = os.path.join(content_dir, "reference.json")
    write_json(index_path, index_doc)
    print(f"[1/{len(articles)+1}] Created index: reference.json")
    
    # Write articles
    created = 1
    for slug, article in articles:
        article_path = os.path.join(content_dir, f"{slug}.json")
        write_json(article_path, article)
        created += 1
    
    print(f"[OK] Created {created} articles ({len(articles)} endpoints + 1 index)")
    return created, created


def export_category(category_slug: str, section_key: str, root_seg: str, out_base: str) -> Tuple[int, int]:
    """
    Scrape and export category với đầy đủ cấu trúc cha-con
    """
    base_folder = os.path.join(out_base, section_key)
    content_dir = os.path.join(base_folder, f"content_{section_key}")
    ensure_dir(content_dir)
    
    category_url = f"https://{PROJECT_HOST}/{category_slug}"
    
    try:
        all_urls, nav_structure = find_all_pages_in_category(category_url, category_slug)
    except Exception as e:
        print(f"[ERR] Cannot parse navigation: {e}")
        return 0, 0
    
    # Load existing mapping
    mapping_fp = os.path.join(base_folder, f"url_mapping_{section_key}.json")
    old_map: Dict[str, str] = {}
    if os.path.exists(mapping_fp):
        try:
            old_map = json.load(open(mapping_fp, "r", encoding="utf-8"))
        except Exception:
            old_map = {}
    
    # Build parent_url to slug mapping
    parent_slug_map = {}
    for url in all_urls:
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        slug = path_to_slug(path)
        parent_slug_map[url] = slug
    
    url_map: Dict[str, str] = {}
    total_docs = 0
    created_files = 0
    
    for idx, url in enumerate(all_urls, 1):
        print(f"[{idx}/{len(all_urls)}] Processing: {url}")
        
        try:
            html_text, soup = scrape_page(url)
            
            # Get navigation info for this URL
            nav_info = nav_structure.get(url, {})
            title_from_nav = nav_info.get('title', '')
            parent_url = nav_info.get('parent_url')
            
            # Extract title and content
            title, content_html = extract_title_and_content(soup, url)
            
            # Use title from navigation if available
            if title_from_nav:
                title = title_from_nav
            
            # Build path and slug
            parsed = urlparse(url)
            path = parsed.path.strip("/")
            parents = to_segments_from_path(path, root_seg)
            full_slug = path_to_slug(path)
            
            # Determine parent slug if exists
            parent_slug = None
            if parent_url and parent_url in parent_slug_map:
                parent_slug = parent_slug_map[parent_url]
            
            # Build doc structure (gán thứ tự crawl làm order_index và _id_seq)
            doc = {
                "origin_url": url.rstrip("/"),
                "origin_host": PROJECT_HOST,
                "collection": "abivin-docs",
                "section": section_key,
                "parents_segments": parents,
                "parent_slug": parent_slug,  # NEW: lưu parent
                "order_index": idx,
                "_id_seq": idx,
                "old_slug": full_slug,
                "new_slug": full_slug,
                "title": title,
                "html_content": content_html,
                "tags": [],
                "lang": "en",
                "status": "ready",
                "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "scraped": True,
                "_readme_category": category_slug,
            }
            
            out_fp = os.path.join(content_dir, f"{full_slug}.json")
            url_map[doc["origin_url"]] = out_fp
            
            # Check if needs update
            need_write = True
            if os.path.exists(out_fp):
                try:
                    old = json.load(open(out_fp, "r", encoding="utf-8"))
                    if (old.get("title") == doc["title"] 
                        and len(old.get("html_content") or "") == len(doc["html_content"])):
                        need_write = False
                        print(f"  Skip (unchanged)")
                except Exception:
                    need_write = True
            
            if need_write:
                write_json(out_fp, doc)
                created_files += 1
                print(f"  Written ✓")
            
            total_docs += 1
            time.sleep(0.5)  # Rate limiting
            
        except Exception as e:
            print(f"  Error: {e}")
            continue
    
    write_json(mapping_fp, url_map)
    print(f"[OK] {section_key} → {total_docs} docs (wrote {created_files}, skipped {total_docs - created_files})")
    return total_docs, created_files


def main():
    ap = argparse.ArgumentParser(
        description="Improved ReadMe scraper with parent-child structure and OpenAPI support"
    )
    ap.add_argument("--out", required=True, help="Base output directory")
    ap.add_argument("--map", default="changelog:release_notes:changelog,docs:user_guide:docs",
                     help="Category mappings: 'category_slug:section_key:root_segment' (comma-separated)")
    ap.add_argument("--openapi-dir", default=None,
                     help="Directory containing OpenAPI JSON files (for Developer Guide/Swagger)")
    ap.add_argument("--openapi-section", default="developer_guide",
                     help="Section key for OpenAPI files (default: developer_guide)")
    args = ap.parse_args()
    
    ensure_dir(args.out)
    summary = []
    
    # Parse map
    mappings = []
    if args.map:
        for part in args.map.split(','):
            if not part.strip():
                continue
            bits = [b.strip() for b in part.split(':')]
            if len(bits) == 3:
                mappings.append((bits[0], bits[1], bits[2]))
    
    # Process regular HTML scraping
    for cat_slug, section_key, root_seg in mappings:
        print(f"\n{'='*60}")
        print(f"=== Exporting {section_key} (category: {cat_slug}) ===")
        print(f"{'='*60}\n")
        try:
            total, wrote = export_category(cat_slug, section_key, root_seg, args.out)
            summary.append((section_key, total, wrote))
        except Exception as e:
            print(f"[ERR] Export {section_key} failed: {e}")
    
    # Process OpenAPI files (for Developer Guide/Swagger)
    if args.openapi_dir and os.path.isdir(args.openapi_dir):
        print(f"\n{'='*60}")
        print(f"=== Processing OpenAPI files from: {args.openapi_dir} ===")
        print(f"{'='*60}\n")
        
        openapi_files = [f for f in os.listdir(args.openapi_dir) 
                        if f.endswith(('.json', '.yaml', '.yml'))]
        
        if not openapi_files:
            print(f"[WARN] No OpenAPI files found in '{args.openapi_dir}'")
            print("\nHướng dẫn lấy OpenAPI file:")
            print("1. Mở trang Developer Guide trên trình duyệt")
            print("2. Mở Developer Tools (F12) > Network tab")
            print("3. Tải lại trang (F5)")
            print("4. Tìm file .json hoặc .yaml (ví dụ: openapi.json)")
            print("5. Right-click > Save as > Lưu vào thư mục chỉ định")
        else:
            for openapi_file in openapi_files:
                openapi_path = os.path.join(args.openapi_dir, openapi_file)
                try:
                    total, wrote = parse_openapi_file(openapi_path, args.openapi_section, args.out)
                    summary.append((f"{args.openapi_section} ({openapi_file})", total, wrote))
                except Exception as e:
                    print(f"[ERR] Failed to process {openapi_file}: {e}")
    
    # Summary
    if summary:
        print(f"\n{'='*60}")
        print("=== SUMMARY ===")
        print(f"{'='*60}")
        for section_key, total, wrote in summary:
            print(f"{section_key}: {total} docs (wrote {wrote}, skipped {total - wrote})")
    else:
        print("\nNo sections exported.")


if __name__ == "__main__":
    main()

