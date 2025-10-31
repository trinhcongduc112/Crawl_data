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


def find_all_pages_in_category(category_url: str, category_slug: str) -> List[str]:
    """
    Tìm tất cả pages trong category bằng cách:
    1. Lấy từ sidebar navigation
    2. Lấy từ links trong page
    """
    print(f"  Parsing navigation from: {category_url}")
    
    html, soup = scrape_page(category_url)
    
    # Parse navigation structure
    nav_structure = parse_sidebar_navigation(soup, category_url)
    
    # Also collect all links
    all_urls = set()
    
    # Add all URLs from navigation
    for url in nav_structure.keys():
        if category_slug in url:
            all_urls.add(url)
    
    # Also get links from page content
    for link in soup.find_all('a', href=True):
        href = link.get('href', '')
        if href.startswith('/'):
            full_url = f"https://{PROJECT_HOST}{href}"
            if href.startswith(f'/{category_slug}'):
                all_urls.add(full_url)
    
    all_urls.add(category_url)
    
    print(f"  Found {len(all_urls)} unique pages")
    return sorted(list(all_urls)), nav_structure


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
            
            # Build doc structure
            doc = {
                "origin_url": url.rstrip("/"),
                "origin_host": PROJECT_HOST,
                "collection": "abivin-docs",
                "section": section_key,
                "parents_segments": parents,
                "parent_slug": parent_slug,  # NEW: lưu parent
                "order_index": idx,
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
        description="Improved ReadMe scraper with parent-child structure"
    )
    ap.add_argument("--out", required=True, help="Base output directory")
    ap.add_argument("--map", default="changelog:release_notes:changelog,docs:user_guide:docs")
    args = ap.parse_args()
    
    # Parse map
    mappings = []
    if args.map:
        for part in args.map.split(','):
            if not part.strip():
                continue
            bits = [b.strip() for b in part.split(':')]
            if len(bits) == 3:
                mappings.append((bits[0], bits[1], bits[2]))
    
    ensure_dir(args.out)
    summary = []
    
    for cat_slug, section_key, root_seg in mappings:
        print(f"\n{'='*60}")
        print(f"=== Exporting {section_key} (category: {cat_slug}) ===")
        print(f"{'='*60}\n")
        try:
            total, wrote = export_category(cat_slug, section_key, root_seg, args.out)
            summary.append((section_key, total, wrote))
        except Exception as e:
            print(f"[ERR] Export {section_key} failed: {e}")
    
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

