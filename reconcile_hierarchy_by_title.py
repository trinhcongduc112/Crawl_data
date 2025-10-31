import os
import glob
import json
import sys
import time
import re
import xmlrpc.client
from typing import Dict, Tuple

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


def odoo_write(models, uid, model, ids, vals):
    if not isinstance(ids, list):
        ids = [ids]
    return odoo_call(models, uid, model, "write", ids, vals)


def ensure_space(models, uid, space_name):
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name", "=", space_name)], ["id"], limit=1)
    if not rec:
        raise SystemExit("Space not found")
    return rec[0]["id"]


def ensure_category(models, uid, parent_id, category_name):
    rec = odoo_search(models, uid, MODEL_ARTICLE, [("name", "=", category_name), ("parent_id", "=", parent_id)], ["id"], limit=1)
    if rec:
        return rec[0]["id"]
    return odoo_call(models, uid, MODEL_ARTICLE, "create", [{"name": category_name, "parent_id": parent_id}])


def normalize_title(s: str) -> str:
    if not s:
        return ""
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = s.replace("’", "'")
    s = s.replace("–", "-")
    s = s.replace("—", "-")
    return s


def load_title_to_category_map() -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    sections = {
        "user_guide": (os.path.join(BASE_OUTPUT_DIR, "user_guide", "content_user_guide"), "User Guide"),
        "release_notes": (os.path.join(BASE_OUTPUT_DIR, "release_notes", "content_release_notes"), "Release Notes"),
        "developer_guide": (os.path.join(BASE_OUTPUT_DIR, "developer_guide", "content_developer_guide"), "Developer Guide"),
    }
    for _, (content_dir, cat) in sections.items():
        if not os.path.isdir(content_dir):
            continue
        for jp in glob.glob(os.path.join(content_dir, "*.json")):
            try:
                with open(jp, "r", encoding="utf-8") as f:
                    doc = json.load(f)
                title = normalize_title(doc.get("title"))
                if title:
                    mapping[title] = cat
            except Exception:
                pass
    return mapping


def main():
    if sys.platform == 'win32':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    models, uid = odoo_login()
    space_id = ensure_space(models, uid, SPACE_NAME)

    # Ensure top categories
    cat_ids: Dict[str, int] = {}
    for cat in ["User Guide", "Release Notes", "Developer Guide"]:
        cat_ids[cat] = ensure_category(models, uid, space_id, cat)

    title_to_cat = load_title_to_category_map()

    # Fetch all articles under space and under categories
    root_articles = odoo_search(models, uid, MODEL_ARTICLE, [("parent_id", "=", space_id)], ["id", "name"], limit=0)

    moved = 0
    already_ok = 0
    unmatched = 0

    for rec in root_articles:
        name = rec.get("name", "")
        key = normalize_title(name)
        target_cat_name = title_to_cat.get(key)
        if not target_cat_name:
            unmatched += 1
            continue
        target_parent_id = cat_ids[target_cat_name]
        try:
            odoo_write(models, uid, MODEL_ARTICLE, [rec["id"]], {"parent_id": target_parent_id})
            moved += 1
        except Exception:
            # If write fails, count as unmatched for manual review
            unmatched += 1

    print(f"moved={moved} unmatched={unmatched} already_ok={already_ok}")


if __name__ == "__main__":
    main()





