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
    "posted": "September 14, 2026",
    "due": "Friday at 3:30 PM",
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
    {"number": 5, "title": "The seven bridges of the cafeteria", "topic": "Graph theory",
     "answer": "No such walk exists - four corners have odd degree."},
    {"number": 4, "title": "A rope around the equator", "topic": "Geometry",
     "answer": "About 16 cm, and it does not depend on the size of the planet."},
    {"number": 3, "title": "Three dice, one suspicious total", "topic": "Probability",
     "answer": "25/216"},
    {"number": 2, "title": "Why 1 is not prime", "topic": "Number theory",
     "answer": "Unique factorization would fail."},
    {"number": 1, "title": "Folding a strip of paper", "topic": "Sequences",
     "answer": "The dragon curve."},
]

# ---- What the club actually does -----------------------------
ABOUT = {
    "lead": (
        "Math Club is open to every student at "
        + SITE["school"]
        + ", whether you are in Algebra 1 or finishing BC Calculus. "
        "You do not need to be fast, and you do not need to compete."
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
    "when": "Thursdays, 3:15 - 4:30 PM",
    "where": "Room 205",
    "next_date": "Thursday, September 17",
    "next_topic": "Pigeonhole principle, and why it keeps showing up",
    "note": "Come late, leave early, bring food. Nobody takes attendance.",
}

# ---- Competition calendar (a real sequence, so it is dated) ---
COMPETITIONS = [
    {"date": "Nov 6", "name": "AMC 10/12 A", "detail": "Sign up with our faculty advisor by October 10. Free for members."},
    {"date": "Nov 12", "name": "AMC 10/12 B", "detail": "Alternate sitting if you have a conflict with the A date."},
    {"date": "Feb 5", "name": "AIME I", "detail": "Qualify through the AMC. We run two prep sessions in January."},
    {"date": "Mar 21", "name": "State Math League finals", "detail": "Team of six. Tryouts in February."},
    {"date": "May 30", "name": "Pi Day Puzzle Hunt", "detail": "We host it. Volunteers needed to write puzzles."},
]

# ---- Officers ------------------------------------------------
OFFICERS = [
    {"name": "WORK IN PROGRESS", "role": "President", "note": "Grade 12"},
    {"name": "WORK IN PROGRESS", "role": "Vice president", "note": "Grade 11"},
    {"name": "WORK IN PROGRESS", "role": "Treasurer", "note": "Grade 11"},
    {"name": "WORK IN PROGRESS", "role": "Faculty advisor", "note": "Room 205"},
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
        "Show up to any Thursday meeting in Room 205. That is the whole process.",
        "Add your name to the roster sheet so you get the weekly email.",
        "Optional: pay the $5 yearly dues, which cover contest fees and snacks.",
    ],
    "closing": "If you would rather ask a question first, email us.",
}
