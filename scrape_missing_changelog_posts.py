# =============================================================
# File: scrape_missing_changelog_posts.py
# Tìm và cào (scrape) các bài changelog còn thiếu, lưu JSON + ảnh
# =============================================================

import os
import re
import json
import time
import requests
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Tuple

BASE_OUTPUT_DIR = r"C:\Abivin\data_docs03"
ORIGIN_HOST = "docs.abivin.com"

CONTENT_DIR = os.path.join(BASE_OUTPUT_DIR, "release_notes", "content_release_notes")
ASSETS_DIR = os.path.join(BASE_OUTPUT_DIR, "release_notes", "assets_release_notes")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}


def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def read_json(fp: str) -> dict:
    with open(fp, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(fp: str, obj: dict) -> None:
    ensure_dir(os.path.dirname(fp))
    with open(fp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def slug_from_url(url: str) -> str:
    # https://docs.abivin.com/changelog/dec-21-2022-release-notes -> changelog__dec-21-2022-release-notes
    path = urlparse(url).path.strip("/")
    return path.replace("/", "__")


def list_missing_post_urls() -> List[str]:
    """Scrape TẤT CẢ các pages release notes từ page 1-20"""
    all_urls = []
    
    # Tìm tất cả các pages
    for page in range(1, 21):
        if page == 1:
            changelog_url = "https://docs.abivin.com/changelog"
        else:
            changelog_url = f"https://docs.abivin.com/changelog?page={page}"
        
        print(f"Fetching page {page}: {changelog_url}")
        try:
            html = fetch_html(changelog_url)
        except Exception as e:
            print(f"  ⚠️  Không thể fetch page {page}: {e}")
            break
        
        # Find all links to changelog posts on this page
        urls = re.findall(r'href=["\'](https://docs\.abivin\.com/changelog/[^"\']+)["\']', html)
        all_urls.extend(urls)
        
        # Nếu không tìm thấy link nào có nghĩa là hết rồi
        if not urls:
            print(f"  ✓ Đã hết dữ liệu ở page {page}")
            break
    
    missing: List[str] = []
    for u in set(all_urls):  # Remove duplicates
        slug = slug_from_url(u)
        out_fp = os.path.join(CONTENT_DIR, f"{slug}.json")
        if not os.path.exists(out_fp):
            missing.append(u)
    
    return sorted(missing)


def download_binary(url: str, save_path: str) -> bool:
    try:
        ensure_dir(os.path.dirname(save_path))
        r = requests.get(url, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(r.content)
            return True
        return False
    except Exception:
        return False


def fetch_html(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.text


def extract_title(html: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r"<.*?>", "", m.group(1)).strip()
    # fallback: page <title>
    m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r"<.*?>", "", m.group(1)).strip()
    return "Release Notes"


def rewrite_images_and_collect(html: str) -> Tuple[str, List[Tuple[str, str]]]:
    """Rewrite files.readme.io -> ../assets_release_notes/<filename> and collect (url, filename)."""
    downloads: List[Tuple[str, str]] = []

    def repl(m):
        src = m.group(1)
        # keep filename
        filename = os.path.basename(urlparse(src).path)
        if filename:
            downloads.append((src, filename))
            return f'src="../assets_release_notes/{filename}"'
        return m.group(0)

    # handle both single and double quotes
    pattern = r'src=["\'](https?://files\.readme\.io/[^"\']+)["\']'
    new_html = re.sub(pattern, repl, html)
    return new_html, downloads


def scrape_one(url: str, order_index: int) -> None:
    print(f"  - Fetching: {url}")
    raw_html = fetch_html(url)

    title = extract_title(raw_html)
    html, imgs = rewrite_images_and_collect(raw_html)

    # download images
    downloaded = 0
    for img_url, filename in imgs:
        dest = os.path.join(ASSETS_DIR, filename)
        if not os.path.exists(dest):
            if download_binary(img_url, dest):
                downloaded += 1
    if imgs:
        print(f"    images: {downloaded}/{len(imgs)} downloaded")

    # build JSON structure aligned with existing files
    slug = slug_from_url(url)
    doc = {
        "origin_url": url,
        "origin_host": ORIGIN_HOST,
        "collection": "abivin-docs",
        "section": "release_notes",
        "parents_segments": ["changelog"],
        "parent_slug": None,
        "order_index": order_index,
        "old_slug": slug,
        "new_slug": slug,
        "title": title,
        "html_content": html,
        "tags": [],
        "lang": "en",
        "status": "ready",
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "scraped": True,
    }

    out_fp = os.path.join(CONTENT_DIR, f"{slug}.json")
    write_json(out_fp, doc)
    print(f"    ✓ Wrote {out_fp}")


def main():
    ensure_dir(CONTENT_DIR)
    ensure_dir(ASSETS_DIR)

    missing = list_missing_post_urls()
    if not missing:
        print("No missing posts.")
        return

    print(f"Found {len(missing)} missing changelog posts.")
    for idx, url in enumerate(missing, 1):
        scrape_one(url, order_index=1000 + idx)  # large index to keep order stable


if __name__ == "__main__":
    main()

