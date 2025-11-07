# =============================================================
# File: fix_images_in_space.py  (Odoo 19 - Post-process images)
# Sửa hiển thị ảnh & (tuỳ chọn) mirror ảnh ngoài vào ir.attachment
#
# Tính năng:
#  - Mirror ảnh ngoài (--mirror) -> /web/image/...&width=<imgw>
#  - Responsive + fit khung figure (max-width = --maxw)
#  - Click-to-zoom: gắn data-abivin-zoom="1" + data-zoom-src
#  - Idempotent: không bọc <figure> lặp, không re-style ảnh đã xử lý
#  - "Brutal mode": bắt mọi biến thể URL ReadMe (src, srcset, source[srcset],
#                   data-src, data-original, href, background-image, URL fallback)
# =============================================================

import re
import sys
import os
import base64
import argparse
import xmlrpc.client
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
import requests  # pip install requests

# ===== CẤU HÌNH MẶC ĐỊNH (có thể override qua --args) =====
ODOO_BASE_URL = "https://test018.odoo.com"
ODOO_DB_NAME  = "test018"
ODOO_USER     = "trinhcongduc0112@gmail.com"
ODOO_API_KEY  = "3f623d85508792f81af911610db742d67a5d1845"

SPACE_NAME      = "docs_abivin"  # Tên Space (nếu có field space)
ROOT_ARTICLE    = None                  # Tên bài gốc nếu không có field space
MAX_FIGURE_W    = 960                   # px
RESPONSIVE_W    = 1200                  # px cho tham số /web/image?width=
MIRROR_EXTERNAL = False                 # True để mirror ảnh ngoài vào Odoo

MODEL_ARTICLE    = "knowledge.article"
MODEL_ATTACHMENT = "ir.attachment"

SPACE_FIELD = None
SPACE_MODEL = None

# ------------- Odoo Core -------------
def odoo_login():
    common = xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/common")
    uid = common.authenticate(ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY, {})
    if not uid:
        raise SystemExit("❌ Không đăng nhập được Odoo (API key/quyền?).")
    print(f"🔐 Đăng nhập Odoo OK (uid={uid})")
    return xmlrpc.client.ServerProxy(f"{ODOO_BASE_URL}/xmlrpc/2/object"), uid

def odoo_call(models, uid, model, method, *args, **kwargs):
    return models.execute_kw(ODOO_DB_NAME, uid, ODOO_API_KEY, model, method, args, kwargs or {})

def odoo_search_read(models, uid, model, domain, fields=None, limit=0):
    kw = {}
    if fields: kw["fields"] = fields
    if limit: kw["limit"] = limit
    return odoo_call(models, uid, model, "search_read", domain, **kw)

def odoo_write(models, uid, model, ids, vals):
    if not isinstance(ids, list): ids = [ids]
    return odoo_call(models, uid, model, "write", ids, vals)

def odoo_create(models, uid, model, vals):
    return odoo_call(models, uid, model, "create", vals)

# ------------- Space Detect -------------
def detect_space_field(models, uid):
    global SPACE_FIELD, SPACE_MODEL
    if SPACE_FIELD is not None:
        return SPACE_FIELD, SPACE_MODEL
    fields = odoo_call(models, uid, MODEL_ARTICLE, "fields_get", [], {"attributes": ["type","relation"]})
    for cand in ["space_id", "collection_id", "workspace_id"]:
        if cand in fields and fields[cand].get("type") == "many2one":
            SPACE_FIELD = cand
            SPACE_MODEL = fields[cand].get("relation")
            print(f"✓ Phát hiện field Space: {SPACE_FIELD} -> {SPACE_MODEL}")
            return SPACE_FIELD, SPACE_MODEL
    SPACE_FIELD, SPACE_MODEL = None, None
    print("• Không có field Space — sẽ tìm theo bài gốc (parent_id).")
    return None, None

