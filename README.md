# Hongkun Dou (窦泓焜) — Academic Homepage

Personal academic website based on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template.

## Quick start (local preview)

```bash
# Ruby + Bundler required
bundle install
bundle exec jekyll serve
```

Then open <http://127.0.0.1:4000>.

## Deploy to GitHub Pages

1. Create a GitHub repository named `YOUR_USERNAME.github.io` (or any repo with GitHub Pages enabled).
2. In `_config.yml`, update:
   - `url` → `https://YOUR_USERNAME.github.io`
   - `repository` → `YOUR_USERNAME/YOUR_USERNAME.github.io`
   - optionally `author.github` / `author.googlescholar`
3. Push this site to the repository’s default branch (or `gh-pages`, depending on your Pages settings).
4. Replace `images/profile.png` with your photo.

## Site structure

| Path | Content |
|------|---------|
| `_config.yml` | Site-wide settings & sidebar profile |
| `_pages/about.md` | Home / About |
| `_pages/research.md` | Research projects |
| `_pages/cv.md` | CV |
| `_publications/` | Papers (journals & conferences) |
| `files/CV_Dou_Hongkun.pdf` | Downloadable CV |

Navigation: **Publications · Research · CV**
