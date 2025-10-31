"""
Test connection to Odoo
"""

import xmlrpc.client

ODOO_BASE_URL = "https://test018.odoo.com" 
ODOO_DB_NAME = "test018"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "3f623d85508792f81af911610db742d67a5d1845"

print("Testing Odoo connection...")
print(f"URL: {ODOO_BASE_URL}")
print(f"User: {ODOO_USER}\n")

try:
    # Test common endpoint
    common = xmlrpc.client.ServerProxy(f'{ODOO_BASE_URL}/xmlrpc/2/common')
    version_info = common.version()
    print(f"✓ Version info: {version_info}")
    
    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if uid:
        print(f"✓ Authenticated! UID: {uid}")
    else:
        print("✗ Authentication failed")
        print("  Check your API key or credentials")
        
except Exception as e:
    print(f"✗ Connection failed: {e}")



