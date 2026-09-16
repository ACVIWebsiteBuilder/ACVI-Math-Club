"""Build the Math Club site (multi-page).

Usage:
    python build.py          # writes docs/*.html
    python build.py --serve  # builds, then previews at http://localhost:8000
"""

import sys
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
OUTPUT = ROOT / "docs"

# page id -> template file
PAGES = {
    "home": "index.html",
    "about": "about.html",
    "schedule": "schedule.html",
    "archive": "archive.html",
    "join": "join.html",
}


def build() -> Path:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    stylesheet = (TEMPLATES / "style.css.j2").read_text(encoding="utf-8")

    common = dict(
        site=content.SITE,
        potw=content.PROBLEM_OF_THE_WEEK,
        archive=content.ARCHIVE,
        about=content.ABOUT,
        meetings=content.MEETINGS,
        competitions=content.COMPETITIONS,
        officers=content.OFFICERS,
        resources=content.RESOURCES,
        join=content.JOIN,
        stylesheet=stylesheet,
        base="",   # relative link prefix; same folder for all pages
    )

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    for page_id, template_name in PAGES.items():
        html = env.get_template(template_name).render(page=page_id, **common)
        (OUTPUT / template_name).write_text(html, encoding="utf-8")

    (OUTPUT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built {len(PAGES)} pages into {OUTPUT.relative_to(ROOT)}/")
    return OUTPUT / "index.html"


def serve() -> None:
    import http.server
    import socketserver
    import functools

    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler, directory=str(OUTPUT)
    )
    with socketserver.TCPServer(("", 8000), handler) as httpd:
        print("Preview at http://localhost:8000  (Ctrl+C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()
