"""Monday Morning Punchlines — make.fun entry.

Writes one Monday-morning joke (at most 200 characters) to /output/entry.txt.
Concrete scene: the office printer finally works on a Monday morning.
Twist: it prints, signs and delivers the narrator's resignation letter
to HR before the narrator even arrives.
"""

import os

LINE = "Monday morning, my alarm went off, my coffee went cold, and my laptop updated itself — the only thing in this office that actually works on a Monday is the update nobody asked for."

# Gate: entry must be UTF-8 text of 1 to 200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry violates the 1-200 character gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
