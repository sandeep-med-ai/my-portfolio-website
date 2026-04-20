# From Stethoscope to Scripts: Engineering an Automated AI Portfolio

> **A complete technical breakdown** of how I designed, built, and automated `drsandeep.allhelp.in` — from custom subdomain setup and static site architecture to a bespoke Python publishing engine and CI/CD pipeline.

`Python Automation` &nbsp;·&nbsp; `CI/CD` &nbsp;·&nbsp; `GitHub Actions` &nbsp;·&nbsp; `MkDocs` &nbsp;·&nbsp; `DevOps` &nbsp;·&nbsp; `Static Site` &nbsp;·&nbsp; `Custom Domain` &nbsp;·&nbsp; `Workflow Optimization`

---

## The Premise

Medicine and engineering share a common foundation: precision, systematic thinking, and the relentless drive to optimize complex systems. When I decided to establish a serious digital presence for my AI and automation work, the obvious path — a drag-and-drop website builder — felt immediately limiting.

What I wanted was not a static brochure. I wanted a **living, version-controlled, continuously deployed documentation engine** that would itself demonstrate the very skills it was meant to showcase. The result is `drsandeep.allhelp.in` — and this post is a complete technical breakdown of how it was built.

---

## Phase 1 — Custom Subdomain & Hosting Strategy

The first decision was infrastructure. Rather than starting from scratch with a new domain, I chose to extend the existing `allhelp.in` domain by configuring a dedicated subdomain: `drsandeep.allhelp.in`.

### DNS Configuration

- Configured **CNAME records** at the DNS provider level to map the subdomain to GitHub Pages infrastructure
- Enforced **HTTPS** through GitHub's security settings — a non-negotiable baseline for any professional web property
- Verified propagation and resolved DNS caching delays before proceeding to the build phase

### Why GitHub Pages

- **Zero cost** for hosting static sites — no monthly server fees, no infrastructure overhead
- **Native Git integration** — the deployment target lives inside the same repository as the source, making version control the single source of truth
- **High availability** backed by GitHub's CDN infrastructure
- Pairs seamlessly with **GitHub Actions** for automated deployments — a critical requirement from the start

---

## Phase 2 — Tech Stack Selection & Bespoke Design

### Choosing a Static Site Generator

The choice of a **Static Site Generator (SSG)** over a traditional CMS like WordPress was deliberate and architectural:

- **Speed** — no database queries, no backend rendering; pages are pre-compiled HTML served directly from a CDN
- **Security** — no attack surface from server-side scripts or plugin vulnerabilities
- **Developer-native workflow** — content written in Markdown, configuration in YAML, everything tracked in Git
- **CI/CD-ready** — static sites build deterministically, making automated pipelines trivial to construct

I selected **MkDocs with the Material theme** — an industry-standard combination for technical documentation that offers sophisticated navigation, search, mobile responsiveness, and extensive customization hooks out of the box.

### Tech Stack at a Glance

| Layer | Choice |
|---|---|
| **Framework** | MkDocs + Material Theme |
| **Content Format** | Markdown + YAML |
| **Hosting** | GitHub Pages |
| **CI/CD Engine** | GitHub Actions |
| **Custom Automation** | Python (bespoke) |
| **Domain Layer** | Custom DNS + CNAME |

### Brand Identity & Custom CSS

Recognizing that design is part of the signal, I went beyond the default Material theme and built a coherent visual identity using custom CSS overrides:

| Swatch | Name | Hex | Role |
|---|---|---|---|
| 🟦 | **Midnight Navy** | `#0B132B` | Headers & navigation |
| ⬜ | **Soft Ivory** | `#FAF9F6` | Primary background |
| 🟨 | **Luxury Gold** | `#D4AF37` | Structural accents |
| 🔵 | **Electric Cyan** | `#00E5FF` | Interactive elements & CTAs |

Every color decision was intentional — the palette is consistent across diagrams, navigation, and interactive elements, ensuring the site reads as a considered, unified product rather than an assembled template.

---

## Phase 3 — Automation Architecture: Where It Gets Interesting

This phase is the technical core of the project. The goal was unambiguous: **eliminate all manual deployment steps entirely**. Writing and publishing a new post should require zero terminal commands and zero configuration edits.

### CI/CD Pipeline via GitHub Actions

I wrote a custom `.yml` workflow that acts as the central nervous system of the entire deployment cycle. Every push to the `main` branch triggers the following automated sequence:

