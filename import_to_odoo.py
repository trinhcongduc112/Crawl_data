"""
Import scraped docs vào Odoo using XML-RPC API

Usage:
  python import_to_odoo.py
  
Requirements:
  - pip install odoorpc
"""

import os
import json
import sys
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

try:
    import odoorpc
except ImportError:
    print("Installing odoorpc...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "odoorpc"])
    import odoorpc


# Odoo Connection Info
ODOO_BASE_URL = "https://abivindocs1.odoo.com"
ODOO_DB_NAME = "abivindocs1"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "06f44edc309a7c6d558321f8809d2c72509e41df"


def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def connect_odoo():
    """Connect to Odoo using XML-RPC"""
    print("Connecting to Odoo...")
    
    try:
        import xmlrpc.client
        
        # Try XML-RPC authentication
        print("  Trying XML-RPC...")
        
        common = xmlrpc.client.ServerProxy(f'{ODOO_BASE_URL}/xmlrpc/2/common')
        
        # Test connection
        version_info = common.version()
        print(f"  Version: {version_info.get('server_version', 'Unknown')}")
        
        # Authenticate
        uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
        
        if uid:
            print(f"[OK] Authenticated! UID: {uid}")
            
            # Create session for models
            models = xmlrpc.client.ServerProxy(f'{ODOO_BASE_URL}/xmlrpc/2/object')
            
            # Return session-like object
            return {
                'uid': uid,
                'models': models,
                'db': ODOO_DB_NAME
            }
        else:
            print("[ERROR] Authentication failed")
            return None
            
    except Exception as e:
        print(f"[ERROR] Connection error: {e}")
        print(f"\nPossible issues:")
        print(f"  1. Network/Firewall blocking")
        print(f"  2. Odoo URL might need different protocol")
        print(f"  3. API key might be expired")
        return None


def get_or_create_article(odoo, title, html_content, slug=None):
    """
    Get or create an article in Odoo Knowledge
    Returns article ID
    """
    try:
        models = odoo['models']
        db = odoo['db']
        uid = odoo['uid']
        
        # Search for existing article
        article_ids = models.execute_kw(db, uid, ODOO_API_KEY,
            'knowledge.article', 'search', [[('name', '=', title)]],
            {'limit': 1})
        
        if article_ids and len(article_ids) > 0:
            # Update existing article
            models.execute_kw(db, uid, ODOO_API_KEY,
                'knowledge.article', 'write', [article_ids, {'body': html_content}])
            print(f"  Updated: {title}")
            return article_ids[0]
        
        # Create new article
        article_id = models.execute_kw(db, uid, ODOO_API_KEY,
            'knowledge.article', 'create', [{
                'name': title,
                'body': html_content,
            }])
        print(f"  Created: {title}")
        return article_id
        
    except Exception as e:
        print(f"  ✗ Error with article '{title}': {e}")
        return None


def import_file(odoo, json_file, collection_name="abivin-docs"):
    """Import a single JSON file"""
    print(f"\nImporting: {json_file.name}")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    title = data.get('title', 'Untitled')
    html_content = data.get('html_content', '')
    slug = data.get('old_slug', '')
    parent_slug = data.get('parent_slug')
    section = data.get('section', '')
    
    # Get or create article
    article_id = get_or_create_article(odoo, title, html_content, slug)
    
    if article_id:
        print(f"  ✓ Article ID: {article_id}")
        return article_id
    else:
        print(f"  ✗ Failed to create article")
        return None


def import_section(odoo, section_dir, section_key):
    """Import all files in a section"""
    print(f"\n{'='*60}")
    print(f"Importing section: {section_key}")
    print(f"{'='*60}")
    
    content_dir = os.path.join(section_dir, f"content_{section_key}")
    
    if not os.path.exists(content_dir):
        print(f"No content directory: {content_dir}")
        return
    
    json_files = list(Path(content_dir).glob("*.json"))
    print(f"Found {len(json_files)} files")
    
    article_ids = {}
    
    for json_file in json_files:
        article_id = import_file(odoo, json_file)
        if article_id:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            slug = data.get('old_slug', '')
            article_ids[slug] = article_id
    
    # Set parent-child relationships
    print("\nSetting parent-child relationships...")
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        slug = data.get('old_slug', '')
        parent_slug = data.get('parent_slug')
        
        if parent_slug and parent_slug in article_ids:
            article_id = article_ids.get(slug)
            parent_id = article_ids.get(parent_slug)
            
            if article_id and parent_id:
                try:
                    odoo.env['knowledge.article'].write([article_id], {
                        'parent_id': parent_id
                    })
                    print(f"  ✓ Set parent for {data.get('title', '')[:50]}")
                except Exception as e:
                    print(f"  ✗ Failed to set parent: {e}")
    
    print(f"\n✓ Completed: {section_key}")


def main():
    base_dir = "C:\\Abivin\\data_docs03"
    
    # Connect to Odoo
    odoo = connect_odoo()
    if not odoo:
        return
    
    # Import sections
    sections = [
        ("user_guide", os.path.join(base_dir, "user_guide")),
        ("release_notes", os.path.join(base_dir, "release_notes")),
    ]
    
    for section_key, section_dir in sections:
        try:
            import_section(odoo, section_dir, section_key)
        except Exception as e:
            print(f"\n✗ Error importing {section_key}: {e}")
    
    print("\n" + "="*60)
    print("IMPORT COMPLETED!")
    print("="*60)


if __name__ == "__main__":
    main()

