"""
Re-download images for Release Notes từ files.readme.io
Vì script ban đầu đã replace URLs nhưng chưa download ảnh
"""
import sys
import requests
import json
import os
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def download_image(url, save_path):
    """Download image from URL"""
    try:
        print(f"  Downloading: {url}")
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            f.write(r.content)
        print(f"  ✓ Saved: {save_path}")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

# Check all release note pages for images
content_dir = Path("release_notes/content_release_notes")
assets_dir = Path("release_notes/assets_release_notes")

# Get all image references from HTML
import re

for json_file in content_dir.glob("*.json"):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html = data.get('html_content', '')
    
    # Find all image references (relative paths already in HTML)
    pattern = r'src=["\']\.\./assets_release_notes/([^"\']+)["\']'
    matches = re.findall(pattern, html)
    
    for filename in matches:
        # Construct original URL from filename
        # Based on the pattern: filename like "4f44de2-Screenshot_from_2023-03-09_09-32-12.png"
        # Original URL was: https://files.readme.io/4f44de2-Screenshot_from_2023-03-09_09-32-12.png
        original_url = f"https://files.readme.io/{filename}"
        local_path = assets_dir / filename
        
        if not local_path.exists():
            print(f"Downloading: {original_url}")
            download_image(original_url, str(local_path))
        else:
            print(f"  Skip (exists): {filename}")

print("\n✓ Done!")

