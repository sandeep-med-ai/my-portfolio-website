import os
import re

def slugify(text):
    # यह फंक्शन फाइल के नाम से स्पेशल कैरेक्टर्स हटाकर उसे सुरक्षित बनाता है
    text = text.lower()
    # कोलन, सवालिया निशान आदि हटाता है
    text = re.sub(r'[^\w\s-]', '', text)
    # स्पेस को डैश (-) में बदलता है
    return re.sub(r'[-\s]+', '-', text).strip('-')

def auto_publish():
    DOCS_DIR = "docs"
    
    print("-" * 50)
    print("🚀 Dr. Sandeep's HTML-to-MkDocs Auto-Publisher (V2)")
    print("-" * 50)

    category = input("👉 Folder का नाम (e.g., ai-projects): ").strip()
    title = input("👉 Page का Title (e.g., My New Blog): ").strip()
    
    # स्मार्ट फाइल नेमिंग: टाइटल को क्लीन करके पक्का .md जोड़ता है
    clean_name = slugify(title)
    file_name = f"{clean_name}.md"
    
    category_path = os.path.join(DOCS_DIR, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
        print(f"📁 नया फोल्डर बनाया गया: {category}")

    print("📝 अपना HTML कोड पेस्ट करें (खत्म होने पर नई लाइन में 'DONE' लिखकर Enter दबाएं):")
    html_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        html_lines.append(line)
    
    final_content = "\n".join(html_lines)
    file_path = os.path.join(category_path, file_name)

    # फाइल लिखना
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)

    print("-" * 50)
    print(f"✅ BOOM! आपकी फाइल पब्लिश होने के लिए तैयार है!")
    print(f"📍 Location: {file_path}")
    print("-" * 50)

if __name__ == "__main__":
    if not os.path.exists("docs"):
        os.makedirs("docs")
    auto_publish()