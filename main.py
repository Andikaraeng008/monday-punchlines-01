"""Monday Morning Punchlines — make.fun entry.

Writes one Monday-morning joke (at most 200 characters) to /output/entry.txt.
Concrete scene: the narrator tells the bed five more minutes on Monday morning.
Twist: the bed believes it so hard it files the narrator as missing until noon.
"""

import os

LINE = "I told my bed I'd only lie down for five more minutes on Monday morning. It believed me so hard it filed me as missing until noon."

# Gate: entry must be UTF-8 text of 1 to 200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry violates the 1-200 character gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
