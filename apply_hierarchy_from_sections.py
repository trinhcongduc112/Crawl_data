import os
import glob
import json
import sys
import time
import xmlrpc.client

BASE_OUTPUT_DIR = r"C:\Abivin\data_docs03"

ODOO_BASE_URL = "https://test018.odoo.com"
ODOO_DB_NAME = "test018"
ODOO_USER = "trinhcongduc0112@gmail.com"
ODOO_API_KEY = "3f623d85508792f81af911610db742d67a5d1845"

SPACE_NAME = "Tài liệu Abivin"
MODEL_ARTICLE = "knowledge.article"


def odoo_login():
    common = xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/common")
    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if not uid:
        raise SystemExit("Auth failed")
    return xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/object"), uid


def odoo_call(models, uid, model, method, *args, **kwargs):
    for _ in range(3):
        try:
            return models.execute_kw(ODOO_DB_NAME, uid, ODOO_API_KEY, model, method, args, kwargs)
        except Exception:
            time.sleep(1)
    raise RuntimeError(f"RPC failed: {model}.{method}")


def odoo_search(models, uid, model, domain, fields=None, limit=0):
    kwargs = {}
    if fields:
        kwargs["fields"] = fields
    if limit:
        kwargs["limit"] = limit
    return odoo_call(models, uid, model, "search_read", domain, **kwargs)


def odoo_create(models, uid, model, vals):
    return odoo_call(models, uid, model, "create", vals)


def odoo_write(models, uid, model, ids, vals):
    if not isinstance(ids, list):
        ids = [ids]
    return odoo_call(models, uid, model, "write", ids, vals)


def ensure_space(models, uid, space_name):
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name", "=", space_name)], ["id"], limit=1)
    if rec:
        return rec[0]["id"]
    return odoo_create(models, uid, MODEL_ARTICLE, {"name": space_name, "body": "<p>Imported docs</p>"})


def ensure_category(models, uid, parent_id, category_name):
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name", "=", category_name), ("parent_id", "=", parent_id)], ["id"], limit=1)
    if rec:
        return rec[0]["id"]
    return odoo_create(models, uid, MODEL_ARTICLE, {"name": category_name, "parent_id": parent_id})


def load_docs_with_sections():
    all_docs = []
    sections = {
        "user_guide": {
            "content": os.path.join(BASE_OUTPUT_DIR, "user_guide", "content_user_guide"),
            "category": "User Guide",
        },
        "release_notes": {
            "content": os.path.join(BASE_OUTPUT_DIR, "release_notes", "content_release_notes"),
            "category": "Release Notes",
        },
        "developer_guide": {
            "content": os.path.join(BASE_OUTPUT_DIR, "developer_guide", "content_developer_guide"),
            "category": "Developer Guide",
        },
    }
    for key, info in sections.items():
        content_dir = info["content"]
        if not os.path.isdir(content_dir):
            continue
        for jp in sorted(glob.glob(os.path.join(content_dir, "*.json"))):
            try:
                with open(jp, "r", encoding="utf-8") as f:
                    doc = json.load(f)
                title = doc.get("title")
                if not title:
                    continue
                all_docs.append({
                    "title": title,
                    "section_category": info["category"],
                })
            except Exception:
                pass
    return all_docs


def main():
    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)

    # Create top-level categories
    cat_ids = {}
    for cat_name in ["User Guide", "Release Notes", "Developer Guide"]:
        cat_ids[cat_name] = ensure_category(models, uid, space_id, cat_name)

    docs = load_docs_with_sections()

    moved = 0
    skipped = 0

    # Move articles currently under space into section categories by title match
    for doc in docs:
        title = doc["title"]
        category_id = cat_ids.get(doc["section_category"]) or space_id
        existing = odoo_search(
            models, uid, MODEL_ARTICLE,
            [("name", "=", title), ("parent_id", "=", space_id)], ["id"], limit=1
        )
        if existing:
            try:
                odoo_write(models, uid, MODEL_ARTICLE, [existing[0]["id"]], {"parent_id": category_id})
                moved += 1
            except Exception:
                skipped += 1
        else:
            skipped += 1

    print(f"Moved: {moved}, Skipped: {skipped}")


if __name__ == "__main__":
    if sys.platform == 'win32':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass
    main()





