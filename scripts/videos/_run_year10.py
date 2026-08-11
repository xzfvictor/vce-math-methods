#!/usr/bin/env python3
"""Build and render all 77 Year 10 Manim scenes from one source of truth.

Steps:
  1. Generate scene files from SCENES (algebra + measurement + number + space + statistics + probability).
  2. Build per-shard render scripts.
  3. Run each shard in a separate Docker call.
"""
from __future__ import annotations
import os
import subprocess
from pathlib import Path

ROOT = Path("/home/victor/maths-decoded")
OUT = ROOT / "scripts/videos"
AUDIO = ROOT / "public/audio/lessons"


# Each entry: (title, subtitle, beats, takeaway_eq, takeaway_sub, audio_seconds)
# This dict is split across three files for editing but merged here.
def _build_part1():
    """Algebra + measurement + number."""
    return {
        "m10-algebra-factorisation/common-factor": (
            "Common factor",
            "Pull the greatest thing out the front.",
            [
                [("6x^{2} + 9x", "BLUE_TERM", 1.05, (-3.0, 1.3, 0.0), "two terms", "ORANGE_TERM", 1.6, 1.2),
                 (r"\text{GCD}(6,9)=3", "ORANGE_TERM", 0.95, (3.0, 1.3, 0.0), "numerical part", None, 1.6, 1.2),
                 (r"\text{lowest power of } x = x", "GREEN_OK", 0.9, (-3.0, -0.4, 0.0), "variable part", None, 1.8, 1.2),
                 (r"\text{GCF} = 3x", "GREEN_OK", 1.1, (3.0, -0.4, 0.0), "combine", None, 1.6, 1.4)],
                [(r"6x^{2} + 9x = 3x(2x + 3)", "GREEN_OK", 1.2, (0, 1.2, 0.0), "pull 3x out the front", "BLUE_TERM", 2.0, 2.0),
                 (r"\dfrac{6x^{2}}{3x}=2x,\;\dfrac{9x}{3x}=3", "ORANGE_TERM", 0.9, (0, -0.4, 0.0), "divide each term", None, 1.8, 1.6)],
                [(r"3(2x+3) \;\neq\; 3x(2x+3)", "RED_REJECT", 1.0, (0, 1.2, 0.0), "missing the variable x", "BLUE_TERM", 1.6, 1.2),
                 (r"\text{always include }x\text{ if every term has }x", "GREEN_OK", 0.85, (0, -0.4, 0.0), "rule", None, 1.6, 1.6)],
            ],
            r"ab+ac=a(b+c)",
            "Pull out the greatest common factor; expand to check.",
            99.6,
        ),
        "m10-algebra-factorisation/grouping-in-pairs": (
            "Grouping in pairs",
            "Factor each pair, then pull out the common bracket.",
            [
                [(r"x^{2}+3x+xy+3y", "BLUE_TERM", 1.1, (0, 1.4, 0.0), "four terms", "ORANGE_TERM", 1.8, 1.4)],
                [(r"(x^{2}+3x)+(xy+3y)", "ORANGE_TERM", 1.05, (0, 1.4, 0.0), "group into pairs", None, 1.8, 1.2),
                 (r"x(x+3) + y(x+3)", "GREEN_OK", 1.05, (0, 0.0, 0.0), "factor each pair", None, 1.8, 1.2),
                 (r"(x+3)(x+y)", "GREEN_OK", 1.15, (0, -1.2, 0.0), "pull out the common bracket", None, 1.8, 2.0)],
                [(r"ab + 2a + 3b + 6", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "try again", None, 1.6, 1.0),
                 (r"(ab+2a)+(3b+6)=a(b+2)+3(b+2)", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "common bracket b+2", None, 1.8, 1.2),
                 (r"(b+2)(a+3)", "GREEN_OK", 1.1, (0, -1.2, 0.0), "final form", None, 1.6, 1.4)],
            ],
            r"a(b+c)+d(b+c) = (a+d)(b+c)",
            "Spot the common bracket across the two pair-factors.",
            81.9,
        ),
    }


