# Resume

Markdown-based resume built with [python-markdown](https://python-markdown.github.io/) and [WeasyPrint](https://weasyprint.org/).

## Prerequisites

- Python >= 3.14
- [uv](https://docs.astral.sh/uv/)

## Usage

Install dependencies:

    uv sync

Build HTML and PDF:

    uv run python build.py

The output files are `resume.html` and `resume.pdf`.

## CI

On every push to `main`, a GitHub Actions workflow builds the resume and deploys it to GitHub Pages.
On pull requests, the workflow builds the resume and posts a comment with a link to download the PDF.
