# Resume

Markdown-based resume built with [resume-markdown](https://github.com/mikepqr/resume-markdown).

## Prerequisites

- Python >= 3.9
- [uv](https://docs.astral.sh/uv/)
- Google Chrome or Chromium (for PDF generation)

## Usage

Install dependencies:

    uv sync

Build HTML and PDF:

    uv run resume-markdown build

The output files are `resume.html` and `resume.pdf`.

## CI

On every push to `main`, a GitHub Actions workflow builds the resume and uploads the PDF as a workflow artifact.
On pull requests, the workflow validates that the resume builds successfully.
