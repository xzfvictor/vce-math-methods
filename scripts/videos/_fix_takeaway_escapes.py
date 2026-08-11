"""Fix the takeaway string escape counts in the generated scene files.

The source dict was collapsed from `\\\\d` (4 source backslashes = 2 in memory)
to `\\d` (2 source backslashes = 1 in memory). When the file was written
as `r"""\\d"""`, the raw string preserves the 2 source backslashes
verbatim, which means the runtime value is 2 backslashes (wrong for LaTeX).

We want the file to have 2 source backslashes per logical backslash so
that the runtime value is 1 backslash (correct LaTeX).
"""
from pathlib import Path
import re

for p in Path("scripts/videos").glob("m10-*.py"):
    text = p.read_text()
    original = text
    # Pattern: r"""..content.."""
    pattern = re.compile(r"(takeaway_eq|takeaway_sub)=r\"\"\"([\s\S]*?)\"\"\"")
    def repl(m):
        key = m.group(1)
        val = m.group(2)
        # Collapse 4 backslashes to 2 in raw strings.
        val = val.replace("\\\\\\\\", "\\\\")
        return f'{key}=r"""{val}"""'
    text = pattern.sub(repl, text)
    if text != original:
        p.write_text(text)
        print(f"updated {p.name}")