def get_space_id(models, uid, name):
    if not name: return None
    if SPACE_FIELD and SPACE_MODEL:
        rec = odoo_search_read(models, uid, SPACE_MODEL, [("name","=",name)], ["id"], limit=1)
        if rec: return rec[0]["id"]
        sid = odoo_create(models, uid, SPACE_MODEL, {"name": name})
        print(f"   + Tạo Space '{name}' (ID {sid})")
        return sid
    # fallback: tìm bài gốc cùng tên
    root = odoo_search_read(models, uid, MODEL_ARTICLE, [("name","=",name), ("parent_id","=",False)], ["id"], limit=1)
    if root: return root[0]["id"]
    # nếu chưa có, tạo bài gốc
    rid = odoo_create(models, uid, MODEL_ARTICLE, {"name": name, "body": "<p>Root</p>", "parent_id": False})
    print(f"   + Tạo bài gốc '{name}' (ID {rid})")
    return rid

# ------------- Image helpers -------------
def _add_query_param(url: str, **params) -> str:
    u = urlparse(url)
    q = dict(parse_qsl(u.query))
    q.update({k: str(v) for k, v in params.items() if v is not None})
    return urlunparse((u.scheme, u.netloc, u.path, u.params, urlencode(q), u.fragment))

def _strip_hw_attrs(tag_html: str) -> str:
    tag_html = re.sub(r'\swidth="[^"]*"', '', tag_html, flags=re.IGNORECASE)
    tag_html = re.sub(r"\swidth='[^']*'", '', tag_html, flags=re.IGNORECASE)
    tag_html = re.sub(r'\sheight="[^"]*"', '', tag_html, flags=re.IGNORECASE)
    tag_html = re.sub(r"\sheight='[^']*'", '', tag_html, flags=re.IGNORECASE)
    # xoá width/height cũ trong style
    tag_html = re.sub(
        r'style="[^"]*"',
        lambda m: re.sub(r'(?:^|\s)(?:max-)?(?:width|height)\s*:[^;]*;?', '', m.group(0), flags=re.IGNORECASE),
        tag_html
    )
    return tag_html

def _guess_mimetype_from_url(url: str) -> str:
    url = url.lower()
    if url.endswith('.png'): return "image/png"
    if url.endswith('.jpg') or url.endswith('.jpeg'): return "image/jpeg"
    if url.endswith('.gif'): return "image/gif"
    if url.endswith('.svg'): return "image/svg+xml"
    if url.endswith('.webp'): return "image/webp"
    if url.endswith('.avif'): return "image/avif"
    return "application/octet-stream"

def _mirror_external_image(models, uid, src_url: str):
    """Tải ảnh bên ngoài rồi tạo ir.attachment public, trả về URL /web/image/..."""
    try:
        r = requests.get(src_url, timeout=20)
        r.raise_for_status()
        content = r.content
        name = os.path.basename(urlparse(src_url).path) or "image"
        b64 = base64.b64encode(content).decode()
        att_id = odoo_create(models, uid, MODEL_ATTACHMENT, {
            "name": name,
            "datas": b64,
            "mimetype": _guess_mimetype_from_url(src_url),
            "public": True
        })
        rec = odoo_search_read(models, uid, MODEL_ATTACHMENT, [("id","=",att_id)], ["id","name","checksum"], limit=1)
        qs = f"?unique={rec[0]['checksum']}" if rec and rec[0].get("checksum") else ""
        return f"/web/image/{rec[0]['id']}/{rec[0]['name']}{qs}"
    except Exception as e:
        print(f"   ✗ Mirror thất bại: {src_url} -> {e}")
        return None

# ------------- HTML Regex -------------
IMG_TAG_RE   = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
SRC_RE       = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
SRCSET_RE    = re.compile(r'(srcset)=["\']([^"\']+)["\']', re.IGNORECASE)
SOURCE_SRCSET_RE = re.compile(r'(<source\b[^>]*\s)srcset=["\']([^"\']+)["\']', re.IGNORECASE)
URL_IN_STYLE_RE  = re.compile(r'url\((["\']?)([^)\'"]+)\1\)', re.IGNORECASE)

