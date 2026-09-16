# Math Club site

A small Python program that builds your club's website. You edit one Python
file, run one command, and get a single `index.html` you can host anywhere for
free.

```
content.py            <- the only file you need to edit
build.py              <- run this to rebuild the site
templates/
  base.html           <- shared masthead, nav, footer
  index.html          <- Home page (problem of the week)
  about.html          <- About page (description, officers)
  schedule.html       <- Schedule page (meetings, competitions)
  archive.html        <- Archive page (past problems)
  join.html           <- Join page (how to join, resources)
  style.css.j2        <- colors, fonts, layout
docs/
  *.html              <- generated. Do not edit by hand; it gets overwritten.
```

The site is five separate pages (Home, About, Schedule, Archive, Join) sharing
one masthead and navigation bar, styled in a plain classic-minimalist look:
one serif typeface, no boxes or shadows, thin hairline rules between
sections.

## Running it

You need Python 3.9 or newer.

```bash
pip install -r requirements.txt
python build.py --serve
```

Then open http://localhost:8000. Stop it with Ctrl+C. Click through Home,
About, Schedule, Archive, and Join to check each page.

To rebuild without the preview server, just run `python build.py`.

## Changing the content

Open `content.py`. Everything on the page comes from that file: the club name,
the problem of the week, meeting times, the competition calendar, officers,
resources. Change a value, save, run `python build.py` again, refresh.

Posting a new problem each week is three edits:

1. Move the current problem into the top of the `ARCHIVE` list.
2. Replace `PROBLEM_OF_THE_WEEK` with the new one.
3. Run `python build.py` and push (see below).

Math symbols can be pasted straight into the text: √ π ≤ ≥ ≠ ∑ ∞ ° ² ³ ₁ ₂.
If you ever need real equation layout, add MathJax by putting this line just
before `</head>` in `templates/base.html` (it's shared by every page):

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js"></script>
```

Then you can write `\(x^2 + y^2 = r^2\)` inside any content string.

## Putting it online, free

**GitHub Pages** is the recommendation. It's free with no time limit, it never
sleeps, and it works with a school-owned domain later if you want one.

There's a workflow file already set up for you at
`.github/workflows/build.yml`. It makes GitHub run `python build.py` for you
automatically every time you save a change — so once it's turned on, you can
edit `content.py` directly on GitHub's website and never touch a terminal
again.

**One-time setup:**

1. Make a free GitHub account and create a repository named `math-club`.
2. Upload this whole folder to it, including the hidden `.github` folder
   (the web uploader's "Add file → Upload files" works, but make sure your
   file browser shows hidden folders when you select files to upload, or
   drag the whole unzipped project folder in at once).
3. In the repo, go to **Settings → Pages**.
4. Under "Build and deployment," set **Source** to **GitHub Actions** (not
   "Deploy from a branch" — that matters, since the workflow handles the
   build now).
5. Go to the **Actions** tab, and you should see a workflow run start
   automatically. Wait for the green checkmark (usually under a minute).
6. Your site is now at `https://YOUR-USERNAME.github.io/math-club/`.

**From then on, every edit is just:**

1. Open `content.py` on GitHub (click the file → pencil icon → edit).
2. Make your change, scroll down, click **Commit changes**.
3. Wait about a minute — check the **Actions** tab for a green checkmark.
4. Refresh your live site.

No more downloading, no more running `build.py`, no more re-uploading a
`docs` folder by hand. GitHub does the rebuild for you on every save.

You can still edit and preview locally the old way any time
(`python build.py --serve`) — that hasn't changed, it's just optional now.

### Other free options

- **Netlify** or **Cloudflare Pages** — drag the `docs` folder onto their
  dashboard. Also free and permanent. Good if you want a nicer URL.
- **PythonAnywhere** — free tier, and it runs actual Python on a server. Only
  worth it if you later want features that need a server, like a form members
  submit solutions through. A plain club site does not need this.

## One thing to check before launching

Ask your advisor before publishing student names or photos. Many schools have
rules about it. Listing first names and grade levels is usually fine; last
names and personal emails often aren't.