# Build a single merged dict.
def _import_part2():
    import importlib.util
    spec = importlib.util.spec_from_file_location("p2", OUT / "_build_year10_part2.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SCENES


def _import_part3():
    import importlib.util
    spec = importlib.util.spec_from_file_location("p3", OUT / "_build_year10_part3.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SCENES


def _import_part1():
    import importlib.util
    spec = importlib.util.spec_from_file_location("p1", OUT / "_build_year10_pairs.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SCENES


def main():
    from pathlib import Path as P

    SCENES = {}
    SCENES.update(_import_part1())
    SCENES.update(_import_part2())
    SCENES.update(_import_part3())
    print(f"merged scenes: {len(SCENES)}")

    # Cross-check with audio
    audio_lessons = {(p.parent.name, p.stem) for p in (ROOT / "public/audio/lessons").glob("m10-*/*.json")}
    print(f"audio lessons: {len(audio_lessons)}")
    missing = []
    for topic, lesson in audio_lessons:
        key = f"{topic}/{lesson}"
        if key not in SCENES:
            missing.append(key)
    if missing:
        print(f"MISSING from SCENES: {missing}")
        raise SystemExit("incomplete")
    extras = [k for k in SCENES if (k.split("/")[0], k.split("/")[1]) not in audio_lessons]
    if extras:
        print(f"EXTRAS in SCENES: {extras}")
        raise SystemExit("incomplete")
    print("scene <-> audio coverage matches")

    # Build all scene files
    for key, (title, subtitle, beats, takeaway_eq, takeaway_sub, audio_seconds) in SCENES.items():
        topic, lesson = key.split("/", 1)
        stem = f"{topic}-{lesson}"
        cls = "".join(part[:1].upper() + part[1:] for part in stem.split("-")) + "Scene"
        out = OUT / f"{stem}.py"
        if out.exists():
            continue
        # Build Step(...) objects from tuple data.
        step_lines = []
        for beat in beats:
            inner = []
            for step in beat:
                if len(step) == 8:
                    text, color, scale, anchor, sub, sub_color, write_time, post_wait = step
                else:
                    raise SystemExit(f"bad step tuple: {step}")
                if sub is None:
                    sub_field = "None"
                else:
                    sub_field = repr(sub)
                if sub_color is None:
                    sub_color_field = "None"
                else:
                    sub_color_field = repr(sub_color)
                # Use raw triple-quoted strings so backslashes pass through.
                TQ = chr(39) * 3
                inner.append(
                    f"            Step(r{TQ}{text}{TQ}, color={color!r}, scale={scale!r}, "
                    f"anchor={anchor!r}, sub={sub_field}, sub_color={sub_color_field}, "
                    f"write_time={write_time!r}, post_wait={post_wait!r}, pre_wait=0.4)"
                )
            step_lines.append("        [\n" + ",\n".join(inner) + "\n        ]")
        beats_literal = "[\n" + ",\n".join(step_lines) + "\n    ]"
        # No-op: takeaways are written verbatim so the backslashes land in
        # the file as single characters, which Python parses into the same
        # single-backslash LaTeX source.
        take = takeaway_eq
        sub = takeaway_sub
        title_esc = title
        subtitle_esc = subtitle
        # Use chr(39)*3 delimiters so the inner text (which may contain
        # backslashes or apostrophes) doesn't conflict.
        Q = chr(39) * 3
        body = f'''"""Manim scene for lesson `{lesson}` (topic `{topic}`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class {cls}(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title={title_esc!r},
            subtitle={subtitle_esc!r},
            beats={beats_literal},
            takeaway_eq=r{Q}{take}{Q},
            takeaway_sub=r{Q}{sub}{Q},
            audio_seconds={audio_seconds},
        )
'''
        out.write_text(body)
    print(f"wrote {len(SCENES)} scene files")

    # Build shard render scripts
    pairs = []
    for key, _ in SCENES.items():
        topic, lesson = key.split("/", 1)
        stem = f"{topic}-{lesson}"
        cls = "".join(part[:1].upper() + part[1:] for part in stem.split("-")) + "Scene"
        pairs.append((topic, lesson, cls))

    def write(name, rows):
        with open(OUT / name, "w") as f:
            f.write("#!/usr/bin/env bash\nset -euo pipefail\n\n")
            f.write("for row in \\\n")
            for i, (t, l, c) in enumerate(rows):
                end = " \\\n" if i < len(rows) - 1 else "\n"
                f.write(f'  "{t}|{l}|{c}"{end}')
            f.write('do\n  IFS="|" read -r topic lesson cls <<< "$row"\n')
            f.write('  bash scripts/videos/_render.sh "scripts/videos/${topic}-${lesson}.py" "$cls" "$topic" "$lesson" ql\n')
            f.write("done\n")
        (OUT / name).chmod(0o755)

    write("_render_all_year10.sh", pairs)
    for shard in range(4):
        rows = [(t, l, c) for i, (t, l, c) in enumerate(pairs) if i % 4 == shard]
        write(f"_render_year10_{shard}.sh", rows)
    print("wrote render scripts")


if __name__ == "__main__":
    main()