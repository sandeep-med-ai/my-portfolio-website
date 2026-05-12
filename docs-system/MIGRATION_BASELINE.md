# Astro Migration Baseline Snapshot

## Environment & Versions
- **Astro Version:** ^6.3.1
- **Installed Integrations:**
  - `@astrojs/mdx` (^5.0.4)
  - `@astrojs/sitemap` (^3.7.2)

## Build Configuration
- **Build Scripts:**
  - `dev`: `astro dev`
  - `build`: `astro build`
  - `preview`: `astro preview`
- **Build Output Folder:** `dist/`
- **Sitemap URL:** `https://drsandeep.allhelp.in/`

## Project Structure
- **Content Section Folders (src/pages/):**
  - `ai-hub/`
  - `ai-lab/`
  - `ai-projects/`
  - `clinical/`
  - `healthtech/`
  - `insights/`
  - `logs/`
  - `medical/`
  - `portfolio/`
  - `visuals/`
- **Page Count:** 39 generated routes
- **Active Layouts:**
  - `src/layouts/Layout.astro`
- **Active CSS Files:**
  - `src/styles/custom.css`
- **Public Asset Folders:**
  - `public/` (Root assets: `favicon.ico`, `favicon.svg`, `CNAME`, `google78d5b225102cbb45.html`)

## DO NOT CHANGE WITHOUT ARCHITECT APPROVAL

### Routing Structure
- File-based routing is strictly enforced within `src/pages/`.
- All index pages must be named `index.mdx` or `index.astro`.

### Layout Structure
- `src/layouts/Layout.astro` is the primary wrapper for all content.
- MDX files must reference the layout in frontmatter: `layout: ../path/to/Layout.astro`.
- Astro components must import and wrap content in `<Layout>`.

### CSS Organization
- Global styles are maintained in `src/styles/custom.css`.
- Layout-specific overrides are handled in `src/layouts/Layout.astro` via `<style is:global>`.
- Component-scoped styles should use standard Astro `<style>` blocks.

### Public Asset Paths
- All static files (CNAME, verification files, icons) must remain in the `public/` root.

### Link Policy
- **Root-Relative Links:** All internal links in MDX/Astro files MUST use root-relative paths starting with `/` (e.g., `href="/ai-projects/emr-automation/"`). Relative paths are prohibited to ensure link stability across nested routes.
