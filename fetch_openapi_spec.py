"""
Fetch OpenAPI spec từ ReadMe và convert sang HTML tĩnh cho Odoo
"""
import requests
import json
import os
from pathlib import Path

# Cấu hình
README_PROJECT = "abivin-docs"
README_HOST = "docs.abivin.com"

def fetch_openapi_spec():
    """Lấy OpenAPI spec từ ReadMe"""
    try:
        # Thử lấy từ ReadMe API reference
        url = f"https://{README_HOST}/reference/openapi.json"
        print(f"Đang lấy OpenAPI spec từ: {url}")
        
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            try:
                spec = response.json()
                print(f"✅ Lấy được OpenAPI spec!")
                print(f"   Title: {spec.get('info', {}).get('title', 'N/A')}")
                print(f"   Version: {spec.get('info', {}).get('version', 'N/A')}")
                print(f"   Paths: {len(spec.get('paths', {}))}")
                
                # Lưu spec file
                with open('openapi_spec.json', 'w', encoding='utf-8') as f:
                    json.dump(spec, f, indent=2, ensure_ascii=False)
                
                print(f"✅ Đã lưu vào: openapi_spec.json")
                return spec
            except json.JSONDecodeError as e:
                print(f"⚠️  Không parse được JSON: {e}")
                print(f"   Content preview: {response.text[:500]}")
        else:
            print(f"❌ HTTP {response.status_code}: {response.text[:200]}")
            
            # Thử URL khác
            alt_url = f"https://{README_HOST}/reference"
            print(f"\nThử URL khác: {alt_url}")
            print(f"Vui lòng truy cập {alt_url} và kiểm tra nếu có link tải OpenAPI spec")
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        
    return None


def convert_spec_to_html(spec_path='openapi_spec.json'):
    """Convert OpenAPI spec sang HTML đơn giản"""
    if not os.path.exists(spec_path):
        print(f"❌ Không tìm thấy file: {spec_path}")
        return
    
    print(f"\n{'='*60}")
    print("🔄 Đang convert OpenAPI spec sang HTML...")
    print(f"{'='*60}\n")
    
    # TODO: Implement conversion logic here
    print("⏳ Tính năng này đang được phát triển...")
    

if __name__ == "__main__":
    spec = fetch_openapi_spec()
    if spec:
        convert_spec_to_html()


