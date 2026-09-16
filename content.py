# =============================================================
#  EDIT THIS FILE TO CHANGE YOUR SITE.
#  Everything below is placeholder content - swap in your own,
#  then run:  python build.py
# =============================================================

SITE = {
    "club_name": "Math Club",
    "school": "Anderson CVI",
    "tagline": "We meet every week to argue about problems that don't have obvious answers.",
    "email": "mathclub@andersoncvi.edu",
    "instagram": "",          # e.g. "riversidemathclub" - leave "" to hide
    "year": "2026-27",
    "founded": "1960",     # shown in the small line above the club name
}

# ---- The problem that opens the site -------------------------
# Keep it short enough to read in one breath. Unicode symbols work
# fine here: √ π ≤ ≥ ≠ ∑ ∞ ° ⌊ ⌋ ² ³ ₁ ₂
PROBLEM_OF_THE_WEEK = {
    "number": 6,
    "posted": "September 16, 2026",
    "due": "Wednesday at 12:15 PM",
    "difficulty": "Medium",      # Warm-up / Medium / Hard
    "statement": (
        "A 3 × 3 grid is filled with the numbers 1 through 9, each used once. "
        "Call a filling <em>balanced</em> if every row and every column has the "
        "same sum. How many balanced fillings are there?"
    ),
    "hint": (
        "Every row must sum to 15, since the nine numbers total 45. Start by "
        "asking which number has to sit in the center."
    ),
    "how_to_submit": "Drop your solution in the box outside Room 205, or email it to us.",
}

# ---- Past problems (newest first) ----------------------------
ARCHIVE = [
    {"number": 5, "title": "WIP", "topic": "WIP",
     "answer": "WIP"},
    {"number": 4, "title": "WIP",
     "answer": "WIP"},
    {"number": 3, "title": "WIP",
     "answer": "25/216"},
    {"number": 2, "title": "WIP", "topic": "WIP",
     "answer": "Unique factorization would fail."},
    {"number": 1, "title": "WIP", "topic": "WIP",
     "answer": "WIP"},
]

# ---- What the club actually does -----------------------------
ABOUT = {
    "lead": (
        "Math Club is open to every student at "
        + SITE["school"]
        + "You do not need to be fast, and you do not need to compete."
    ),
    "activities": [
        ("Problem sessions", "We put one problem on the board and work it out together. "
                             "Wrong turns are the useful part."),
        ("Contest practice", "Timed sets from old AMC and ARML papers for anyone who wants them."),
        ("Talks", "Short student talks on something you found interesting. "
                  "Fifteen minutes, no slides required."),
        ("Peer tutoring", "Members tutor underclassmen during lunch on Wednesdays."),
    ],
}

# ---- Meetings ------------------------------------------------
MEETINGS = {
    "when": "Wednesday, 12:15 - 12:50 PM",
    "where": "Room 205",
    "next_date": "Wednesday, September 23",
    "next_topic": "WIP",
    "note": "WIP",
}

# ---- Competition calendar (a real sequence, so it is dated) ---
COMPETITIONS = [
    {"date": "WIP", "name": "WIP", "detail": "WIP"},
    {"date": "WIP", "name": "WIP", "detail": "WIP"},
    {"date": "WIP", "name": "WIP", "detail": "WIP"},
    {"date": "WIP", "name": "WIPs", "detail": "WIP"},
    {"date": "WIP", "name": "WIP", "detail": "WIP"},
]

# ---- Officers ------------------------------------------------
OFFICERS = [
    {"name": "WORK IN PROGRESS", "role": "WIP", "note": "WIP"},
    {"name": "WORK IN PROGRESS", "role": "WIP", "note": "WIP"},
    {"name": "WORK IN PROGRESS", "role": "WIP", "note": "WIP"},
    {"name": "WORK IN PROGRESS", "role": "WIP", "note": "Room 205"},
]

# ---- Resources -----------------------------------------------
RESOURCES = [
    {"name": "Art of Problem Solving", "url": "https://artofproblemsolving.com",
     "note": "Forums, textbooks, and every past AMC problem with solutions."},
    {"name": "Past AMC problems", "url": "https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions",
     "note": "Sorted by year and difficulty."},
    {"name": "Project Euler", "url": "https://projecteuler.net",
     "note": "Math problems you solve by writing code."},
    {"name": "3Blue1Brown", "url": "https://www.3blue1brown.com",
     "note": "Visual explanations of ideas you will meet later in high school."},
    {"name": "Our shared folder", "url": "#",
     "note": "Replace this link with your club's Drive folder of notes and past sets."},
]

# ---- Joining -------------------------------------------------
JOIN = {
    "steps": [
        "Show up to any Wednesday meeting in Room 205. That is the whole process.",
    ],
    "closing": "Go ahead and email us",
}
