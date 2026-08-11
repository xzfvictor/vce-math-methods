#!/usr/bin/env python3
"""Build the rest of the Year 10 scenes (measurement, number, space, statistics, probability)."""
from __future__ import annotations
from pathlib import Path

ROOT = Path("/home/victor/maths-decoded")
OUT = ROOT / "scripts/videos"


SCENES: dict[str, tuple] = {
    "m10-measurement-area-volume/surface-area": (
        "Surface area",
        "Add up every face's area.",
        [
            [("rectangular prism", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "3 pairs of faces", "ORANGE_TERM", 1.6, 1.2)],
            [("length=4,\\;width=3,\\;height=2", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "dimensions", None, 1.4, 1.0),
             ("top+bottom = 2(4\\cdot 3) = 24", "ORANGE_TERM", 0.9, (0, 0.0, 0.0), "pair of faces", None, 1.8, 1.2),
             ("front+back = 2(4\\cdot 2) = 16", "ORANGE_TERM", 0.9, (0, -1.0, 0.0), "another pair", None, 1.8, 1.0),
             ("sides = 2(3\\cdot 2) = 12", "ORANGE_TERM", 0.9, (0, -2.0, 0.0), "third pair", None, 1.6, 1.0),
             ("surface area = 24+16+12 = 52", "GREEN_OK", 1.05, (0, -3.0, 0.0), "total", None, 1.8, 1.4)],
            [("sphere: SA = 4\\pi r^{2}", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "curved surface", None, 1.4, 1.0),
             ("cylinder: SA = 2\\pi r^{2} + 2\\pi r h", "GREEN_OK", 0.9, (0, -0.2, 0.0), "two circles plus rectangle", None, 1.8, 1.4)],
        ],
        "SA_{\text{box}}=2(lw+lh+wh)",
        "Surface area = sum of the areas of every face.",
        88.2,
    ),
    "m10-measurement-area-volume/volume": (
        "Volume",
        "Length × cross-section area.",
        [
            [("V = \\text{base area} \\times \\text{height}", "BLUE_TERM", 1.05, (0, 1.4, 0.0), "prism rule", "ORANGE_TERM", 1.6, 1.4)],
            [("V = l\\times w\\times h", "BLUE_TERM", 1.05, (0, 1.2, 0.0), "rectangular prism", None, 1.4, 1.0),
             ("l=4,\\;w=3,\\;h=2 \\Rightarrow V=24", "GREEN_OK", 1.0, (0, 0.0, 0.0), "example", None, 1.6, 1.4),
             ("V = \\pi r^{2} h", "ORANGE_TERM", 1.0, (0, -1.2, 0.0), "cylinder", None, 1.4, 1.0),
             ("V = \\tfrac{1}{3}\\pi r^{2} h", "GREEN_OK", 1.0, (0, -2.2, 0.0), "cone", None, 1.4, 1.4)],
            [("V = \\tfrac{4}{3}\\pi r^{3}", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "sphere", None, 1.4, 1.0),
             ("r=3 \\Rightarrow V = 36\\pi", "GREEN_OK", 1.0, (0, -0.4, 0.0), "evaluate", None, 1.4, 1.6)],
        ],
        "V=\text{base area}\times \text{height}",
        "Volume = area of the base times the perpendicular height.",
        83.7,
    ),
    "m10-measurement-log-scales/reading-scale": (
        "Read a log scale",
        "Each gridline jumps by a power of the base.",
        [
            [("pH scale", "BLUE_TERM", 1.1, (0, 1.4, 0.0), "logarithmic axis", "ORANGE_TERM", 1.4, 1.2),
             ("each step = x10 concentration", "GREEN_OK", 0.9, (0, 0.4, 0.0), "powers of 10", None, 1.6, 1.2)],
            [("pH=3", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "position 3", None, 1.2, 1.0),
             ("=10^{-3} M", "GREEN_OK", 1.0, (0, 0.0, 0.0), "convert", None, 1.4, 1.4),
             ("pH=5", "BLUE_TERM", 1.0, (0, -1.2, 0.0), "two steps to the right", None, 1.2, 1.0),
             ("=10^{-5} M \\;\\text{(100x less)}", "GREEN_OK", 0.9, (0, -2.2, 0.0), "two orders of magnitude", None, 1.6, 1.4)],
            [("Richter scale: each +1 \\Rightarrow \\times 10", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "log10 axis", None, 1.4, 1.0),
             ("magnitude 5 vs magnitude 7", "ORANGE_TERM", 0.9, (0, 0.0, 0.0), "compare", None, 1.4, 1.0),
             ("magnitude 7 \\Rightarrow 100\\times energy", "GREEN_OK", 0.9, (0, -1.2, 0.0), "factor of 100", None, 1.6, 1.4)],
        ],
        "\log_{10}\text{ scale: each tick} = \times 10",
        "Each major tick on a log scale multiplies by the base.",
        88.2,
    ),
    "m10-measurement-log-scales/real-world": (
        "Log scales in the real world",
        "They compress huge ranges onto a single chart.",
        [
            [("sound intensity (dB)", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "log10 axis", "ORANGE_TERM", 1.4, 1.0),
             ("pH (acidity)", "BLUE_TERM", 1.0, (0, 0.4, 0.0), "log10 axis", None, 1.4, 1.0),
             ("Richter (earthquake)", "BLUE_TERM", 1.0, (0, -0.6, 0.0), "log10 axis", None, 1.4, 1.0)],
            [("whisper ~ 30 dB", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "quiet", None, 1.2, 1.0),
             ("rock concert ~ 110 dB", "ORANGE_TERM", 0.9, (0, 0.0, 0.0), "loud", None, 1.4, 1.0),
             ("ratio = 10^{8}", "GREEN_OK", 1.0, (0, -1.2, 0.0), "intensity ratio", None, 1.6, 1.4),
             ("dB = 10\\log_{10}\\dfrac{I}{I_0}", "GREEN_OK", 0.9, (0, -2.2, 0.0), "definition", None, 1.8, 1.4)],
            [("log scale lets huge numbers fit on one chart", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "takeaway", None, 1.6, 1.4)],
        ],
        "\text{log scale: each tick is a power of the base}",
        "Log scales compress wide-ranging data so small and huge values fit together.",
        82.6,
    ),
    "m10-measurement-scaling/scale": (
        "Linear scale factor",
        "Lengths scale by k, areas by k^2, volumes by k^3.",
        [
            [("scale factor k", "BLUE_TERM", 1.1, (0, 1.4, 0.0), "one dimension", "ORANGE_TERM", 1.4, 1.2)],
            [("length = k \\cdot L", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "linear", None, 1.4, 1.0),
             ("area = k^{2} \\cdot A", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "2D", None, 1.4, 1.0),
             ("volume = k^{3} \\cdot V", "GREEN_OK", 1.0, (0, -1.2, 0.0), "3D", None, 1.4, 1.4)],
            [("k=2: length \\times 2", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "example", None, 1.4, 1.0),
             ("area = 4\\cdot A,\\; volume = 8\\cdot V", "GREEN_OK", 0.9, (0, 0.0, 0.0), "k^{2}=4,\\;k^{3}=8", None, 1.6, 1.6)],
        ],
        "\text{length }k,\;\text{area }k^{2},\;\text{volume }k^{3}",
        "Linear: k. Area: k². Volume: k³.",
        77.4,
    ),
    "m10-measurement-scaling/proportion": (
        "Direct proportion",
        "When one doubles, the other doubles too.",
        [
            [("y = kx", "BLUE_TERM", 1.1, (0, 1.4, 0.0), "directly proportional", "ORANGE_TERM", 1.4, 1.2)],
            [("x=2 \\Rightarrow y=2k", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "double x", None, 1.2, 1.0),
             ("x=4 \\Rightarrow y=4k", "ORANGE_TERM", 0.9, (0, 0.0, 0.0), "double again", None, 1.2, 1.0),
             ("ratio y/x = k \\text{ (constant)}", "GREEN_OK", 0.95, (0, -1.2, 0.0), "the test", None, 1.4, 1.4)],
            [("5 kg of flour costs \\$12", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "real-world", None, 1.4, 1.0),
             ("8 kg costs \\dfrac{8}{5}\\cdot 12 = 19.2", "GREEN_OK", 0.9, (0, 0.0, 0.0), "scale up", None, 1.8, 1.6)],
        ],
        "\dfrac{y_{1}}{x_{1}}=\dfrac{y_{2}}{x_{2}}",
        "If y/x stays constant, y and x are directly proportional.",
        99.4,
    ),
    "m10-measurement-scaling/errors": (
        "Absolute and relative error",
        "Error = measured minus true.",
        [
            [("error = \\text{measured} - \\text{true}", "BLUE_TERM", 1.05, (0, 1.4, 0.0), "signed error", "ORANGE_TERM", 1.6, 1.2),
             ("|error| = \\text{absolute error}", "GREEN_OK", 1.05, (0, 0.4, 0.0), "magnitude", None, 1.4, 1.2)],
            [("true = 50 cm", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "exact", None, 1.2, 1.0),
             ("measured = 49 cm", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "off by 1", None, 1.4, 1.0),
             ("absolute error = 1 cm", "GREEN_OK", 1.0, (0, -1.2, 0.0), "|49-50|", None, 1.4, 1.0),
             ("relative error = 1/50 = 0.02 = 2%", "GREEN_OK", 0.95, (0, -2.2, 0.0), "relative", None, 1.8, 1.4)],
            [("true = 5 km,\\; measured = 4.99 km", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "different scale", None, 1.6, 1.0),
             ("abs error = 0.01 km = 10 m", "ORANGE_TERM", 0.9, (0, 0.0, 0.0), "same units", None, 1.6, 1.0),
             ("relative error = 0.01/5 = 0.002 = 0.2%", "GREEN_OK", 0.9, (0, -1.2, 0.0), "small relative", None, 1.6, 1.4)],
        ],
        "\text{relative error}=\dfrac{|\text{meas}-\text{true}|}{\text{true}}",
        "Absolute error is in your units; relative error is a fraction of the true value.",
        92.8,
    ),
    "m10-measurement-trig/bearings": (
        "Bearings",
        "A three-digit angle clockwise from North.",
        [
            [("000° = North", "BLUE_TERM", 1.0, (-3.0, 1.2, 0.0), "zero", "ORANGE_TERM", 1.4, 1.0),
             ("090° = East", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "quarter turn", None, 1.2, 1.0),
             ("180° = South", "BLUE_TERM", 1.0, (3.0, 1.2, 0.0), "half turn", None, 1.2, 1.0),
             ("270° = West", "GREEN_OK", 1.0, (0, 0.0, 0.0), "three-quarter", None, 1.2, 1.0)],
            [("plane bears 120°", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "turn 120° from N", None, 1.4, 1.0),
             ("draw N-S line at start", "ORANGE_TERM", 0.9, (0, 0.0, 0.0), "reference", None, 1.2, 1.0),
             ("draw perpendicular to get right triangle", "GREEN_OK", 0.85, (0, -1.2, 0.0), "N-S/E-W", None, 1.8, 1.4),
             ("opp/adj \\Rightarrow tan or sin/cos", "GREEN_OK", 0.9, (0, -2.2, 0.0), "trig", None, 1.4, 1.4)],
            [("remember 3 digits: 045°, 120°, 270°", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "always", None, 1.4, 1.0),
             ("clockwise from North", "GREEN_OK", 0.9, (0, 0.0, 0.0), "never anticlockwise", None, 1.4, 1.4)],
        ],
        "B = 000°\text{ to }359°,\;\text{clockwise from N}",
        "Bearings are three digits, always clockwise from North.",
        77.0,
    ),
    "m10-measurement-trig/elevation-depression": (
        "Angles of elevation and depression",
        "Above or below the horizontal line of sight.",
        [
            [("horizontal line of sight", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "reference", "ORANGE_TERM", 1.4, 1.2)],
            [("elevation = above horizontal", "BLUE_TERM", 1.0, (-3.0, 1.2, 0.0), "look up", None, 1.4, 1.0),
             ("depression = below horizontal", "ORANGE_TERM", 1.0, (3.0, 1.2, 0.0), "look down", None, 1.4, 1.0)],
            [("eye height = 1.7 m, \\; angle = 30°", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "setup", None, 1.4, 1.0),
             ("tan(30°) = h / 30", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "right triangle", None, 1.4, 1.0),
             ("h = 30\\tan(30°) \\approx 17.3 m", "GREEN_OK", 1.0, (0, -1.2, 0.0), "evaluate", None, 1.6, 1.4),
             ("total = 1.7 + 17.3 = 19 m", "GREEN_OK", 1.0, (0, -2.2, 0.0), "include eye height", None, 1.6, 1.4)],
        ],
        "\tan(\text{angle}) = \dfrac{\text{opp}}{\text{adj}}",
        "Elevation: angle above horizontal. Depression: angle below horizontal.",
        79.4,
    ),
    "m10-measurement-trig/pythagoras-trig": (
        "Pythagoras and trigonometry",
        "Right triangle → opposite, adjacent, hypotenuse.",
        [
            [("a^{2}+b^{2}=c^{2}", "BLUE_TERM", 1.1, (0, 1.4, 0.0), "Pythagoras", "ORANGE_TERM", 1.4, 1.2),
             ("\\sin\\theta=\\tfrac{o}{c},\\;\\cos\\theta=\\tfrac{a}{c},\\;\\tan\\theta=\\tfrac{o}{a}", "GREEN_OK", 0.95, (0, 0.2, 0.0), "trig ratios", None, 2.0, 1.4)],
            [("opp=3,\\; adj=4", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "given", None, 1.2, 1.0),
             ("hyp = \\sqrt{9+16} = 5", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "Pythagoras", None, 1.4, 1.0),
             ("\\tan\\theta = \\tfrac{3}{4}", "GREEN_OK", 1.0, (0, -1.0, 0.0), "opposite over adjacent", None, 1.4, 1.0),
             ("\\sin\\theta = \\tfrac{3}{5},\\;\\cos\\theta = \\tfrac{4}{5}", "GREEN_OK", 0.95, (0, -2.0, 0.0), "opp/hyp, adj/hyp", None, 1.6, 1.4)],
            [("picking the right ratio saves time", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "strategy", None, 1.4, 1.0),
             ("know OAH \\Rightarrow pick sin/cos/tan", "GREEN_OK", 0.9, (0, -0.2, 0.0), "match the question", None, 1.6, 1.4)],
        ],
        "\sin=\tfrac{O}{H},\;\cos=\tfrac{A}{H},\;\tan=\tfrac{O}{A}",
        "Pythagoras gives the third side; trig ratios give angles or sides.",
        87.7,
    ),
    "m10-measurement-trig/surveying-design": (
        "Surveying and design",
        "Plan a survey that minimises error and effort.",
        [
            [("design a survey", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "plan first", "ORANGE_TERM", 1.2, 1.0)],
            [("1. identify landmarks", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "step 1", None, 1.2, 1.0),
             ("2. measure baselines", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "step 2", None, 1.2, 1.0),
             ("3. measure angles", "GREEN_OK", 0.95, (0, -1.0, 0.0), "step 3", None, 1.2, 1.0),
             ("4. triangulate", "GREEN_OK", 1.0, (0, -2.0, 0.0), "step 4", None, 1.2, 1.4)],
            [("triangulation gives distance via angles", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "core idea", None, 1.4, 1.0),
             ("baseline + two angles = full triangle", "GREEN_OK", 0.9, (0, 0.0, 0.0), "law of sines", None, 1.6, 1.6)],
        ],
        "\text{two angles + one side = triangle}",
        "Surveying: pick landmarks, measure baseline and angles, then triangulate.",
        78.6,
    ),
    "m10-number-approximations/rounding-truncation": (
        "Rounding vs truncation",
        "Round to nearest; truncate chops the digits off.",
        [
            [("3.14159…", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "full value", "ORANGE_TERM", 1.2, 1.0),
             ("to 2 d.p.: round \\Rightarrow 3.14", "GREEN_OK", 1.0, (0, 0.4, 0.0), "look at next digit", None, 1.4, 1.0),
             ("to 2 d.p.: truncate \\Rightarrow 3.14", "ORANGE_TERM", 1.0, (0, -0.4, 0.0), "chop", None, 1.4, 1.0)],
            [("next digit \\geq 5 \\Rightarrow round up", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "round rule", None, 1.4, 1.0),
             ("next digit < 5 \\Rightarrow round down", "BLUE_TERM", 1.0, (0, 0.0, 0.0), "round rule", None, 1.4, 1.0),
             ("2.456 \\to 2.46 (round), \\to 2.45 (truncate)", "GREEN_OK", 0.95, (0, -1.2, 0.0), "example", None, 1.6, 1.4)],
            [("truncate always rounds toward zero", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "warning", None, 1.4, 1.0),
             ("truncation introduces systematic error", "GREEN_OK", 0.9, (0, 0.0, 0.0), "use round in practice", None, 1.6, 1.4)],
        ],
        "\text{round: nearest; truncate: cut}",
        "Rounding looks at the next digit; truncation just chops.",
        83.9,
    ),
    "m10-number-approximations/compound-errors": (
        "Compound errors",
        "Errors stack when measurements multiply.",
        [
            [("error = \\dfrac{|\\text{approx}-\\text{true}|}{|\\text{true}|}", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "relative error", "ORANGE_TERM", 1.6, 1.2)],
            [("length measured off by 1%, width off by 1%", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "two errors", None, 1.6, 1.0),
             ("area error \\approx 1% + 1% = 2%", "ORANGE_TERM", 0.9, (0, 0.0, 0.0), "area", None, 1.6, 1.0),
             ("volume error \\approx 3 \\times 1% = 3%", "GREEN_OK", 0.9, (0, -1.0, 0.0), "volume", None, 1.6, 1.0),
             ("area error \\neq 1% \\times 1%", "GREEN_OK", 0.9, (0, -2.0, 0.0), "common mistake", None, 1.6, 1.4)],
            [("more measurements \\Rightarrow more error", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "compounding", None, 1.4, 1.0),
             ("minimise the chain of measurements", "GREEN_OK", 0.9, (0, 0.0, 0.0), "strategy", None, 1.4, 1.4)],
        ],
        "\text{length errors add for area (2D) and volume (3D)}",
        "Errors add when a derived quantity combines measurements.",
        91.8,
    ),
}


def main():
    pairs = []
    for key, (title, subtitle, beats, takeaway_eq, takeaway_sub, audio_seconds) in SCENES.items():
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

    write("_render_all_year10_part2.sh", pairs)
    for shard in range(4):
        rows = [(t, l, c) for i, (t, l, c) in enumerate(pairs) if i % 4 == shard]
        write(f"_render_year10_part2_{shard}.sh", rows)
    print(f"wrote {len(pairs)} part2 pairs")


if __name__ == "__main__":
    main()