# RICH CONTENT POLICY

## 1. APPROVED RICH CONTENT TYPES
- **MDX:** Primary format for mixed content (Markdown + JSX/HTML).
- **Astro Components (.astro):** Mandatory for pages requiring complex logic, multiple `<style>` blocks, or scoped scripts.
- **Isolated HTML Blocks:** Permitted within MDX for structural layout.
- **Embedded Scripts:** Permitted via Astro `<script>` tags (bundled/scoped) or `is:inline` for verified small snippets.

## 2. FORBIDDEN PATTERNS
- **Global CSS Leakage:** DO NOT use `<style>` in MDX without scope or targeting. Use Astro components for styling isolation.
- **Inline Unscoped JS:** No `<script>` tags in the middle of MDX body without `is:inline` (and only if necessary).
- **External CDN Reliance:** DO NOT rely on external CDNs for core functionality. Download and place in `public/` or `src/`.
- **Uncontrolled Iframes:** No iframes without fixed dimensions and `loading="lazy"`.
- **Duplicate Styling Systems:** No Tailwind, Bootstrap, or other frameworks. Use existing `custom.css` variables.

## 3. SAFE COMPONENT RULES
- Components must reside in `src/components/` (if shared) or `src/pages/` (if page-specific `.astro` files).
- Every component must handle its own errors to prevent site-wide build failure.

## 4. HTML ISOLATION RULES
- Complex HTML structures (dashboards, reports) MUST be moved to `.astro` files to ensure proper rendering and style encapsulation.
- MDX should be reserved for content-heavy pages with simple HTML enhancements.

## 5. SCRIPT LOADING RULES
- Use standard Astro `<script>` tags (processed by Vite) by default.
- Use `<script is:inline>` ONLY for third-party tracking or verification snippets.
- Avoid JS for visual effects that can be achieved with CSS.

## 6. ASSET PLACEMENT RULES
- **Content Images:** `public/assets/images/[section]/`
- **Global Assets:** `public/` root (favicon, CNAME).
- **Styles:** `src/styles/` for global; Component-scoped `<style>` for local.

## 7. PERFORMANCE PROTECTION RULES
- Large datasets must be structured as JSON in `src/data/` or handled via static site generation.
- Media must use `loading="lazy"` and appropriate dimensions.

## 8. ACCESSIBILITY MINIMUMS
- All images MUST have `alt` text.
- All interactive elements MUST have visible focus states.
- Semantic HTML headers (h1-h6) MUST follow a logical hierarchy.

## 9. MOBILE RENDERING REQUIREMENTS
- All rich content MUST be responsive.
- Horizontal scrolling is prohibited except for `<table>` or `<pre>` blocks.
- Touch targets for buttons/links must be at least 44x44px.

## 10. RECOVERY RULES
- If a page breaks the global layout:
  1. Immediately wrap the content in a defensive `<div>` with `overflow: hidden`.
  2. If failure persists, convert the page to a minimal `.astro` file using only the base `Layout`.
  3. Validate against `RECOVERY_WORKFLOW.md`.
