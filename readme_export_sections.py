
"""
ReadMe.io → output sections (User Guide, Release Notes) for Odoo importer
Author: Abivin
Python: 3.8+

Usage:
  # Env (khuyến nghị)
  set README_API_KEY=xxxxx
  set README_VERSION=latest

  # Chạy cơ bản (mặc định 2 mục: user-guide, release-notes)
  python readme_export_sections.py --out "C:\Abivin\data_docs03"

  # Tuỳ biến mapping category:
  #   --map "<cat_slug>:<section_key>:<root_seg>,<cat_slug2>:<section_key2>:<root_seg2>"
  python readme_export_sections.py --out "C:\Abivin\data_docs03" ^
    --map "user-guide:user_guide:user-guide,release-notes:release_notes:release-notes"

Notes:
- Script chỉ export nội dung; importer sẽ lo phân cấp/thứ tự/asset upload.
- Nếu ReadMe trả 'html' thì dùng trực tiếp; nếu không, sẽ fallback sang markdown -> HTML tối giản (pre).
"""

import os
import re
import json
import time
import argparse
import requests
from typing import Dict, List, Tuple

# ===================== Config mặc định =====================
API_BASE_DEFAULT = "https://dash.readme.com/api/v1"
PROJECT_HOST_DEFAULT = "docs.abivin.com"  # ghi metadata origin_host/origin_url

# Mặc định export 2 category: user-guide & release-notes
DEFAULT_MAP = [
    # (cat_slug_on_ReadMe, section_key_out, section_root_seg_for_path)
    ("user-guide",    "user_guide",    "user-guide"),
    ("release-notes", "release_notes", "release-notes"),
]
# ===========================================================


# ---------------- FS helpers ----------------
def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def write_json(path: str, obj: dict) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def path_to_slug(path: str) -> str:
    """Convert a URL-like path to a filesystem-safe slug."""
    base = (path or "/").strip("/").replace("/", "__")
    return base or "index"


def to_segments_from_path(path: str, section_root: str) -> List[str]:
    parts = [x for x in (path or "").strip("/").split("/") if x]
    if section_root in parts:
        i = parts.index(section_root)
        return parts[i:-1]  # bỏ segment cuối (doc slug)
    return parts[:-1]


def md_to_html_fallback(md: str) -> str:
    """If ReadMe doesn't return html, fallback to a minimal pre block."""
    if not md:
        return ""
    # Bạn có thể thay bằng markdown2.markdown(md) nếu muốn HTML chuẩn hơn
    return f"<div class='md-body'><pre>{md}</pre></div>"


# ---------------- HTTP / ReadMe API ----------------
def make_session(api_key: str, version: str, api_base: str) -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "Accept": "application/json",
        "x-readme-version": version or "latest",
    })
    s.auth = (api_key, "")  # Basic auth: username=key, password=""
    s.api_base = api_base.rstrip("/")
    return s


def api_get(session: requests.Session, path: str, **params):
    url = f"{session.api_base}{path}"
    r = session.get(url, params=params or None, timeout=30)
    if r.status_code >= 400:
        raise RuntimeError(f"GET {url} failed {r.status_code}: {r.text[:200]}")
    return r.json()


def fetch_all_categories(session: requests.Session) -> List[dict]:
    return api_get(session, "/categories")


def fetch_docs_in_category(session: requests.Session, cat_slug: str, page: int, per_page: int = 100) -> List[dict]:
    return api_get(session, f"/categories/{cat_slug}/docs", page=page, perPage=per_page)


def fetch_doc_detail(session: requests.Session, doc_slug: str) -> dict:
    return api_get(session, f"/docs/{doc_slug}")


