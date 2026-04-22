# Gabriela Henriquez, Ph.D. — Personal Website

A clean, modern, static portfolio site for Gabriela Henriquez, Ph.D.

## Stack

Plain **HTML + CSS + a tiny vanilla JS** file. No build step. No framework runtime shipped to the client. Hosts anywhere static (GitHub Pages, Netlify, Cloudflare Pages, S3, etc.).

## Structure

```
.
├── index.html           # Single-page site
├── styles/main.css      # All styles (custom properties, responsive, accessible)
├── scripts/main.js      # Mobile nav + email obfuscation + footer year
├── assets/              # Source materials (résumé, etc.)
└── .github/copilot-instructions.md
```

## Local preview

No build is required. Just serve the directory with any static server, e.g.:

```bash
# Python
python -m http.server 8080

# Node
npx serve .
```

Then open <http://localhost:8080>.

## Deploy

### GitHub Pages
1. Push to GitHub.
2. Settings → Pages → **Deploy from a branch** → `main` / root.
3. Your site will be live at `https://<user>.github.io/<repo>/`.

### Netlify / Cloudflare Pages / Vercel
Drop the repo in — no build command, publish directory is the project root.

## Editing content

All copy lives in `index.html`. The visual system uses CSS custom properties at the top of `styles/main.css` (colors, radii, spacing) — adjust there for theme tweaks.

## Notes

- Résumé download link points to `assets/Gabriela Henriquez_Resume.docx`. To offer a PDF, drop `Gabriela_Henriquez_Resume.pdf` into `assets/` and update the two links in `index.html`.
- Email is lightly obfuscated client-side and falls back to `noscript` text.
- Publication list is curated; full list links out to Google Scholar.
