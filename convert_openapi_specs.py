import json
import re
from pathlib import Path

SAFE_TAG = re.compile(r"[^a-zA-Z0-9_\-]")

def slugify(text: str) -> str:
    s = re.sub(r"\s+", "-", text.strip())
    s = SAFE_TAG.sub("-", s)
    return s.strip("-").lower()

STYLE = """
<style>
  body{font-family:Segoe UI,Arial,sans-serif;line-height:1.6;padding:20px;color:#222}
  .badge{display:inline-block;padding:2px 8px;border-radius:4px;font-size:12px;color:#fff;margin-right:8px}
  .GET{background:#2f855a}.POST{background:#2b6cb0}.PUT{background:#975a16}.DELETE{background:#c53030}
  pre{background:#f6f8fa;border:1px solid #eaecef;border-radius:6px;padding:12px;overflow:auto}
  table{border-collapse:collapse;width:100%;margin:12px 0}
  th,td{border:1px solid #eaecef;padding:8px;text-align:left}
  h1,h2,h3{margin:18px 0 8px}
</style>
"""

def render_endpoint_html(spec_title: str, spec_name: str, tag: str, method: str, path: str, op: dict) -> str:
    summary = op.get("summary") or op.get("operationId") or f"{method} {path}"
    description = op.get("description") or ""
    badge = f"<span class='badge {method.upper()}'>{method.upper()}</span>"

    # Parameters
    params_html = ""
    params = op.get("parameters") or []
    if params:
        rows = []
        for p in params:
            p_name = p.get("name", "")
            p_in = p.get("in", "")
            p_type = (p.get("schema") or {}).get("type", "")
            p_desc = p.get("description", "")
            rows.append(f"<tr><td>{p_name}</td><td>{p_in}</td><td>{p_type}</td><td>{p_desc}</td></tr>")
        params_html = (
            "<h3>Parameters</h3><table><tr><th>Name</th><th>In</th><th>Type</th><th>Description</th></tr>"
            + "".join(rows)
            + "</table>"
        )

    # Request body
    req_html = ""
    rb = op.get("requestBody") or {}
    if rb:
        req_html = "<h3>Request Body</h3>"
        content = (rb.get("content") or {}).get("application/json") or {}
        schema = content.get("schema")
        if schema:
            req_html += f"<pre><code>{json.dumps(schema, ensure_ascii=False, indent=2)}</code></pre>"

    # Responses
    resp_html = ""
    responses = op.get("responses") or {}
    if responses:
        parts = []
        for code, r in responses.items():
            schema = (((r or {}).get("content") or {}).get("application/json") or {}).get("schema")
            examples = (((r or {}).get("content") or {}).get("application/json") or {}).get("examples")
            block = f"<h4>Status {code}</h4>"
            if schema:
                block += f"<pre><code>{json.dumps(schema, ensure_ascii=False, indent=2)}</code></pre>"
            if examples:
                block += f"<pre><code>{json.dumps(examples, ensure_ascii=False, indent=2)}</code></pre>"
            parts.append(block)
        resp_html = "<h3>Responses</h3>" + "".join(parts)

    html = f"""
{STYLE}
<h1>{badge} {summary}</h1>
<p><strong>Path:</strong> <code>{path}</code></p>
<p><strong>Spec:</strong> {spec_title} ({spec_name})</p>
{('<p>'+description+'</p>') if description else ''}
{params_html}
{req_html}
{resp_html}
"""
    return html

def main() -> None:
    in_dir = Path("openapi")
    out_dir = Path("developer_guide")
    (out_dir / "content_developer_guide").mkdir(parents=True, exist_ok=True)
    (out_dir / "assets_developer_guide").mkdir(parents=True, exist_ok=True)

    # Skip OpenAPI files vì format không đúng, dùng data đã generate sẵn
    print("⚠️  OpenAPI specs format không đúng, dùng Developer Guide đã có sẵn...")
    # Load các file đã generate từ trước
    existing_docs = list((out_dir / "content_developer_guide").glob("*.json"))
    if existing_docs:
        print(f"  ✓ Tìm thấy {len(existing_docs)} articles trong Developer Guide")
        return
    
    print("  → Chưa có Developer Guide content, vui lòng scrape từ docs.abivin.com")
    print("Generated HTML for Developer Guide from OpenAPI specs.")

if __name__ == "__main__":
    main()