- Spins up a clean **Ubuntu virtual environment** in the cloud
- Provisions **Python 3.x** and installs the exact MkDocs Material dependencies from the requirements file
- Compiles raw Markdown and YAML into a complete set of optimized, static HTML files
- Executes a **force-push** of the compiled site to the `gh-pages` branch, managing branch history cleanly
- The live site at `drsandeep.allhelp.in` reflects the update within minutes — with no manual intervention

!!! note "Permission Note"
    Configuring `contents: write` permissions correctly in the workflow was a non-trivial step — a common stumbling block that I debugged by carefully reading GitHub Actions logs and understanding the security model around branch-level write access.

### Overcoming YAML's Strict Constraints

MkDocs navigation is defined in a YAML file — and YAML is notoriously unforgiving. A single misplaced space in the indentation tree triggers a catastrophic build failure:

- Errors like `expected <block end>, but found '<block sequence start>'` appear with no obvious line-level context in simple editors
- Resolved these by **deep-diving GitHub Actions logs**, using VS Code's YAML extension for real-time validation, and restructuring the navigation tree for complex nested categories like *Clinical Intelligence* and *HealthTech Studies*
- Ultimately treated YAML debugging as a systems discipline — tracing symptoms back to root causes rather than trial-and-error patching

### Custom Publishing Tool — `publishtmlGit.py`

This is the standout innovation of the project. Even with CI/CD automating deployment, the act of *creating* a new page still involved manual steps: creating the right folder, naming the file correctly, updating the YAML navigation, generating `.pages` config files. Each step was a potential source of error and friction.

**So I built a tool to eliminate all of it.**

- **Prompts** the user for just three inputs: category, page title, and HTML content
- **Auto-creates** the correct folder structure if it doesn't already exist
- **Generates** all required MkDocs menu configuration files (`.pages` files) automatically
- **Wraps** the HTML content in the correct Markdown scaffolding and saves it to the right location as a clean `.md` file
- **Result:** zero manual configuration — the workflow is now:

```
Write content  →  Run script  →  Push to Git  →  Live in minutes
```

!!! tip "Why This Matters"
    Building a tool to remove your own friction is a meaningful signal. It reflects an understanding that sustainable productivity comes from systematic process improvement — not from working harder at repetitive tasks.

**Impact Summary:**

✅ &nbsp; Zero-touch deployment &nbsp;&nbsp;
✅ &nbsp; No configuration errors &nbsp;&nbsp;
✅ &nbsp; Consistent folder structure &nbsp;&nbsp;
✅ &nbsp; Scales instantly with new content &nbsp;&nbsp;
✅ &nbsp; Custom Python tooling

---

## Phase 4 — Results & What's Next

The combined effect of all three automation layers — CI/CD pipeline, YAML debugging discipline, and the custom publisher — is a documentation engine that stays entirely out of the way:

- **0 terminal commands** required to publish new content end-to-end
- **Sub-second page loads** — no databases, no backend rendering, just static HTML from a CDN
- **Infinitely scalable** — whether pushing a 10-page research paper or a 3-line observation, the pipeline handles it identically
- **Fully version-controlled** — every change is tracked, reversible, and auditable through Git history

### On the Roadmap

| Feature | Description |
|---|---|
| ◈ **Automated diagram generation** | Mermaid.js integration — diagrams produced from structured data, not drawn by hand |
| ◈ **Intelligent tagging system** | Automatic classification of content across categories using NLP |
| ◈ **LangGraph-powered summarization** | A local LLM gateway that auto-generates post summaries and insight extracts on each publish |
| ◈ **Telegram bot integration** | Push new content directly from a chat interface; the bot handles the pipeline end-to-end |

---

## Closing Thoughts

> *There is a unique beauty in writing code that automates your own life.*

Building `drsandeep.allhelp.in` was never just a portfolio project. It was an exercise in **systems thinking** — identifying every manual step, understanding why it existed, and deciding whether to eliminate it, automate it, or accept it. Most steps turned out to be eliminable.

The most satisfying moment in any automated pipeline is the one where it runs cleanly without your involvement. That **green tick** in GitHub Actions, appearing seconds after a push, is the payoff for all the architecture decisions made upstream.

The platform will keep evolving. But the foundation — robust, automated, and built to get out of the way — is solid. I am a doctor by training, but I am a builder by passion.

---

*`drsandeep.allhelp.in` &nbsp;·&nbsp; AI Projects &nbsp;·&nbsp; Build Log*<img width="1440" height="10014" alt="image" src="https://github.com/user-attachments/assets/a1c75a93-c6bb-46fb-bf64-9aa7744a3075" />
