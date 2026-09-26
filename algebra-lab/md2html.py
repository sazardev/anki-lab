#!/usr/bin/env python3
"""Render CHEATSHEET.md to a self-contained HTML page with MathJax.

Omarchy opens .md files in a plain text editor, so the LaTeX shows up as raw
source. This turns the Markdown into HTML with MathJax so $...$ and $$...$$
render properly in the browser.

MathJax is loaded from a CDN. If you want it fully offline, drop
mathjax/ under this directory and change the script src to ./mathjax/tex-mml-chtml.js.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent / "CHEATSHEET.md"
OUT = Path(__file__).resolve().parent / "cheatsheet.html"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Algebra Rules Bible</title>
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['\\\\(', '\\\\)']],
      displayMath: [['\\\\[', '\\\\]'], ['$$', '$$']],
      processEscapes: true
    },
    options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre'] }
  };
</script>
<!-- Local MathJax first (works offline); CDN only as a fallback. -->
<script defer src="./mathjax/tex-chtml-full.js"></script>
<script>
  if (!window.MathJax || !window.MathJax.version) {
    document.write('<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"><\\/script>');
  }
</script>
<style>
  :root {
    --bg: #14161a; --fg: #d7dae0; --dim: #8b929e; --rule: #262a31;
    --acc: #7aa2f7; --warn: #e0af68; --code: #1c1f26;
  }
  @media (prefers-color-scheme: light) {
    :root { --bg:#fbfbfd; --fg:#1a1c20; --dim:#5c6370; --rule:#e3e6ea;
            --acc:#2f5fd0; --warn:#8a6100; --code:#f2f4f7; }
  }
  body {
    background: var(--bg); color: var(--fg); margin: 0;
    font: 16px/1.65 -apple-system, "GeistMono Nerd Font", system-ui, sans-serif;
  }
  main { max-width: 46rem; margin: 0 auto; padding: 3rem 1.25rem 6rem; }
  h1 { font-size: 2rem; letter-spacing: -.02em; margin: 0 0 .3em; }
  h2 { font-size: 1.3rem; margin: 2.6em 0 .6em; padding-bottom: .3em;
       border-bottom: 1px solid var(--rule); }
  h3 { font-size: 1.05rem; margin: 1.9em 0 .5em; color: var(--acc); }
  p, li { color: var(--fg); }
  a { color: var(--acc); }
  strong { color: #fff; }
  @media (prefers-color-scheme: light) { strong { color: #000; } }
  code { background: var(--code); padding: .12em .38em; border-radius: 4px;
         font-family: "GeistMono Nerd Font", ui-monospace, monospace; font-size: .9em; }
  pre { background: var(--code); padding: 1rem; border-radius: 8px; overflow-x: auto; }
  pre code { background: none; padding: 0; }
  table { border-collapse: collapse; width: 100%; margin: 1.1em 0; font-size: .95em; }
  th, td { border: 1px solid var(--rule); padding: .5em .7em; text-align: left;
           vertical-align: top; }
  th { background: var(--code); font-weight: 600; }
  hr { border: 0; border-top: 1px solid var(--rule); margin: 2.5em 0; }
  blockquote { border-left: 3px solid var(--warn); margin: 1.2em 0;
               padding: .1em 0 .1em 1em; color: var(--dim); }
  mjx-container[display="true"] { margin: 1.1em 0 !important; overflow-x: auto; }
  .note { color: var(--dim); font-size: .88em; }
</style>
</head>
<body><main>
__BODY__
</main></body>
</html>
"""


def protect_math(md: str) -> tuple[str, list[str]]:
    """Replace math with placeholders so Markdown munging cannot touch it."""
    stash: list[str] = []
    # $$...$$ first, then \(...\) and \[...\]
    def keep(m: re.Match) -> str:
        stash.append(m.group(0))
        return f"\x00MATH{len(stash)-1}\x00"
    md = re.sub(r"\$\$.+?\$\$", keep, md, flags=re.S)
    md = re.sub(r"\\\[.+?\\\]", keep, md, flags=re.S)
    md = re.sub(r"\\\(.+?\\\)", keep, md, flags=re.S)
    md = re.sub(r"(?<!\$)\$[^$\n]+\$(?!\$)", keep, md)
    return md, stash


def to_mathjax(src: str) -> str:
    """Rewrite delimiters to the ones MathJax is configured for.

    The Markdown uses $...$ and $$...$$; MathJax is set up for \\( \\) and
    \\[ \\], so leaving the dollars in place would render nothing.
    """
    if src.startswith("$$") and src.endswith("$$"):
        return r"\[" + src[2:-2].strip() + r"\]"
    if src.startswith("$") and src.endswith("$") and len(src) > 1:
        return r"\(" + src[1:-1].strip() + r"\)"
    return src


def restore_math(text: str, stash: list[str]) -> str:
    def back(m: re.Match) -> str:
        return to_mathjax(stash[int(m.group(1))])
    return re.sub(r"\x00MATH(\d+)\x00", back, text)


def md_to_html(md: str) -> str:
    md, stash = protect_math(md)
    out: list[str] = []
    in_code = False
    para: list[str] = []
    quote: list[str] | None = None
    in_table = False
    for raw in md.splitlines():
        line = raw.rstrip()

        if line.startswith("```"):
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []
            if quote is not None:
                out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
                quote = None
            out.append("</pre>" if in_code else "<pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line))
            continue

        is_row = line.startswith("|") and line.endswith("|")
        if is_row:
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []
            if quote is not None:
                out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
                quote = None
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            tag = "th" if not in_table else "td"
            if not in_table:
                out.append("<table>")
                in_table = True
            # cells must go through inline() too, or **bold** and `code` show raw
            out.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
            continue
        if in_table:
            out.append("</table>")
            in_table = False

        if not line:
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []
            if quote is not None:
                out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
                quote = None
            out.append("")
            continue

        h = re.match(r"^(#{1,6})\s+(.*)", line)
        if h:
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []
            if quote is not None:
                out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
                quote = None
            lvl = len(h.group(1))
            out.append(f"<h{lvl}>{inline(h.group(2))}</h{lvl}>")
            continue

        if re.fullmatch(r"-{3,}|\*{3,}", line):
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []
            if quote is not None:
                out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
                quote = None
            out.append("<hr>")
            continue

        if line.startswith(">"):
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []
            if quote is not None:
                out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
                quote = None
            if quote is None:
                quote = []
            quote.append(line.lstrip("> ").strip())
            continue
        if quote is not None:
            out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
            quote = None

        li = re.match(r"^(\s*)(?:[-*+]|\d+[.)])\s+(.*)", line)
        if li:
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []
            if quote is not None:
                out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
                quote = None
            pad = "&nbsp;" * (len(li.group(1)) // 2)
            out.append(f"<li>{pad}{inline(li.group(2))}</li>")
            continue

        # Ordinary text: buffer it, because Markdown hard-wraps paragraphs and
        # each physical line is not its own paragraph.
        para.append(line.strip())

    if quote is not None:
        out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
    if para:
        out.append(f"<p>{inline(' '.join(para))}</p>")
    if in_table:
        out.append("</table>")
    if in_code:
        out.append("</pre>")
    return restore_math("\n".join(out), stash)


def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def main() -> int:
    if not SRC.exists():
        print(f"error: {SRC} not found", file=sys.stderr)
        return 1
    body = md_to_html(SRC.read_text())
    OUT.write_text(TEMPLATE.replace("__BODY__", body))
    n_math = body.count("MATH") + len(re.findall(r"\\[(()]", body))
    print(f"wrote {OUT}  ({len(OUT.read_text()) // 1024} KiB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
