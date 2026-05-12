import os
import sys
import re
import argparse

"""
USAGE EXAMPLE:
python ingest_html.py article.html ai-systems/projects "My Project" --desc "A brief description"
python ingest_html.py report.html clinical/research "Clinical Study" --dry-run
"""

# Configuration
INPUT_DIR = "./input"
PAGES_DIR = "./src/pages"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def sanitize_content(html):
    # Remove outer html/head/body wrappers
    html = re.sub(r'<!DOCTYPE.*?>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<html.*?>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'</html>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<head.*?>.*?</head>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<body.*?>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'</body>', '', html, flags=re.IGNORECASE | re.DOTALL)
    return html.strip()

def ingest_html(filename, category, title, description="", dry_run=False):
    input_path = os.path.join(INPUT_DIR, filename)
    
    if not os.path.exists(input_path):
        print(f"Error: Source file '{filename}' not found in {INPUT_DIR}")
        return

    # Process Path
    category_parts = category.strip('/').split('/')
    category_path = os.path.join(PAGES_DIR, *category_parts)
    slug = slugify(title)
    output_path = os.path.join(category_path, f"{slug}.astro")

    # Safety Check: Do not overwrite
    if os.path.exists(output_path):
        print(f"Error: Destination file '{output_path}' already exists. Use a different title or remove the file manually.")
        return

    # Calculate Import Depth
    depth = len(category_parts)
    dots = "../" * (depth + 1)

    if dry_run:
        print(f"[DRY RUN] Would create: {output_path}")
        print(f"[DRY RUN] Category depth detected: {depth}")
        print(f"[DRY RUN] Relative path for imports: {dots}")
        return

    # Read and Sanitize
    with open(input_path, 'r', encoding='utf-8') as f:
        content = sanitize_content(f.read())

    # Build Astro Template
    astro_template = f"""---
import Layout from '{dots}layouts/Layout.astro';
import RichContentShell from '{dots}components/RichContentShell.astro';
---

<Layout title="{title}">
  <RichContentShell title="{title}" description="{description}">
    {content}
  </RichContentShell>
</Layout>
"""

    # Ensure Category Path Exists
    if not os.path.exists(category_path):
        os.makedirs(category_path)
        print(f"Created new category: {category_path}")

    # Write File
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(astro_template)

    print(f"Success! Generated: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sanitize and ingest raw HTML files into the Astro project.")
    parser.add_argument("filename", help="The HTML filename inside the input/ folder.")
    parser.add_argument("category", help="Target category path (e.g., ai-systems/projects).")
    parser.add_argument("title", help="Page title (used for slug generation).")
    parser.add_argument("--desc", default="", help="Optional page description.")
    parser.add_argument("--dry-run", action="store_true", help="Preview the destination without writing files.")

    args = parser.parse_args()

    ingest_html(args.filename, args.category, args.title, args.desc, args.dry_run)