# Brutal mode – bắt tất cả biến thể attr/URL ReadMe còn sót
GEN_ATTR_RE = re.compile(
    r'(?P<attr>\b(?:src|data-src|data-original|data-lazy-src|href)\b)\s*=\s*["\'](?P<url>https?://files\.readme\.io/[^"\']+)["\']',
    re.IGNORECASE
)
ALL_URL_RE = re.compile(
    r'https?://files\.readme\.io/[\w\-/\.%]+(?:\.(?:png|jpg|jpeg|gif|svg|webp|avif)|\?(?:[^"\')<>\s]+)?)',
    re.IGNORECASE
)

# ------------- Img attr + zoom -------------
def _img_add_responsive_attrs(tag_html: str) -> str:
    if re.search(r'\bdata-abivin-img="1"\b', tag_html, flags=re.IGNORECASE):
        return tag_html

    # xoá width/height/style cũ
    tag_html = _strip_hw_attrs(tag_html)

    # ✅ KHÔNG ép width:100%. Chỉ cho phép co lại trong khung, không phóng to
    style_attrs = (
        'style="max-width:100%!important;'
        'height:auto!important;'
        'display:inline-block!important;'
        'object-fit:contain!important;"'
    )
    if ' style=' not in tag_html:
        tag_html = tag_html.replace('<img', f'<img {style_attrs}', 1)
    else:
        tag_html = re.sub(r'style="[^"]*"', style_attrs, tag_html)

    if ' loading=' not in tag_html:
        tag_html = tag_html.replace('<img', '<img loading="lazy"', 1)

    if not re.search(r'\bsizes=', tag_html, flags=re.IGNORECASE):
        tag_html = tag_html.replace(
            '<img',
            f'<img sizes="(max-width: {MAX_FIGURE_W}px) 100vw, {MAX_FIGURE_W}px"',
            1
        )

    # đánh dấu + bật zoom
    tag_html = tag_html.replace('<img', '<img data-abivin-img="1" data-abivin-zoom="1"', 1)

    # data-zoom-src chỉ dùng bản lớn (2400px) cho ảnh zoom
    m = re.search(r'\ssrc=["\']([^"\']+)["\']', tag_html, flags=re.IGNORECASE)
    if m:
        src = m.group(1)
        if '/web/image' in src:
            u = urlparse(src); q = dict(parse_qsl(u.query))
            q['width'] = '2400'
            zoom_src = urlunparse((u.scheme,u.netloc,u.path,u.params,urlencode(q),u.fragment))
            if 'data-zoom-src' not in tag_html:
                tag_html = tag_html.replace('<img ', f'<img data-zoom-src="{zoom_src}" ', 1)
    return tag_html


def _wrap_figure(img_tag_html: str) -> str:
    return (
        f'<figure style="max-width:{MAX_FIGURE_W}px;'
        f'width:100%;margin:12px auto;display:block;'
        f'text-align:center;box-sizing:border-box;">'
        f'{_img_add_responsive_attrs(img_tag_html)}'
        f'</figure>'
    )


