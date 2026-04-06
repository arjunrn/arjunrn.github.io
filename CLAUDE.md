# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A personal resume authored in Markdown (`resume.md`) and styled with CSS (`resume.css`), converted to HTML and PDF using `build.py` (powered by `python-markdown` and `weasyprint`). The resume is deployed to GitHub Pages on push to `main`.

## Build Commands

```bash
uv sync                    # Install dependencies
uv run python build.py     # Build resume.html and resume.pdf
```

## Key Files

- `resume.md` — Resume content in Markdown. Uses `<span>` elements inside `h3` for flexbox layout of job title + date range.
- `resume.css` — Styling for both screen and print/PDF. The CSS relies on structural selectors (e.g., `h1 + ul` for contact list, `h1 + ul + p` for summary) so Markdown heading order matters.
- `build.py` — Build script that converts Markdown to HTML and PDF using `python-markdown` and `weasyprint`.
- `pyproject.toml` — Declares dependencies (`markdown`, `weasyprint`). Uses `uv` for dependency management.

## CI/CD

- **`.github/workflows/build.yml`** — On push to `main`: builds resume, deploys HTML + PDF to GitHub Pages.
- **`.github/workflows/pr.yml`** — On PRs: builds resume, uploads PDF artifact, posts/updates a bot comment with download link.

## Resume Markdown Conventions

`build.py` converts `resume.md` to HTML wrapped in a `<div id="resume">` and injects `resume.css`. PDF is generated via WeasyPrint (no Chrome required). The Markdown structure follows a specific convention:

- `h1` = name, followed immediately by a `ul` for contact info
- The paragraph after the contact list is the summary
- `h2` = section headings (Experience, Education, Skills)
- `h3` = entries with `<span>Title</span> <span>Date Range</span>` for two-column layout
