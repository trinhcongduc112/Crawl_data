"""
Fix images CSS để hiển thị đúng trong Odoo
- Thêm responsive styles cho images
- Thêm max-width và height: auto
"""

import os
import json
import re
import sys
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


def fix_image_css(html_content: str) -> str:
    """
    Fix images trong HTML để responsive
    - Thêm max-width: 100% và height: auto cho tất cả images
    """
    
    # Pattern để tìm img tags
    def replace_img(match):
        img_tag = match.group(0)
        
        # Check if already has style attribute
        if 'style=' in img_tag:
            # Add to existing style
            img_tag = re.sub(
                r'style="([^"]*)"',
                lambda m: f'style="{m.group(1)} max-width:100%; height:auto;"',
                img_tag
            )
        else:
            # Add new style attribute
            img_tag = re.sub(
                r'(<img[^>]*?)(/?>)',
                r'\1 style="max-width:100%; height:auto;"\2',
                img_tag,
                flags=re.IGNORECASE
            )
        
        return img_tag
    
    # Replace all img tags
    fixed_html = re.sub(
        r'<img[^>]+/?>',
        replace_img,
        html_content,
        flags=re.IGNORECASE
    )
    
    return fixed_html


def process_section(section_dir: str, section_key: str):
    """Process một section, fix CSS cho images"""
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
        
        # Fix images
        fixed_html = fix_image_css(html)
        
        if fixed_html != html:
            data['html_content'] = fixed_html
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            updated_count += 1
    
    print(f"\n✓ Updated {updated_count} files")
    print(f"✓ {section_key} completed!\n")


def main():
    base_dir = "C:\\Abivin\\data_docs03"
    
    sections = [
        ("user_guide", os.path.join(base_dir, "user_guide")),
        ("release_notes", os.path.join(base_dir, "release_notes")),
        ("developer_guide", os.path.join(base_dir, "developer_guide")),
    ]
    
    for section_key, section_dir in sections:
        process_section(section_dir, section_key)
    
    print("="*60)
    print("ALL DONE!")
    print("Images are now responsive for Odoo!")
    print("="*60)


if __name__ == "__main__":
    main()

