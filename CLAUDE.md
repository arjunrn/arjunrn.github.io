# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A personal resume authored in Markdown (`resume.md`) and styled with CSS (`resume.css`), converted to HTML and PDF using the [resume-markdown](https://github.com/mikepqr/resume-markdown) tool. The resume is deployed to GitHub Pages on push to `main`.

## Build Commands

```bash
uv sync                       # Install dependencies
uv run resume-markdown build  # Build resume.html and resume.pdf (requires Chrome/Chromium)
```

## Key Files

- `resume.md` — Resume content in Markdown. Uses `<span>` elements inside `h3` for flexbox layout of job title + date range.
- `resume.css` — Styling for both screen and print/PDF. The CSS relies on structural selectors (e.g., `h1 + ul` for contact list, `h1 + ul + p` for summary) so Markdown heading order matters.
- `pyproject.toml` — Declares the single dependency (`resume-markdown`). Uses `uv` for dependency management.

## CI/CD

- **`.github/workflows/build.yml`** — On push to `main`: builds resume, deploys HTML + PDF to GitHub Pages.
- **`.github/workflows/pr.yml`** — On PRs: builds resume, uploads PDF artifact, posts/updates a bot comment with download link.

## Resume Markdown Conventions

The `resume-markdown` tool converts `resume.md` to HTML wrapped in a `<div id="resume">` and injects `resume.css`. PDF is generated via headless Chrome. The Markdown structure follows a specific convention:

- `h1` = name, followed immediately by a `ul` for contact info
- The paragraph after the contact list is the summary
- `h2` = section headings (Experience, Education, Skills)
- `h3` = entries with `<span>Title</span> <span>Date Range</span>` for two-column layout
