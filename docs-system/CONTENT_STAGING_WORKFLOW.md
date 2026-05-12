# Content Staging Workflow

This document defines the lifecycle and staging procedures for all content additions to the Astro portfolio.

## 1. Lifecycle: Draft → Review → Validate → Publish
1.  **Draft:** Create content in the designated local or temporary folder.
2.  **Review:** Audit for HTML validity, tone consistency, and broken links.
3.  **Validate:** Wrap in necessary components (`RichContentShell`, `OverviewCard`) and run a local build.
4.  **Publish:** Move files to the final directory under `src/pages/` and update navigation or overview grids.

## 2. Folder Strategy
*   **Drafts:** Use local temporary folders or non-indexed subdirectories (e.g., `src/pages/logs/drafts/`).
*   **Staging:** Use a local branch or a dedicated category subdirectory (e.g., `src/pages/ai-lab/`) while the build is being verified.
*   **Published:** Files residing in their final production path within `src/pages/`.

## 3. Naming Conventions
*   **Files:** use `kebab-case.mdx` or `kebab-case.astro`.
*   **Clarity:** Use descriptive names (e.g., `medical-rag-workflow.mdx` instead of `report1.mdx`).
*   **Index:** Section root pages must always be named `index.mdx` or `index.astro`.

## 4. Slug Conventions
*   **Structure:** Slugs are derived from the folder structure (e.g., `/healthtech/whatsapp-automation/`).
*   **Trailing Slashes:** Ensure all internal links include the trailing slash for consistent routing.

## 5. Image Asset Conventions
*   **Location:** Store page-specific images in `public/assets/images/[category]/`.
*   **Naming:** Match the page slug (e.g., `healthtech-whatsapp-hero.webp`).
*   **Format:** Prefer `.webp` or `.svg` for performance.

## 6. AI-Generated Content Review Checklist
- [ ] No placeholder text (e.g., "[Insert Date Here]").
- [ ] No illegal tags (`<html>`, `<head>`, `<body>`).
- [ ] Absolute paths used for all internal links (`/category/page/`).
- [ ] Content wrapped in `RichContentShell` if HTML-heavy.
- [ ] Code blocks are correctly fenced and language-labeled.

## 7. Build Validation Before Publish
1. Run `npm run build`.
2. Confirm the new page appears in the "generating static routes" log.
3. Check for any "broken link" or "missing component" warnings in the console.

## 8. Git Checkpoint Policy
1. **Commit** all stable changes before adding new content.
2. **Commit** the new content only after a successful build.
3. Use descriptive commit messages (e.g., `feat(content): add medical RAG architecture study`).

## 9. Rollback Workflow
1. **Revert:** Use `git revert [commit-hash]` to remove breaking content.
2. **Clean:** Delete the corresponding `.html` file from the `dist/` folder if it persists in the local environment.
3. **Verify:** Run `npm run build` to ensure the project returns to a stable state.

## 10. Conversion Rules
*   **Raw HTML:** Must be sanitized and wrapped in `<RichContentShell>`. Inline `<style>` blocks should be moved to a scoped `<style>` block in an `.astro` file.
*   **Markdown:** Should be converted to `.mdx` to allow component usage (e.g., `<OverviewCard />`).
*   **AI Reports:** Must be audited for "AI Hallucinations" and layout-breaking tables before being committed to `src/pages/`.
