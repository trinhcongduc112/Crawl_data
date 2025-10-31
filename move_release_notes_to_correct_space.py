# =============================================================
# File: move_release_notes_to_correct_space.py
# Di chuyển release notes từ Space nhầm sang Space đúng
# =============================================================

import sys
import xmlrpc.client

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ===================== CẤU HÌNH =====================
ODOO_BASE_URL = "https://abivindocs1.odoo.com"
ODOO_DB_NAME = "abivindocs1"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "06f44edc309a7c6d558321f8809d2c72509e41df"

WRONG_SPACE = "[NHÁP] Dữ liệu Docs Import"
CORRECT_SPACE = "Tài liệu Abivin"

MODEL_ARTICLE = "knowledge.article"
# ====================================================

def odoo_login():
    print("\n🔐 Đang kết nối với Odoo...")
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
    
    # Tìm các Space
    print(f"\n📁 Tìm kiếm Space: '{CORRECT_SPACE}'...")
    correct_space_rec = odoo_call(
        models, uid, MODEL_ARTICLE, "search_read",
        [("name", "=", CORRECT_SPACE)], ["id"], limit=1
    )
    
    if not correct_space_rec:
        print(f"❌ Không tìm thấy Space '{CORRECT_SPACE}'")
        return
    
    correct_space_id = correct_space_rec[0]["id"]
    print(f"  ✓ Tìm thấy Space '{CORRECT_SPACE}' (ID: {correct_space_id})")
    
    print(f"\n📁 Tìm kiếm Space: '{WRONG_SPACE}'...")
    wrong_space_rec = odoo_call(
        models, uid, MODEL_ARTICLE, "search_read",
        [("name", "=", WRONG_SPACE)], ["id"], limit=1
    )
    
    if not wrong_space_rec:
        print(f"⚠️  Không tìm thấy Space '{WRONG_SPACE}'")
        return
    
    wrong_space_id = wrong_space_rec[0]["id"]
    print(f"  ✓ Tìm thấy Space '{WRONG_SPACE}' (ID: {wrong_space_id})")
    
    # Tìm tất cả articles trong Space nhầm
    print(f"\n🔍 Tìm các articles trong Space nhầm...")
    articles = odoo_call(
        models, uid, MODEL_ARTICLE, "search_read",
        [("parent_id", "=", wrong_space_id)],
        ["id", "name"], limit=100
    )
    
    print(f"  → Tìm thấy {len(articles)} articles cần di chuyển")
    
    if not articles:
        print("  ✓ Không có articles nào cần di chuyển")
        return
    
    # Di chuyển từng article
    success_count = 0
    print(f"\n🚀 Đang di chuyển articles sang Space đúng...\n")
    
    for idx, article in enumerate(articles, 1):
        try:
            print(f"[{idx}/{len(articles)}] Di chuyển: {article['name'][:60]}")
            
            # Di chuyển article
            odoo_call(
                models, uid, MODEL_ARTICLE, "write",
                [article['id']], {"parent_id": correct_space_id}
            )
            
            print(f"  ✓ Di chuyển thành công (ID: {article['id']})")
            success_count += 1
            
        except Exception as e:
            print(f"  ❌ Lỗi: {e}")
    
    print("\n" + "="*60)
    print(f"✅✅✅ HOÀN TẤT!")
    print(f"   Đã di chuyển: {success_count}/{len(articles)} articles")
    print(f"   Từ: '{WRONG_SPACE}'")
    print(f"   Sang: '{CORRECT_SPACE}'")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Đã hủy!")
    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback
        traceback.print_exc()






