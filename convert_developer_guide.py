# Convert Developer Guide HTML sang Markdown đơn giản
import os
import json
import re
from bs4 import BeautifulSoup

def clean_developer_html(html_content):
    """Chuyển HTML Developer Guide sang HTML đơn giản"""
    if not html_content:
        return ""
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Xóa các elements không cần thiết
    for tag in soup.find_all(['script', 'style', 'link', 'nav', 'aside']):
        tag.decompose()
    
    # Giữ lại: headings, paragraphs, code blocks, images
    result = []
    
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'pre', 'code', 'img', 'ul', 'ol', 'li']):
        if element.name in ['h1', 'h2', 'h3', 'h4']:
            text = element.get_text(strip=True)
            if text:
                result.append(f"<{element.name}>{text}</{element.name}>")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                result.append(f"<p>{text}</p>")
        elif element.name == 'code':
            text = element.get_text(strip=True)
            if text:
                result.append(f"<code>{text}</code>")
        elif element.name == 'pre':
            text = element.get_text()
            if text:
                result.append(f"<pre>{text}</pre>")
        elif element.name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '')
            if src:
                result.append(f'<img src="{src}" alt="{alt}" style="max-width: 100%; height: auto;" />')
        elif element.name in ['ul', 'ol']:
            li_texts = [li.get_text(strip=True) for li in element.find_all('li') if li.get_text(strip=True)]
            if li_texts:
                for li_text in li_texts:
                    result.append(f"<li>{li_text}</li>")
    
    return '\n'.join(result)


def process_developer_guide():
    """Chuyển đổi tất cả Developer Guide files"""
    dev_guide_dir = os.path.join("developer_guide", "content_developer_guide")
    
    files_processed = 0
    
    for json_file in os.listdir(dev_guide_dir):
        if not json_file.endswith('.json'):
            continue
        
        file_path = os.path.join(dev_guide_dir, json_file)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            doc = json.load(f)
        
        # Clean HTML
        old_html = doc.get('html_content', '')
        new_html = clean_developer_html(old_html)
        
        if new_html and new_html != old_html:
            doc['html_content'] = new_html
            
            # Save back
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(doc, f, ensure_ascii=False, indent=2)
            
            files_processed += 1
            print(f"✓ Converted: {json_file[:50]}")
    
    print(f"\n✅ Đã convert {files_processed} Developer Guide files sang HTML đơn giản!")


if __name__ == "__main__":
    process_developer_guide()


