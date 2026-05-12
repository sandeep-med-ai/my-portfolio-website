# AI Content Import Workflow

This document defines the safe procedure for importing AI-generated HTML and structured content into the Astro portfolio.

## 1. Safe Import Workflow
1. **Source:** Generate content via LLM.
2. **Sanitize:** Remove prohibited tags (see Section 4).
3. **Draft:** Create a `.mdx` or `.astro` file in a branch or local environment.
4. **Shelling:** Wrap HTML-heavy content in `<RichContentShell />`.
5. **Dry Run:** Run `npm run build` to check for parser or routing errors.
6. **Validation:** Check mobile responsiveness and overflow behavior.

## 2. Component Selection Guidance
- **MDX:** Primary choice for article-based content, documentation, and lists. Best for content needing standard project styles.
- **Astro Components:** Use for interactive UI elements, reusable patterns (e.g., `OverviewCard`), or logic-heavy sections.
- **RichContentShell:** Use for complex, HTML-heavy imports, legacy HTML conversions, or content with high layout-breaking risk (tables, large images, pre-formatted code).

## 3. Required Validation
- **HTML Validity:** Ensure all tags are closed; MDX will fail the build on unclosed tags.
- **Path Verification:** Check all `href` and `src` attributes for dead links or relative path inconsistencies.
- **Responsiveness:** Verify that content does not cause horizontal scrolling on mobile (viewport < 700px).

## 4. Forbidden HTML Patterns
- **No `<html>`, `<head>`, or `<body>` tags.**
- **No global `<style>` blocks** (use scoped `<style>` or `<style is:global>` with extreme caution).
- **No ID collisions:** Avoid using generic IDs like `header`, `footer`, or `main`.
- **No absolute pixel widths** on containers (e.g., `width: 800px;`). Use `max-width: 100%`.

## 5. Safe Script Handling
- **Prefer Astro `<script>`:** Keep scripts scoped to the component.
- **No `document.write()`:** Prohibited as it breaks React/Astro hydration.
- **External Scripts:** Must use the `is:inline` directive if they depend on global variables or external CDNs.

## 6. Asset Handling Rules
- **Local Assets:** Place in `public/` or `src/assets/`.
- **Remote Images:** Must have a `loading="lazy"` attribute.
- **Alt Text:** Every `<img>` tag must include descriptive `alt` text.

## 7. CSS Containment Rules
- **Isolation:** Use `<style>` blocks inside `.astro` files to ensure scoped styles.
- **Naming:** Prefix AI-specific classes (e.g., `.ai-canvas`, `.report-grid`) to avoid collisions with `custom.css`.
- **No `!important`:** Do not use `!important` to override global styles unless using `RichContentShell`.

## 8. Build Validation Workflow
1. Apply changes.
2. Run `npm run build`.
3. Check `dist/` output for the specific page.
4. Verify `sitemap-index.xml` includes the new route.

## 9. Rollback Workflow
1. **Identify:** If the build fails or layout breaks, revert to the last stable git commit.
2. **Isolate:** Move the breaking content to a standalone `.txt` file for debugging.
3. **Strip:** Remove all custom CSS and scripts from the content and re-import into a blank `RichContentShell`.

## 10. Maximum Safe Complexity Guidance
- **Single Page Size:** < 500KB (HTML/Text).
- **Inline CSS:** < 200 lines per component.
- **Embedded Scripts:** < 100 lines; otherwise, move to a separate `.js` file.
- **Tables:** Maximum 6 columns for mobile readability; use `overflow-x: auto`.
- **Images:** Maximum 2MB per image; prefer WebP format.
