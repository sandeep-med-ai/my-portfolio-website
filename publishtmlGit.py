import os

# आपकी साइट का मेन docs फोल्डर
DOCS_DIR = "docs"

def auto_publish():
    print("🚀 Dr. Sandeep's HTML-to-MkDocs Auto-Publisher")
    print("-" * 50)
    
    # 1. यूजर से जानकारी लें
    category = input("👉 Folder का नाम बताएं (e.g., healthtech, medical): ").strip()
    title = input("👉 Page का Title बताएं: ").strip()
    
    folder_name = category.lower().replace(" ", "-")
    file_name = title.lower().replace(" ", "-") + ".md"
    
    print("\n👇 अपना पूरा HTML Code नीचे Paste करें.")
    print("   (जब पूरा paste हो जाए, तो नई लाइन में 'DONE' टाइप करके Enter दबाएं):")
    
    html_lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "DONE":
                break
            html_lines.append(line)
        except EOFError:
            break
            
    html_content = "\n".join(html_lines)
    
    # 2. HTML को वैसे ही रखें, बस टॉप पर Title (H1) लगा दें ताकि MkDocs मेन्यू में नाम पकड़ ले
    final_content = f"# {title}\n\n{html_content}"
    
    # 3. फोल्डर तैयार करें
    category_path = os.path.join(DOCS_DIR, folder_name)
    os.makedirs(category_path, exist_ok=True)
    
    # 4. अगर नया फोल्डर है, तो .pages फाइल खुद बनाएं
    pages_file = os.path.join(category_path, ".pages")
    if not os.path.exists(pages_file):
        with open(pages_file, "w", encoding="utf-8") as f:
            f.write(f"title: {category.title()}\n")
        print(f"✅ Auto-created menu setting: {pages_file}")
        
    # 5. फाइल सेव करें
    file_path = os.path.join(category_path, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    print("-" * 50)
    print(f"🎉 BOOM! आपका कस्टम HTML पेज पब्लिश हो गया!")
    print(f"📂 Location: {file_path}")

if __name__ == "__main__":
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)
    auto_publish()