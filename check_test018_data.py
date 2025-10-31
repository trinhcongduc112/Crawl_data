# =============================================================
# File: check_test018_data.py
# Kiểm tra dữ liệu trong môi trường chính test018.odoo.com
# =============================================================

import sys
import xmlrpc.client

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ===================== CẤU HÌNH CHÍNH =====================
ODOO_BASE_URL = "https://test018.odoo.com"
ODOO_DB_NAME = "test018"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "3f623d85508792f81af911610db742d67a5d1845"

SPACE_NAME = "Tài liệu Abivin"
MODEL_ARTICLE = "knowledge.article"
# ====================================================

def odoo_login():
    print("\n🔐 Đang kết nối với Odoo (test018.odoo.com)...")
    common = xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/common")
    
    try:
        version_info = common.version()
        print(f"  ✓ Server version: {version_info.get('server_version', 'Unknown')}")
    except Exception as e:
        print(f"  ✗ Lỗi kiểm tra phiên bản: {e}")
    
    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if not uid:
        raise SystemExit("❌ Xác thực Odoo thất bại.")
    print(f"  ✓ Đã đăng nhập vào Odoo với user ID: {uid}")
    return xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/object"), uid


def odoo_call(models, uid, model, method, *args, **kwargs):
    return models.execute_kw(
        ODOO_DB_NAME, uid, ODOO_API_KEY,
        model, method, list(args), kwargs if kwargs else {}
    )


def main():
    models, uid = odoo_login()
    
    # Tìm Space
    print(f"\n📁 Tìm kiếm Space: '{SPACE_NAME}'...")
    space_rec = odoo_call(
        models, uid, MODEL_ARTICLE, "search_read",
        [("name", "=", SPACE_NAME)], ["id"], limit=1
    )
    
    if not space_rec:
        print(f"❌ Không tìm thấy Space '{SPACE_NAME}'")
        print(f"\n💡 Space '{SPACE_NAME}' chưa tồn tại trong test018.odoo.com")
        print(f"   Cần import dữ liệu vào môi trường chính này!")
        return
    
    space_id = space_rec[0]["id"]
    print(f"  ✓ Tìm thấy Space '{SPACE_NAME}' (ID: {space_id})")
    
    # Đếm số articles trong Space
    print(f"\n📊 Đang đếm articles trong Space...")
    article_count = odoo_call(
        models, uid, MODEL_ARTICLE, "search_count",
        [("parent_id", "=", space_id)]
    )
    
    print(f"  ✓ Có {article_count} articles trong Space '{SPACE_NAME}'")
    
    # Lấy danh sách 20 articles đầu tiên để xem
    print(f"\n📋 Danh sách 20 articles đầu tiên:")
    articles = odoo_call(
        models, uid, MODEL_ARTICLE, "search_read",
        [("parent_id", "=", space_id)],
        ["id", "name"], limit=20
    )
    
    for idx, article in enumerate(articles, 1):
        print(f"  {idx}. [{article['id']}] {article['name'][:60]}")
    
    # Phân loại articles theo section
    print(f"\n📊 Phân tích dữ liệu theo section...")
    
    # Đếm release notes
    release_notes = odoo_call(
        models, uid, MODEL_ARTICLE, "search_read",
        [("parent_id", "=", space_id), ("name", "ilike", "Release Note")],
        ["id"], limit=1000
    )
    
    print(f"  📝 Release Notes: {len(release_notes)} articles")
    
    # Đếm user guide (thử tìm các patterns thường thấy)
    print(f"\n💡 Kiểm tra thêm dữ liệu...")
    
    all_articles = odoo_call(
        models, uid, MODEL_ARTICLE, "search_read",
        [("parent_id", "=", space_id)],
        ["id"], limit=1000
    )
    
    print(f"  📦 Tổng cộng: {len(all_articles)} articles")
    
    print("\n" + "="*60)
    print(f"✅ KẾT QUẢ KIỂM TRA")
    print(f"   Space: '{SPACE_NAME}' (ID: {space_id})")
    print(f"   Tổng articles: {len(all_articles)}")
    print(f"   Release Notes: {len(release_notes)}")
    print("="*60)
    
    if len(all_articles) < 100:
        print("\n⚠️  Dữ liệu chưa đầy đủ trong môi trường chính!")
        print(f"   Hiện chỉ có {len(all_articles)} articles")
        print(f"   Cần import thêm dữ liệu vào đây.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Đã hủy!")
    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback
        traceback.print_exc()






