"""
Download images from files.readme.io và replace URLs in HTML content
"""

import os
import re
import json
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, urljoin
from typing import Set, Dict

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_HOST = "docs.abivin.com"


def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def download_image(url: str, save_path: str) -> bool:
    """Download một image"""
    try:
        print(f"  Downloading: {url}")
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        
        # Lưu file
        ensure_dir(os.path.dirname(save_path))
        with open(save_path, 'wb') as f:
            f.write(r.content)
        
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def extract_image_urls(html_content: str) -> Set[str]:
    """Extract tất cả image URLs từ HTML"""
    urls = set()
    
    # Tìm tất cả img tags với src
    pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
    matches = re.findall(pattern, html_content, re.IGNORECASE)
    
    for match in matches:
        # Convert relative URLs to absolute
        if match.startswith('//'):
            match = 'https:' + match
        elif match.startswith('/'):
            match = f'https://{PROJECT_HOST}{match}'
        elif not match.startswith('http'):
            continue
        
        urls.add(match)
    
    return urls


def process_section(section_dir: str, section_key: str):
    """Process một section, download images và replace URLs"""
    print(f"\n{'='*60}")
    print(f"Processing: {section_key}")
    print(f"{'='*60}\n")
    
    content_dir = os.path.join(section_dir, f"content_{section_key}")
    assets_dir = os.path.join(section_dir, f"assets_{section_key}")
    
    if not os.path.exists(content_dir):
        print(f"No content directory: {content_dir}")
        return
    
    # Collect all image URLs từ tất cả files
    all_image_urls: Dict[str, str] = {}  # url -> local_filename
    
    print("Step 1: Collecting image URLs...")
    json_files = list(Path(content_dir).glob("*.json"))
    
    for json_file in json_files:
        print(f"  Reading: {json_file.name}")
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        html = data.get('html_content', '')
        urls = extract_image_urls(html)
        
        for url in urls:
            if url not in all_image_urls:
                # Generate filename from URL
                parsed = urlparse(url)
                filename = os.path.basename(parsed.path)
                
                # If no extension, try to detect from content
                if '.' not in filename:
                    filename = f"{hash(url) % 1000000}.png"
                
                all_image_urls[url] = filename
    
    print(f"\nFound {len(all_image_urls)} unique images")
    
    # Download images
    print("\nStep 2: Downloading images...")
    download_count = 0
    for url, filename in all_image_urls.items():
        save_path = os.path.join(assets_dir, filename)
        
        # Skip if already downloaded
        if os.path.exists(save_path):
            print(f"  Skip (exists): {filename}")
            continue
        
        if download_image(url, save_path):
            download_count += 1
    
    print(f"\nDownloaded {download_count} new images")
    
    # Replace URLs in HTML content
    print("\nStep 3: Updating HTML content with local URLs...")
    updated_files = 0
    
    for json_file in json_files:
        print(f"  Processing: {json_file.name}")
        
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        html = data.get('html_content', '')
        updated_html = html
        
        # Replace each image URL with local path
        for url, filename in all_image_urls.items():
            # Create relative path from content to assets
            relative_path = f"../assets_{section_key}/{filename}"
            
            # Replace all occurrences of this URL
            updated_html = updated_html.replace(url, relative_path)
        
        # Save updated content
        if updated_html != html:
            data['html_content'] = updated_html
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            updated_files += 1
    
    print(f"\nUpdated {updated_files} files with local image paths")
    print(f"✓ {section_key} completed!\n")


def main():
    base_dir = "C:\\Abivin\\data_docs03"
    
    sections = [
        ("user_guide", os.path.join(base_dir, "user_guide")),
        ("release_notes", os.path.join(base_dir, "release_notes")),
    ]
    
    for section_key, section_dir in sections:
        process_section(section_dir, section_key)
    
    print("="*60)
    print("ALL DONE!")
    print("="*60)


if __name__ == "__main__":
    main()