# ---------------- Core export logic ----------------
def export_section(session: requests.Session,
                   out_base: str,
                   project_host: str,
                   section_key: str,
                   cat_slug: str,
                   root_seg: str) -> Tuple[int, int]:
    """
    Export a single ReadMe category into output folder.
    Returns (total_docs, created_files)
    """
    base_folder = os.path.join(out_base, section_key)
    content_dir = os.path.join(base_folder, f"content_{section_key}")
    assets_dir = os.path.join(base_folder, f"assets_{section_key}")  # để sẵn cho importer
    ensure_dir(content_dir)
    ensure_dir(assets_dir)

    # để hạn chế ghi đè vô ích, load mapping cũ (nếu cần)
    mapping_fp = os.path.join(base_folder, f"url_mapping_{section_key}.json")
    old_map: Dict[str, str] = {}
    if os.path.exists(mapping_fp):
        try:
            old_map = json.load(open(mapping_fp, "r", encoding="utf-8"))
        except Exception:
            old_map = {}

    page = 1
    total_docs = 0
    created_files = 0
    order_idx = 0
    url_map: Dict[str, str] = {}

    while True:
        items = fetch_docs_in_category(session, cat_slug, page=page)
        if not items:
            break

        for item in items:
            slug = item.get("slug")
            if not slug:
                continue

            detail = fetch_doc_detail(session, slug)
            html = detail.get("html") or md_to_html_fallback(detail.get("body") or "")
            # ReadMe doc path (nếu không có, tự hợp thành từ cat/slug)
            path = detail.get("path") or f"{cat_slug}/{slug}"
            parents = to_segments_from_path(path, root_seg)
            full_slug = path_to_slug(path)

            order_idx += 1
            doc = {
                "origin_url": f"https://{project_host}/{path}".rstrip("/"),
                "origin_host": project_host,
                "collection": "abivin-docs",
                "section": section_key,
                "parents_segments": parents,
                "order_index": order_idx,
                "old_slug": full_slug,
                "new_slug": full_slug,
                "title": detail.get("title") or slug,
                "html_content": html,
                "tags": detail.get("tags") or [],
                "lang": detail.get("language") or "en",
                "status": "ready",
                "updated_at": detail.get("updatedAt") or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "scraped": True,
                "_readme_doc_slug": slug,
                "_readme_category": (detail.get("category") or {}).get("slug") or cat_slug,
            }

            out_fp = os.path.join(content_dir, f"{full_slug}.json")
            url_map[doc["origin_url"]] = out_fp

            # chỉ ghi nếu file chưa tồn tại hoặc nội dung thay đổi
            need_write = True
            if os.path.exists(out_fp):
                try:
                    old = json.load(open(out_fp, "r", encoding="utf-8"))
                    # so sánh nhẹ: title + updated_at + độ dài html_content
                    if (old.get("title") == doc["title"]
                        and old.get("updated_at") == doc["updated_at"]
                        and len(old.get("html_content") or "") == len(doc["html_content"])):
                        need_write = False
                except Exception:
                    need_write = True

            if need_write:
                write_json(out_fp, doc)
                created_files += 1

            total_docs += 1

        page += 1

    write_json(mapping_fp, url_map)
    print(f"[OK] {section_key} (category '{cat_slug}') → {total_docs} docs "
          f"(wrote {created_files}, skipped {total_docs - created_files}) "
          f"→ {content_dir}")
    return total_docs, created_files


def parse_map_arg(map_arg: str) -> List[Tuple[str, str, str]]:
    """
    Parse --map "cat:section:root,cat2:section2:root2"
    """
    plan = []
    for part in map_arg.split(","):
        part = part.strip()
        if not part:
            continue
        bits = [b.strip() for b in part.split(":")]
        if len(bits) != 3:
            raise ValueError(f"Invalid map item: {part}. Expect cat_slug:section_key:root_seg")
        plan.append((bits[0], bits[1], bits[2]))
    return plan


# ---------------- CLI ----------------
def main():
    ap = argparse.ArgumentParser(description="Export ReadMe.io categories to output structure for Odoo importer")
    ap.add_argument("--out", required=True, help="Base output dir, e.g. C:\\Abivin\\data_docs03")
    ap.add_argument("--api-base", default=API_BASE_DEFAULT, help=f"ReadMe API base (default: {API_BASE_DEFAULT})")
    ap.add_argument("--project-host", default=PROJECT_HOST_DEFAULT, help=f"Origin host meta (default: {PROJECT_HOST_DEFAULT})")
    ap.add_argument("--api-key", default=os.getenv("README_API_KEY"), help="ReadMe API key (env README_API_KEY if omitted)")
    ap.add_argument("--version", default=os.getenv("README_VERSION", "latest"), help="ReadMe docs version (env README_VERSION or 'latest')")
    ap.add_argument("--map", default="", help="Mapping: 'cat_slug:section_key:root_seg,...' (override defaults)")
    args = ap.parse_args()

    if not args.api_key:
        raise SystemExit("Missing API key. Set --api-key or env README_API_KEY.")

    # Build PLAN
    if args.map:
        plan = parse_map_arg(args.map)
    else:
        plan = DEFAULT_MAP[:]  # copy

    # Warm up session
    sess = make_session(args.api_key, args.version, args.api_base)

    # Validate categories exist (optional: fetch & warn)
    try:
        cats = fetch_all_categories(sess)
        cat_slugs = {c.get("slug") for c in cats if "slug" in c}
    except Exception as e:
        print(f"[WARN] Could not list categories (will try anyway): {e}")
        cat_slugs = set()

    ensure_dir(args.out)
    summary = []

    for cat_slug, section_key, root_seg in plan:
        if cat_slugs and cat_slug not in cat_slugs:
            print(f"[WARN] Category '{cat_slug}' not found on ReadMe; skipping.")
            continue
        try:
            total, wrote = export_section(sess, args.out, args.project_host, section_key, cat_slug, root_seg)
            summary.append((section_key, total, wrote))
        except Exception as e:
            print(f"[ERR] Export {section_key} ({cat_slug}) failed: {e}")

    # Summary print
    if summary:
        print("\n=== SUMMARY ===")
        for section_key, total, wrote in summary:
            print(f"{section_key}: {total} docs (wrote {wrote}, skipped {total - wrote})")
    else:
        print("\nNo sections exported.")


if __name__ == "__main__":
    main()
