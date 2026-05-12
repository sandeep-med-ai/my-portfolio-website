# SYSTEM GUARDRAILS

## PROHIBITED ACTIONS
- DO NOT delete `mkdocs_old/` until a secondary off-site backup is confirmed.
- DO NOT modify the `dist/` directory manually; all changes must come from `src/`.
- DO NOT use relative `href` paths in Markdown/Astro files; use root-relative paths only.
- DO NOT rename folders in `src/pages/` without a corresponding update to `src/layouts/Layout.astro`.

## APPROVED MODIFICATION ZONES
- `src/pages/`: Content and individual page components.
- `src/styles/custom.css`: Global visual identity.
- `src/layouts/Layout.astro`: Site-wide structure and shell.
- `public/`: Static assets, verification files, and downloads.

## FORBIDDEN DEPENDENCY BEHAVIOR
- DO NOT install TailwindCSS or other utility-first CSS frameworks.
- DO NOT add React, Vue, or Svelte components without a specific architectural directive.
- DO NOT remove or downgrade `@astrojs/mdx` or `@astrojs/sitemap`.

## ROUTING PROTECTION RULES
- Every subfolder in `src/pages/` MUST contain an `index.mdx` or `index.astro` file.
- All new routes must be lowercase and use hyphens for spaces (kebab-case).
- Duplicate route definitions (e.g., `index.astro` and `index.mdx` in the same folder) are strictly forbidden.

## CSS PROTECTION RULES
- Global CSS variables must reside in `src/styles/custom.css`.
- Global overrides for third-party or generated HTML must be placed in the `<style is:global>` block of `src/layouts/Layout.astro`.

## ASSET PATH RULES
- Static verification files (Google, Bing, etc.) and `CNAME` must reside in the `public/` root.
- All images used in content should ideally be placed in a structured folder within `public/`.

## BUILD VALIDATION REQUIREMENTS
- `npm run build` MUST execute successfully with zero errors before any merge or deployment.
- All sitemap warnings must be resolved by ensuring `site` is correctly set in `astro.config.mjs`.

## MANDATORY PRE-CHANGE CHECKS
1. Consult `MIGRATION_BASELINE.md` to ensure structural alignment.
2. Run `npm run build` to confirm a stable starting state.
3. Verify that the proposed change does not create a routing collision.
