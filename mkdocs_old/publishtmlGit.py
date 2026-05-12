import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[-\s]+', '-', text).strip('-')

def make_html_bulletproof(raw_html):
    # 1. Extract all CSS styles
    styles = ""
    style_matches = re.finditer(r'<style.*?>(.*?)</style>', raw_html, re.DOTALL | re.IGNORECASE)
    for match in style_matches:
        css_content = match.group(1)
        # Magic: Protect MkDocs body from AI CSS bleeding
        css_content = re.sub(r'\bbody\s*{', '.ai-canvas {', css_content, flags=re.IGNORECASE)
        styles += f"\n<style>\n{css_content}\n</style>\n"

    # 2. Extract actual content (ignore head, html tags)
    body_match = re.search(r'<body.*?>(.*?)</body>', raw_html, re.DOTALL | re.IGNORECASE)
    if body_match:
        body_content = body_match.group(1)
    else:
        # Fallback if AI didn't give a body tag
        body_content = re.sub(r'<head.*?>.*?</head>', '', raw_html, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'<style.*?>.*?</style>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'</?html.*?>', '', body_content, flags=re.IGNORECASE)

    # Wrap content in our isolated canvas
    safe_body = f'<div class="ai-canvas">\n{body_content.strip()}\n</div>'
    
    return styles + "\n" + safe_body

def auto_publish():
    DOCS_DIR = "docs"
    
    print("-" * 50)
    print("🚀 Dr. Sandeep's Bulletproof AI-HTML Publisher")
    print("-" * 50)

    category = input("👉 Folder का नाम (e.g., ai-projects): ").strip()
    title = input("👉 Page का Title (e.g., My New Blog): ").strip()
    
    clean_name = slugify(title)
    file_name = f"{clean_name}.md"
    
    category_path = os.path.join(DOCS_DIR, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
        print(f"📁 नया फोल्डर बनाया गया: {category}")

    print("📝 अपना Raw AI HTML कोड पेस्ट करें (खत्म होने पर नई लाइन में 'DONE' लिखकर Enter दबाएं):")
    html_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        html_lines.append(line)
    
    raw_html = "\n".join(html_lines)
    safe_html = make_html_bulletproof(raw_html)

    # 3. Add YAML Frontmatter so awesome-pages NEVER misses it
    final_content = f"""---
title: {title}
---

{safe_html}
"""
    
    file_path = os.path.join(category_path, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)

    print("-" * 50)
    print(f"✅ BOOM! File is completely Bulletproof and Ready!")
    print(f"📍 Location: {file_path}")
    print("-" * 50)

if __name__ == "__main__":
    if not os.path.exists("docs"):
        os.makedirs("docs")
    auto_publish()