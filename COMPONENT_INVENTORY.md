# COMPONENT INVENTORY

## 1. REPEATED UI PATTERNS

| Pattern Name | File Locations | Reusable Candidate | Reuse Frequency |
| :--- | :--- | :--- | :--- |
| **Category Hero** | `src/pages/[section]/index.mdx` (Multiple) | Yes | High |
| **Overview Grid** | `src/pages/[section]/index.mdx` (Multiple) | Yes | High |
| **Overview Card** | `src/pages/[section]/index.mdx` (Multiple) | Yes | High |
| **Portfolio Hero** | `src/pages/index.mdx` | Yes (Structure) | Low |
| **Metric Strip** | `src/pages/index.mdx` | Yes | Medium |
| **Premium Card** | `src/pages/index.mdx` | Yes | High |
| **Premium Table** | `src/pages/index.mdx` | Yes | Medium |
| **CTA Section** | `src/pages/index.mdx` | Yes | Medium |
| **AI Canvas** | `src/pages/ai-lab/system-diagnostic-report.astro`, `src/pages/ai-projects/healthcare-intelligence-infrastructure.astro` | Yes (Layout) | Medium |
| **Navigation Tabs**| `src/layouts/Layout.astro` | Yes | High |
| **Global Header** | `src/layouts/Layout.astro` | Yes | High |
| **Global Footer** | `src/layouts/Layout.astro` | Yes | High |

## 2. PATTERN DETAILS

### Category Hero
- **Structure:** `<section class="category-hero"><h1>...</h1><p>...</p></section>`
- **Note:** Standardized header for all major section landing pages.

### Overview Grid/Card
- **Structure:** `<div class="overview-grid"><a class="overview-card" href="...">...</a></div>`
- **Note:** Primary navigation pattern for section sub-pages.

### Premium Card
- **Structure:** `<div class="premium-card"><h4>...</h4><ul>...</ul></div>`
- **Note:** High-quality card style used for skillsets, ventures, and features.

### AI Canvas (Rich Content Wrapper)
- **Structure:** `<div class="ai-canvas">...</div>`
- **Note:** Used for dark-themed, dashboard-style diagnostic and architectural reports.

## 3. DO NOT COMPONENTIZE

| Pattern Name | Reason |
| :--- | :--- |
| **Page-specific inline styles** | Styles used only once for a very specific visualization (e.g., custom gradients in `ayurveda-knowledge-os.astro`). |
| **One-off MDX layouts** | Simple Markdown structures that don't benefit from the overhead of a dedicated component. |
| **Temporary migration backups** | Anything inside `mkdocs_old/` is excluded from the componentization roadmap. |

## 4. NEXT STEPS
- [ ] Create `src/components/` directory.
- [ ] Migrate `CategoryHero.astro` first (highest immediate reuse).
- [ ] Refactor `src/layouts/Layout.astro` to use a dedicated `Navigation.astro` component.
- [ ] Standardize `PremiumCard.astro` for use across both MDX and Astro pages.