# ------------- HTML Rewrite -------------
def rewrite_html(models, uid, html: str) -> str:
    if not html:
        return html
    changed = False
    new_html = html

    def add_width_to_web_image(url: str) -> str:
       # if "/web/image" in url:
       #     return _add_query_param(url, width=RESPONSIVE_W)
        return url

    # 1) Thay src trên <img>
    def src_replacer(m):
        nonlocal changed
        src = m.group(1); full = m.group(0)

        if MIRROR_EXTERNAL and src.startswith(("http://", "https://")) and "/web/image" not in src:
            new_web = _mirror_external_image(models, uid, src)
            if new_web:
                new_web = add_width_to_web_image(new_web)
                changed = True
                return full.replace(src, new_web)
            return full

        if "/web/image" in src:
            new_src = add_width_to_web_image(src)
            if new_src != src:
                changed = True
                return full.replace(src, new_src)
        return full

    new_html = SRC_RE.sub(src_replacer, new_html)

    # 2) Bọc figure (idempotent) + responsive attrs
    def wrap_img(m):
        nonlocal changed, new_html
        tag = m.group(0)

        # Bỏ qua nếu đã đánh dấu xử lý
        if re.search(r'\bdata-abivin-img="1"\b', tag, flags=re.IGNORECASE):
            return tag

        # Tránh bọc lặp nếu đã ở trong figure (simple context check)
        start_ctx = max(0, m.start() - 100)
        end_ctx = min(len(new_html), m.end() + 100)
        before = new_html[start_ctx:m.start()]
        after  = new_html[m.end():end_ctx]
        if re.search(r'<figure\b[^>]*>[^<]*$', before, flags=re.IGNORECASE) \
           or re.search(r'^[^>]*</figure>', after, flags=re.IGNORECASE):
            # chỉ thêm responsive attrs
            processed = _img_add_responsive_attrs(tag)
            if processed != tag:
                changed = True
            return processed

        wrapped = _wrap_figure(tag)
        if wrapped != tag:
            changed = True
        return wrapped

    new_html = IMG_TAG_RE.sub(wrap_img, new_html)

    # 3) srcset trên <img>
    def srcset_rewrite(val: str):
        parts = [p.strip() for p in val.split(',') if p.strip()]
        new_parts, modified = [], False
        for p in parts:
            seg = p.split()
            if not seg: continue
            url_part = seg[0]
            rest = " " + " ".join(seg[1:]) if len(seg) > 1 else ""
            if MIRROR_EXTERNAL and url_part.startswith(("http://","https://")) and "/web/image" not in url_part:
                new_url = _mirror_external_image(models, uid, url_part) or url_part
            else:
                new_url = add_width_to_web_image(url_part)
            if new_url != url_part:
                modified = True
            new_parts.append(f"{new_url}{rest}")
        return ", ".join(new_parts), modified

    def srcset_img_replacer(m):
        nonlocal changed
        attr, val = m.group(1), m.group(2)
        repl, mod = srcset_rewrite(val)
        if mod: changed = True
        return f'{attr}="{repl}"'

    new_html = SRCSET_RE.sub(srcset_img_replacer, new_html)

    # 4) <source srcset="...">
    def source_srcset_replacer(m):
        nonlocal changed
        prefix, val = m.group(1), m.group(2)
        repl, mod = srcset_rewrite(val)
        if mod: changed = True
        return f'{prefix}srcset="{repl}"'
    new_html = SOURCE_SRCSET_RE.sub(source_srcset_replacer, new_html)

    # 5) background-image: url(...)
    def css_url_replacer(m):
        nonlocal changed
        quote, u = m.group(1), m.group(2)
        new_u = u
        if MIRROR_EXTERNAL and u.startswith(("http://","https://")) and "/web/image" not in u:
            web = _mirror_external_image(models, uid, u)
            if web:
                new_u = add_width_to_web_image(web)
        elif "/web/image" in u:
            new_u = add_width_to_web_image(u)
        if new_u != u:
            changed = True
        return f"url({quote}{new_u}{quote})"
    new_html = URL_IN_STYLE_RE.sub(css_url_replacer, new_html)

    # 6) BRUTAL MODE – thay trong attr data-src/data-original/href
    def _mirror_url_any(u: str) -> str:
        web = _mirror_external_image(models, uid, u)
        return _add_query_param(web, width=RESPONSIVE_W) if web else u

    def attr_replacer(m):
        nonlocal changed
        url = m.group('url')
        if MIRROR_EXTERNAL and (url.startswith('http://') or url.startswith('https://')) and '/web/image' not in url:
            new_url = _mirror_url_any(url)
            if new_url != url:
                changed = True
            return f'{m.group("attr")}="{new_url}"'
        return m.group(0)
    new_html = GEN_ATTR_RE.sub(attr_replacer, new_html)

    # 7) BRUTAL MODE fallback – quét mọi URL ReadMe còn sót
    def url_replacer(m):
        nonlocal changed
        url = m.group(0)
        if MIRROR_EXTERNAL and '/web/image' not in url:
            new_url = _mirror_url_any(url)
            if new_url != url:
                changed = True
            return new_url
        return url
    new_html = ALL_URL_RE.sub(url_replacer, new_html)

    # 8) Dọn nested figure nếu lỡ bọc lặp
    new_html = re.sub(
        r'<figure[^>]*>\s*(<figure[^>]*>.*?</figure>)\s*</figure>',
        r'\1',
        new_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    return new_html if changed else html

# ------------- Main process -------------
def main():
    global ODOO_BASE_URL, ODOO_DB_NAME, ODOO_USER, ODOO_API_KEY
    global SPACE_NAME, ROOT_ARTICLE, MAX_FIGURE_W, RESPONSIVE_W, MIRROR_EXTERNAL

    ap = argparse.ArgumentParser(description="Post-process ảnh trong Odoo Knowledge.")
    ap.add_argument("--url", default=ODOO_BASE_URL)
    ap.add_argument("--db", default=ODOO_DB_NAME)
    ap.add_argument("--user", default=ODOO_USER)
    ap.add_argument("--apikey", default=ODOO_API_KEY)
    ap.add_argument("--space", help="Tên Space (nếu instance có field space)")
    ap.add_argument("--root", help="Tên bài gốc (nếu không có field space)")
    ap.add_argument("--maxw", type=int, default=MAX_FIGURE_W, help="max-width cho figure (px)")
    ap.add_argument("--imgw", type=int, default=RESPONSIVE_W, help="width cho /web/image (px)")
    ap.add_argument("--mirror", action="store_true", help="Mirror ảnh ngoài vào Odoo")
    args = ap.parse_args()

    ODOO_BASE_URL = args.url.rstrip("/")
    ODOO_DB_NAME  = args.db
    ODOO_USER     = args.user
    ODOO_API_KEY  = args.apikey
    if args.space: SPACE_NAME = args.space
    if args.root:  ROOT_ARTICLE = args.root
    MAX_FIGURE_W  = args.maxw
    RESPONSIVE_W  = args.imgw
    MIRROR_EXTERNAL = args.mirror

    models, uid = odoo_login()
    detect_space_field(models, uid)
    anchor_id = get_space_id(models, uid, SPACE_NAME if SPACE_NAME else ROOT_ARTICLE)
    if not anchor_id:
        raise SystemExit("❌ Không xác định được Space/bài gốc để quét.")

    # Lấy danh sách bài trong Space/bài gốc
    if SPACE_FIELD:
        domain = [(SPACE_FIELD, "=", anchor_id)]
    else:
        domain = []  # fallback: lấy tất cả rồi lọc theo cây

    print("🔎 Đang quét bài viết...")
    fields = ["id","name","body","parent_id"]
    articles = odoo_search_read(models, uid, MODEL_ARTICLE, domain, fields=fields, limit=0)
    if not articles:
        print("• Không tìm thấy bài nào.")
        return

    if not SPACE_FIELD:
        # Lọc theo cây con của anchor_id
        keep = set([anchor_id])
        id_to_parent = {a["id"]: (a["parent_id"][0] if a.get("parent_id") else None) for a in articles}
        changed_flag = True
        while changed_flag:
            changed_flag = False
            for aid, pid in id_to_parent.items():
                if aid in keep: continue
                if pid in keep:
                    keep.add(aid); changed_flag = True
        articles = [a for a in articles if a["id"] in keep]

    print(f"📄 Tổng bài cần xử lý: {len(articles)}")
    updated = 0
    for a in articles:
        old = a.get("body") or ""
        new = rewrite_html(models, uid, old)
        if new != old:
            odoo_write(models, uid, MODEL_ARTICLE, a["id"], {"body": new})
            updated += 1
            print(f"   ✓ Cập nhật: [{a['id']}] {a['name'][:70]}")

    print(f"✅ Hoàn tất. Đã cập nhật {updated}/{len(articles)} bài.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Hủy bởi người dùng")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        import traceback; traceback.print_exc()
