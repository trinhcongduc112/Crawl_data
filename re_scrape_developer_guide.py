"""
Re-scrape Developer Guide từ docs.abivin.com
Đây là script để fetch lại full content cho các API documentation pages
"""

import os
import json
import re
import time
import sys
import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Tuple

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

DEVELOPER_GUIDE_DIR = "developer_guide/content_developer_guide"
URL_MAPPING_FILE = "developer_guide/url_mapping_developer_guide.json"

def fetch_html(url: str, retries: int = 3) -> str:
    """Fetch HTML với retry logic"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            if attempt < retries - 1:
                print(f"  Retry {attempt + 1}/{retries}...")
                time.sleep(2)
            else:
                print(f"  ✗ Failed after {retries} attempts: {e}")
                return ""
    return ""

def extract_api_content(soup: BeautifulSoup) -> str:
    """Extract API documentation content"""
    # Tìm phần main content của API docs
    content_parts = []
    
    # Tìm article hoặc main content area
    article = soup.find('article') or soup.find('main') or soup.find('div', class_=re.compile('content|documentation|api'))
    
    if article:
        # Clean unwanted elements
        for tag in article.find_all(['script', 'style', 'nav', 'aside', 'footer', 'header']):
            tag.decompose()
        
        # Tìm các section chính
        sections = article.find_all(['section', 'div'], class_=re.compile('api|endpoint|method|request|response'))
        
        if sections:
            for section in sections:
                html = str(section)
                # Clean HTML một chút
                html = re.sub(r'\s+', ' ', html)
                content_parts.append(html)
        else:
            # Nếu không có section riêng, lấy toàn bộ content
            html = str(article)
            content_parts.append(html)
    else:
        # Fallback: lấy body content
        body = soup.find('body')
        if body:
            for tag in body.find_all(['script', 'style', 'nav', 'aside', 'footer', 'header']):
                tag.decompose()
            content_parts.append(str(body))
    
    return '\n'.join(content_parts)

def clean_html_for_display(html: str) -> str:
    """Clean HTML để hiển thị tốt trong Odoo"""
    if not html:
        return "<p>No content available</p>"
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Loại bỏ các thẻ không cần thiết
    for tag in soup.find_all(['script', 'style', 'link', 'meta']):
        tag.decompose()
    
    # Loại bỏ các elements trống
    for tag in soup.find_all(['div', 'span', 'p']):
        if not tag.get_text(strip=True):
            tag.decompose()
    
    # Thêm style cho code blocks
    for pre in soup.find_all('pre'):
        pre['style'] = 'background: #f6f8fa; border: 1px solid #eaecef; border-radius: 6px; padding: 12px; overflow: auto;'
    
    for code in soup.find_all('code'):
        if code.parent.name != 'pre':  # Code block riêng lẻ
            code['style'] = 'background: #f6f8fa; padding: 2px 6px; border-radius: 3px; font-family: Consolas, monospace;'
    
    # Thêm style cho images
    for img in soup.find_all('img'):
        img['style'] = 'max-width: 100%; height: auto;'
    
    return str(soup)

def update_developer_guide_file(json_path: str, new_html: str) -> bool:
    """Update JSON file với nội dung mới"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            doc = json.load(f)
        
        old_html = doc.get('html_content', '')
        
        # Nếu content mới khác và có ý nghĩa hơn
        if new_html and len(new_html) > len(old_html) * 1.5:
            doc['html_content'] = new_html
            doc['updated_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ')
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(doc, f, ensure_ascii=False, indent=2)
            return True
        return False
    except Exception as e:
        print(f"  ✗ Error updating file: {e}")
        return False

def main():
    """Main function"""
    print("="*60)
    print("🔄 RE-SCRAPING DEVELOPER GUIDE")
    print("="*60)
    
    # Load URL mapping
    try:
        with open(URL_MAPPING_FILE, 'r', encoding='utf-8') as f:
            url_mapping = json.load(f)
    except Exception as e:
        print(f"❌ Không thể load URL mapping: {e}")
        return
    
    total = len(url_mapping)
    updated = 0
    failed = 0
    
    for idx, (url, json_path) in enumerate(url_mapping.items(), 1):
        if not json_path.startswith('C:'):
            # Handle relative paths
            json_path = json_path.replace('\\', '/')
        
        # Extract slug để hiển thị
        slug = os.path.basename(json_path)
        print(f"\n[{idx}/{total}] {slug}")
        print(f"  URL: {url}")
        
        # Fetch HTML
        html = fetch_html(url)
        if not html:
            print("  ✗ Không thể fetch content")
            failed += 1
            continue
        
        # Parse và extract content
        soup = BeautifulSoup(html, 'html.parser')
        api_content = extract_api_content(soup)
        cleaned_content = clean_html_for_display(api_content)
        
        # Update file nếu content tốt hơn
        if update_developer_guide_file(json_path, cleaned_content):
            print(f"  ✓ Updated content ({len(cleaned_content)} chars)")
            updated += 1
        else:
            print(f"  → Không cần update (content không khác nhiều)")
        
        # Delay để tránh rate limit
        time.sleep(1)
    
    print("\n" + "="*60)
    print(f"✅ HOÀN TẤT!")
    print(f"   Total: {total}")
    print(f"   Updated: {updated}")
    print(f"   Failed: {failed}")
    print("="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Người dùng hủy bỏ!")
    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback
        traceback.print_exc()






