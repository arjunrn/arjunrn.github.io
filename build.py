#!/usr/bin/env python3
"""Build resume.html and resume.pdf from resume.md and resume.css."""

import os
import re
import sys

import markdown
import weasyprint


PREAMBLE = """\
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<div id="resume">
"""

POSTAMBLE = """\
</div>
</body>
</html>
"""


def title(md: str) -> str:
    for line in md.splitlines():
        if re.match(r"^#[^#]", line):
            return line.lstrip("#").strip()
    raise ValueError("Cannot find a markdown h1 heading to use as the title")


def build(prefix: str = "resume") -> None:
    md_path = prefix + ".md"
    css_path = prefix + ".css"

    with open(md_path, encoding="utf-8") as f:
        md = f.read()

    try:
        with open(css_path, encoding="utf-8") as f:
            css = f.read()
    except FileNotFoundError:
        print(f"{css_path} not found. Output will be unstyled.", file=sys.stderr)
        css = ""

    body = markdown.markdown(md, extensions=["smarty", "abbr"])
    html = PREAMBLE.format(title=title(md), css=css) + body + POSTAMBLE

    html_path = os.path.abspath(prefix + ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {html_path}")

    pdf_path = os.path.abspath(prefix + ".pdf")
    weasyprint.HTML(string=html).write_pdf(pdf_path)
    print(f"Wrote {pdf_path}")


if __name__ == "__main__":
    prefix = sys.argv[1] if len(sys.argv) > 1 else "resume"
    build(prefix)
