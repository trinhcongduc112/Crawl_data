"""
Replace image URLs in HTML với local paths
- Tìm tất cả URLs files.readme.io
- Thay thế bằng relative paths tới assets folder
"""

import os
import json
import re
import sys
from pathlib import Path

# Fix encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


def replace_image_urls(html_content: str, section_key: str) -> str:
    """
    Replace tất cả image URLs với local paths
    From: https://files.readme.io/abc123.png
    To: ../assets_user_guide/abc123.png
    """
    
    # Pattern to find image URLs
    pattern = r'src="(https://files\.readme\.io/[^"]+)"'
    
    def replace_url(match):
        url = match.group(1)
        
        # Extract filename from URL
        filename = url.split('/')[-1]
        
        # Create relative path
        relative_path = f"../assets_{section_key}/{filename}"
        
        return f'src="{relative_path}"'
    
    # Replace all URLs
    updated_html = re.sub(pattern, replace_url, html_content)
    
    return updated_html


def process_section(section_dir: str, section_key: str):
    """Process một section"""
    print(f"\n{'='*60}")
    print(f"Processing: {section_key}")
    print(f"{'='*60}\n")
    
    content_dir = os.path.join(section_dir, f"content_{section_key}")
    
    if not os.path.exists(content_dir):
        print(f"No content directory: {content_dir}")
        return
    
    json_files = list(Path(content_dir).glob("*.json"))
    print(f"Found {len(json_files)} files")
    
    updated_count = 0
    
    for json_file in json_files:
        print(f"  Processing: {json_file.name}")
        
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        html = data.get('html_content', '')
        
        # Replace image URLs
        updated_html = replace_image_urls(html, section_key)
        
        if updated_html != html:
            data['html_content'] = updated_html
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            updated_count += 1
    
    print(f"\n✓ Updated {updated_count} files with local image paths")
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
    print("Images now use local paths!")
    print("="*60)


if __name__ == "__main__":
    main()



