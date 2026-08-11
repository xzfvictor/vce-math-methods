"""Fix takeaway escape counts in the generated scene files."""
import re
from pathlib import Path

Q = chr(34) * 3
pat = re.compile(r"\b(takeaway_eq|takeaway_sub)=r" + Q + r"(.*?)" + Q, re.DOTALL)
for p in Path("scripts/videos").glob("m10-*.py"):
    text = p.read_text()
    original = text

    def repl(m):
        key = m.group(1)
        val = m.group(2)
        # Collapse 4 backslashes (which Python sees as 2 chars) into 2
        # backslashes (which Python sees as 1 char) so the runtime value
        # is a single-backslash LaTeX command.
        val = val.replace(chr(92) * 4, chr(92) * 2)
        return f"{key}=r{Q}{val}{Q}"

    text = pat.sub(repl, text)
    if text != original:
        p.write_text(text)
        print(f"updated {p.name}")
