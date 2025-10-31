# =============================================================
# File: update_changelog_with_odoo_links.py
# Cập nhật changelog với links tới Odoo articles
# =============================================================

import os
import re
import json
from typing import Dict

BASE_OUTPUT_DIR = r"C:\Abivin\data_docs03"
ODOO_BASE_URL = "https://test018.odoo.com"


def load_article_mapping() -> Dict[str, str]:
    """Load mapping từ title -> article ID"""
    mapping_file = os.path.join(BASE_OUTPUT_DIR, "release_notes", "odoo_article_mapping.json")
    
    if not os.path.exists(mapping_file):
        print(f"⚠️  Không tìm thấy mapping file: {mapping_file}")
        return {}
    
    with open(mapping_file, "r", encoding="utf-8") as f:
        mapping = json.load(f)
    
    print(f"✓ Loaded {len(mapping)} article mappings")
    return mapping


def title_to_url_slug(title: str) -> str:
    """Convert title to URL slug pattern for matching"""
    # "Dec 21, 2022 - Release Notes" -> "dec-21-2022-release-notes"
    slug = title.lower()
    slug = slug.replace(",", "").replace(" ", "-")
    # Remove "release note" -> "release notes" variations
    slug = slug.replace("release-note", "release-notes")
    return slug


def update_changelog_links(article_mapping: Dict[str, int]) -> bool:
    """Cập nhật links trong changelog.json"""
    
    changelog_file = os.path.join(BASE_OUTPUT_DIR, "release_notes", "content_release_notes", "changelog.json")
    
    with open(changelog_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    html_content = data.get("html_content", "")
    
    # Tìm tất cả links Abivin
    pattern = r'href="(https://docs\.abivin\.com/changelog/([^"]+))"([^>]*)>([^<]+)<'
    
    updated_count = 0
    
    def replace_func(match):
        nonlocal updated_count
        full_url = match.group(1)
        url_slug = match.group(2)
        extra_attrs = match.group(3)
        link_text = match.group(4)
        
        # Tìm title từ link text
        # "Dec 21, 2022 - Release Notes" -> tìm trong mapping
        
        # Try exact match first
        if link_text in article_mapping:
            article_id = article_mapping[link_text]
            new_url = f"https://{ODOO_BASE_URL}/odoo/articles/{article_id}"
            print(f"  ✓ Update: {link_text} -> article {article_id}")
            updated_count += 1
            return f'href="{new_url}"{extra_attrs}>{link_text}<'
        
        # Try with variations
        for title, article_id in article_mapping.items():
            # Check if it's a match
            if title in link_text or link_text in title:
                new_url = f"https://{ODOO_BASE_URL}/odoo/articles/{article_id}"
                print(f"  ✓ Update (fuzzy): {link_text} -> article {article_id}")
                updated_count += 1
                return f'href="{new_url}"{extra_attrs}>{link_text}<'
        
        # No match found
        print(f"  ⚠️  No mapping for: {link_text}")
        return match.group(0)
    
    new_html = re.sub(pattern, replace_func, html_content)
    
    if new_html != html_content:
        data["html_content"] = new_html
        
        with open(changelog_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Đã cập nhật {updated_count} links trong changelog")
        return True
    else:
        print("\nℹ️  Không có thay đổi")
        return False


def main():
    print("\n" + "="*60)
    print("🔧 CẬP NHẬT CHANGELOG VỚI ODEO LINKS")
    print("="*60)
    
    # Load mapping
    article_mapping = load_article_mapping()
    
    if not article_mapping:
        print("\n❌ Không có article mapping. Hãy chạy import trước!")
        return
    
    # Update changelog
    update_changelog_links(article_mapping)
    
    print("\n" + "="*60)
    print("✅ HOÀN TẤT!")
    print("="*60)


if __name__ == "__main__":
    main()


