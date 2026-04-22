# Copilot Instructions — Gabriela Henriquez, Ph.D. Personal Website

## Project Goal
Build a **clean, modern, professional static website** for **Gabriela Henriquez, Ph.D.** that makes a strong impression on prospective hiring managers in the biopharmaceutical / biotech industry (process development, R&D, gene therapy, cell & molecular biology).

The site is a **personal portfolio / academic CV** site — not an app. It must be:
- **Static** (deployable to GitHub Pages, Netlify, or any static host — no backend, no build-time secrets).
- **Fast, accessible (WCAG AA), and mobile-responsive.**
- **SEO-friendly** with proper meta tags, Open Graph, and structured data (`schema.org/Person`).
- **Polished and recruiter-friendly** — quiet, confident design; not flashy.

## About Gabriela
- **Name:** Gabriela Henriquez, Ph.D.
- **Location:** Seattle, WA
- **Email:** ghenriquez16@outlook.com
- **LinkedIn:** https://www.linkedin.com/in/gabriela-henriquezphd/
- **Google Scholar:** https://scholar.google.com/citations?user=QRzJqYUAAAAJ&hl=en
- **Background:** Early-career scientist; Ph.D. in Environmental Science & Engineering (UTEP). Experience in mammalian cell culture, flow cytometry, in vivo models, molecular biology, AAV process development (Bristol Myers Squibb intern), and GLP/GMP quality assurance (Seattle Children's Research Institute).
- **Career focus:** Biopharmaceutical process development, gene therapy, translational research.

## Required Site Sections
1. **Hero / About** — name, title ("Ph.D. Scientist — Biopharmaceutical Process Development"), short tagline, professional photo placeholder, contact CTAs (email, LinkedIn, Scholar, Resume PDF).
2. **Professional Summary** — concise narrative pulled from her resume.
3. **Experience** — BMS, Seattle Children's Research Institute, UTEP graduate research/teaching.
4. **Education** — Ph.D. (UTEP), B.S. (UTESA), Shoreline biotech/biomanufacturing certificates.
5. **Skills** — grouped: Cell & Molecular Biology; Equipment & Lab Operations; Data Management & Software.
6. **Publications** — pulled from / linked to Google Scholar profile.
7. **Contact** — email + LinkedIn + downloadable resume (PDF generated from `assets/Gabriela Henriquez_Resume.docx`).

## Tech & Style Guidelines
- **Stack:** Plain HTML + CSS + minimal vanilla JS, OR a lightweight static generator (Astro/Eleventy) if it improves maintainability. **No heavy frameworks** (no React/Next runtime shipped to the client unless strictly justified).
- **CSS:** Use a small, modern system — CSS custom properties, system font stack or one tasteful Google Font (e.g., Inter, Source Sans, or similar). Avoid Bootstrap-heavy looks.
- **Color palette:** Professional, restrained — neutral base (white/off-white, slate/charcoal text) with one accent color (suggest a muted teal or deep blue evoking science/biotech). Confirm with user before deviating.
- **Typography:** Clear hierarchy, generous spacing, readable line lengths (~65–75ch).
- **Accessibility:** Semantic HTML5, alt text, focus states, sufficient contrast, prefers-reduced-motion respected.
- **Performance:** No render-blocking JS; optimize/responsive images; lazy-load below-the-fold media.
- **Assets:** Source materials live in `assets/`. Generate a clean `Gabriela_Henriquez_Resume.pdf` from the `.docx` for download.
- **Deployment-ready:** Should work when served from the repo root or `/docs`. Include a `README.md` with local preview instructions.

## Content Rules
- Always present Gabriela professionally — third person on the site, factual, no embellishment beyond what the resume supports.
- Do **not** invent publications, dates, employers, or credentials. When in doubt, pull from the resume in `assets/` or her Google Scholar profile.
- Keep her email visible but obfuscated against simple scrapers (e.g., split spans or `mailto:` only).

## Working Conventions
- Keep the repository tidy: `index.html`, `assets/`, `styles/`, `scripts/` (only if needed), `resume/` for the PDF.
- Favor surgical edits; preserve existing files in `assets/` (source of truth for content).
- Before introducing a new dependency, framework, or build step, briefly justify why a lighter approach won't work.
