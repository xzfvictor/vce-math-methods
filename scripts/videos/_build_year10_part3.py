#!/usr/bin/env python3
"""Build Year 10 scenes part 3 — space, statistics, probability."""
from __future__ import annotations
from pathlib import Path

ROOT = Path("/home/victor/maths-decoded")
OUT = ROOT / "scripts/videos"


SCENES: dict[str, tuple] = {
    "m10-space-proofs/proof-vs-demo": (
        "Proof versus demonstration",
        "A proof holds for everyone; a demonstration only checks cases.",
        [
            [("proof: a chain of reasoning", "BLUE_TERM", 1.0, (-3.0, 1.2, 0.0), "general", "ORANGE_TERM", 1.6, 1.0),
             ("demonstration: a check that works for one case", "GREEN_OK", 1.0, (3.0, 1.2, 0.0), "specific", None, 1.8, 1.2)],
            [("\"every angle sum is 180°\"", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "claim", None, 1.4, 1.0),
             ("draw one triangle and measure", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "demonstration", None, 1.4, 1.0),
             ("checks one example only", "GREEN_OK", 1.0, (0, -1.0, 0.0), "not a proof", None, 1.4, 1.4)],
            [("formal proof: angle sum = (n-2)·180°", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "general formula", None, 1.8, 1.2),
             ("split into triangles, sum angles", "GREEN_OK", 0.95, (0, 0.0, 0.0), "construction", None, 1.6, 1.4)],
        ],
        "\text{proof} = \text{reasoning for all cases}",
        "Demonstrations verify one example; proofs justify every example.",
        85.4,
    ),
    "m10-space-proofs/congruent-triangles": (
        "Congruent triangles",
        "SSS, SAS, AAS, RHS give matching sides and angles.",
        [
            [("triangle ≅ triangle", "BLUE_TERM", 1.1, (0, 1.4, 0.0), "congruent", "ORANGE_TERM", 1.4, 1.2)],
            [("SSS: 3 sides match", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "side-side-side", None, 1.2, 1.0),
             ("SAS: 2 sides + included angle", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "side-angle-side", None, 1.4, 1.0),
             ("AAS: 2 angles + 1 side", "GREEN_OK", 0.95, (0, -1.0, 0.0), "angle-angle-side", None, 1.2, 1.0),
             ("RHS: right angle, hypotenuse, side", "GREEN_OK", 0.95, (0, -2.0, 0.0), "right triangle", None, 1.6, 1.4)],
            [("CPCTC: corresponding parts equal", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "conclusion", None, 1.4, 1.0),
             ("all corresponding angles equal", "GREEN_OK", 0.95, (0, 0.0, 0.0), "then sides too", None, 1.6, 1.4)],
        ],
        "\text{SSS, SAS, AAS, RHS}\Rightarrow\triangle\cong\triangle",
        "Match the right combination of sides and angles, then every part matches.",
        100.2,
    ),
    "m10-space-proofs/dynamic-geometry": (
        "Dynamic geometry software",
        "Sketch, drag, measure — geometry you can see move.",
        [
            [("GeoGebra / Cabri", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "common tools", "ORANGE_TERM", 1.4, 1.2)],
            [("1. sketch the construction", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "step 1", None, 1.2, 1.0),
             ("2. measure key lengths", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "step 2", None, 1.2, 1.0),
             ("3. drag a vertex and watch", "GREEN_OK", 0.95, (0, -1.0, 0.0), "step 3", None, 1.4, 1.4),
             ("4. conjecture: what stays the same?", "GREEN_OK", 0.95, (0, -2.0, 0.0), "step 4", None, 1.4, 1.4)],
            [("useful for exploring conjectures", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "role", None, 1.4, 1.0),
             ("not a substitute for proof", "GREEN_OK", 0.9, (0, 0.0, 0.0), "limitation", None, 1.4, 1.4)],
        ],
        "\text{measure, drag, conjecture, then prove}",
        "Drag the figure — measure what's invariant, then write the proof.",
        86.2,
    ),
    "m10-space-proofs/isosceles-properties": (
        "Isosceles triangle properties",
        "Equal sides give equal base angles.",
        [
            [("AB = AC", "BLUE_TERM", 1.1, (0, 1.4, 0.0), "two equal sides", "ORANGE_TERM", 1.4, 1.2),
             ("∠B = ∠C", "GREEN_OK", 1.1, (0, 0.2, 0.0), "base angles", None, 1.4, 1.4)],
            [("draw the angle bisector AD", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "proof idea", None, 1.4, 1.0),
             ("△ABD ≅ △ACD (SAS)", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "shared angle + AD", None, 1.6, 1.0),
             ("→ ∠B = ∠C", "GREEN_OK", 1.0, (0, -1.2, 0.0), "congruent angles", None, 1.4, 1.4)],
            [("converse also true", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "equiangular \\Rightarrow isosceles", None, 1.4, 1.0),
             ("equal base angles \\Rightarrow equal sides", "GREEN_OK", 0.9, (0, 0.0, 0.0), "converse", None, 1.6, 1.4)],
        ],
        "\triangle ABC\text{ isosceles}\Longleftrightarrow\angle B=\angle C",
        "Equal sides come with equal base angles; equal base angles come with equal sides.",
        85.1,
    ),
    "m10-space-networks/network-basics": (
        "Network basics",
        "Vertices joined by edges.",
        [
            [("vertex (node)", "BLUE_TERM", 1.0, (-3.0, 1.2, 0.0), "a point", "ORANGE_TERM", 1.2, 1.0),
             ("edge (link)", "GREEN_OK", 1.0, (3.0, 1.2, 0.0), "a connection", None, 1.2, 1.0)],
            [("degree = # edges meeting at a vertex", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "degree", None, 1.4, 1.0),
             ("vertex A degree = 3", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "example", None, 1.2, 1.0),
             ("vertex B degree = 2", "GREEN_OK", 1.0, (0, -1.0, 0.0), "example", None, 1.2, 1.0)],
            [("handshake lemma: sum of degrees = 2·(# edges)", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "key fact", None, 1.6, 1.0),
             ("each edge contributes 2 to the sum", "GREEN_OK", 0.9, (0, 0.0, 0.0), "why", None, 1.6, 1.4)],
        ],
        "\sum \text{degrees}=2|\text{edges}|",
        "Vertices joined by edges; the handshake lemma links degrees and edges.",
        86.0,
    ),
    "m10-space-networks/euler-polyhedra": (
        "Euler's formula for polyhedra",
        "V - E + F = 2 for every convex polyhedron.",
        [
            [("cube: V=8, E=12, F=6", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "count", "ORANGE_TERM", 1.4, 1.0),
             ("8-12+6 = 2", "GREEN_OK", 1.0, (0, 0.2, 0.0), "Euler", None, 1.4, 1.4)],
            [("tetrahedron: V=4, E=6, F=4", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "count", None, 1.4, 1.0),
             ("4-6+4 = 2", "GREEN_OK", 1.0, (0, 0.0, 0.0), "Euler", None, 1.4, 1.4),
             ("icosahedron: V=12, E=30, F=20", "BLUE_TERM", 0.95, (0, -1.0, 0.0), "count", None, 1.4, 1.0),
             ("12-30+20 = 2", "GREEN_OK", 1.0, (0, -2.0, 0.0), "Euler", None, 1.4, 1.4)],
            [("Euler's formula: V - E + F = 2", "BLUE_TERM", 1.1, (0, 1.2, 0.0), "general", None, 1.6, 1.2),
             ("works for every convex polyhedron", "GREEN_OK", 0.9, (0, -0.2, 0.0), "caveat", None, 1.4, 1.4)],
        ],
        "V - E + F = 2",
        "Count vertices, edges, faces on any convex polyhedron — they always sum to 2.",
        93.6,
    ),
    "m10-statistics-boxplots/five-number-summary": (
        "Five-number summary",
        "Min, Q1, median, Q3, max.",
        [
            [("min, Q1, median, Q3, max", "BLUE_TERM", 0.95, (0, 1.4, 0.0), "five numbers", "ORANGE_TERM", 1.6, 1.2)],
            [("data: 2, 4, 5, 7, 9, 12, 15", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "example", None, 1.4, 1.0),
             ("min=2,\\; max=15", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "extremes", None, 1.4, 1.0),
             ("median=7", "GREEN_OK", 1.0, (0, -1.0, 0.0), "middle", None, 1.2, 1.0),
             ("Q1=4,\\; Q3=12", "GREEN_OK", 1.0, (0, -2.0, 0.0), "quartiles", None, 1.4, 1.4)],
            [("IQR = Q3 - Q1 = 8", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "interquartile range", None, 1.4, 1.0),
             ("spread of the middle 50%", "GREEN_OK", 0.9, (0, 0.0, 0.0), "what it measures", None, 1.4, 1.4)],
        ],
        "\text{IQR}=Q_{3}-Q_{1}",
        "Five-number summary: min, Q1, median, Q3, max — the IQR measures the middle 50%.",
        99.5,
    ),
    "m10-statistics-boxplots/boxplots": (
        "Boxplots",
        "A picture of the five-number summary.",
        [
            [("box = Q1 to Q3", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "middle 50%", "ORANGE_TERM", 1.4, 1.0),
             ("line inside = median", "ORANGE_TERM", 1.0, (0, 0.4, 0.0), "Q2", None, 1.4, 1.0),
             ("whiskers = min and max", "GREEN_OK", 1.0, (0, -0.6, 0.0), "outliers excluded", None, 1.4, 1.4)],
            [("data 2,4,5,7,9,12,15", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "example", None, 1.2, 1.0),
             ("left whisker to 2", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "min", None, 1.2, 1.0),
             ("box from 4 to 12", "GREEN_OK", 1.0, (0, -1.0, 0.0), "Q1-Q3", None, 1.2, 1.0),
             ("right whisker to 15", "GREEN_OK", 1.0, (0, -2.0, 0.0), "max", None, 1.2, 1.4)],
            [("outliers plotted separately", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "1.5 IQR rule", None, 1.4, 1.0),
             ("skew: long whisker \\Rightarrow skewed", "GREEN_OK", 0.9, (0, 0.0, 0.0), "shape", None, 1.6, 1.4)],
        ],
        "\text{box=Q1--Q3,\; line=median,\; whiskers=min,max}",
        "A boxplot shows the five-number summary as a box and whiskers.",
        92.2,
    ),
    "m10-statistics-boxplots/comparing-displays": (
        "Comparing boxplots",
        "Side-by-side boxes tell you which group is bigger or more spread out.",
        [
            [("two datasets, two boxplots", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "compare", "ORANGE_TERM", 1.4, 1.0)],
            [("Class A: median=65, IQR=10", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "Class A", None, 1.4, 1.0),
             ("Class B: median=72, IQR=12", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "Class B", None, 1.4, 1.0),
             ("B > A on the median", "GREEN_OK", 1.0, (0, -1.0, 0.0), "centre", None, 1.4, 1.4),
             ("B more spread out", "GREEN_OK", 1.0, (0, -2.0, 0.0), "spread", None, 1.4, 1.4)],
            [("compare centre, spread, shape", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "three checks", None, 1.4, 1.0),
             ("outliers: only in A", "GREEN_OK", 0.9, (0, 0.0, 0.0), "shape", None, 1.4, 1.4)],
        ],
        "\text{centre, spread, shape, outliers}",
        "Compare boxplots on centre, spread, shape and any outliers.",
        83.8,
    ),
    "m10-statistics-boxplots/digital-tools": (
        "Digital tools for boxplots",
        "Spreadsheets and calculators draw them in seconds.",
        [
            [("spreadsheet / calculator", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "tools", "ORANGE_TERM", 1.4, 1.0)],
            [("1. enter the data", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "step 1", None, 1.2, 1.0),
             ("2. ask for quartiles", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "step 2", None, 1.4, 1.0),
             ("3. insert chart", "GREEN_OK", 0.95, (0, -1.0, 0.0), "step 3", None, 1.2, 1.0),
             ("4. choose box plot", "GREEN_OK", 0.95, (0, -2.0, 0.0), "step 4", None, 1.4, 1.4)],
            [("always check the units on the axis", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "caveat", None, 1.4, 1.0),
             ("tools can mis-label outliers", "GREEN_OK", 0.9, (0, 0.0, 0.0), "sanity check", None, 1.4, 1.4)],
        ],
        "\text{enter data \to quartiles \to box plot}",
        "Use a spreadsheet or calculator to find the quartiles, then insert the box plot.",
        78.4,
    ),
    "m10-statistics-claims/axes-samples": (
        "Axes, units and samples",
        "Always label both axes and state the sample size.",
        [
            [("x-axis: independent variable", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "what you change", "ORANGE_TERM", 1.6, 1.2),
             ("y-axis: dependent variable", "GREEN_OK", 1.0, (0, 0.4, 0.0), "what you measure", None, 1.4, 1.2)],
            [("scale: starts at zero?", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "check 1", None, 1.4, 1.0),
             ("units labelled?", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "check 2", None, 1.2, 1.0),
             ("n = ?", "GREEN_OK", 1.0, (0, -1.0, 0.0), "check 3", None, 1.2, 1.4)],
            [("small n \\Rightarrow read with care", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "small sample", None, 1.4, 1.0),
             ("big n \\Rightarrow more reliable", "GREEN_OK", 0.9, (0, 0.0, 0.0), "big sample", None, 1.4, 1.4)],
        ],
        "\text{label axes, units, sample size}",
        "Label every axis, the units, and the sample size n.",
        76.2,
    ),
    "m10-statistics-claims/causation-ethics": (
        "Causation, ethics and claims",
        "Correlation is not causation — and the data has to be ethical.",
        [
            [("correlation \\neq causation", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "key warning", "ORANGE_TERM", 1.6, 1.4)],
            [("ice-cream sales correlate with drownings", "BLUE_TERM", 0.85, (0, 1.2, 0.0), "spurious", None, 1.6, 1.0),
             ("confounder: hot weather", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "hidden variable", None, 1.4, 1.0),
             ("neither causes the other", "GREEN_OK", 1.0, (0, -1.0, 0.0), "spurious correlation", None, 1.4, 1.4)],
            [("ethical data: informed consent", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "principle 1", None, 1.4, 1.0),
             ("anonymise respondents", "ORANGE_TERM", 0.9, (0, 0.0, 0.0), "principle 2", None, 1.2, 1.0),
             ("report sources honestly", "GREEN_OK", 0.9, (0, -1.0, 0.0), "principle 3", None, 1.4, 1.4)],
        ],
        "\text{correlation}\neq\text{causation}",
        "Always check for confounders and respect the people behind the data.",
        83.4,
    ),
    "m10-statistics-investigations/cycle": (
        "Statistical investigation cycle",
        "Plan, collect, process, analyse, communicate.",
        [
            [("1. plan the question", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "step 1", "ORANGE_TERM", 1.4, 1.0),
             ("2. collect data", "ORANGE_TERM", 1.0, (0, 0.4, 0.0), "step 2", None, 1.2, 1.0),
             ("3. process & analyse", "GREEN_OK", 1.0, (0, -0.6, 0.0), "step 3", None, 1.4, 1.0),
             ("4. communicate results", "GREEN_OK", 1.0, (0, -1.6, 0.0), "step 4", None, 1.4, 1.4)],
            [("plan \\to collect \\to analyse \\to communicate", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "order matters", None, 1.6, 1.0),
             ("loops back to plan if results surprise", "GREEN_OK", 0.9, (0, 0.0, 0.0), "iterative", None, 1.6, 1.4)],
        ],
        "\text{plan}\to\text{collect}\to\text{analyse}\to\text{communicate}",
        "Investigations cycle: plan, collect, process, analyse, communicate.",
        86.4,
    ),
    "m10-statistics-investigations/time-series": (
        "Time series data",
        "Measure the same thing over time to see a trend.",
        [
            [("time on x-axis", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "always", "ORANGE_TERM", 1.4, 1.0),
             ("value on y-axis", "GREEN_OK", 1.0, (0, 0.4, 0.0), "measurement", None, 1.2, 1.4)],
            [("trend: long-term direction", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "trend", None, 1.4, 1.0),
             ("seasonal: repeats each year", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "season", None, 1.4, 1.0),
             ("residual: noise", "GREEN_OK", 0.95, (0, -1.0, 0.0), "residual", None, 1.2, 1.4)],
            [("watch for seasonal spikes", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "be careful", None, 1.4, 1.0),
             ("smooth before forecasting", "GREEN_OK", 0.9, (0, 0.0, 0.0), "strategy", None, 1.4, 1.4)],
        ],
        "\text{time on x, value on y}",
        "Plot time on the x-axis; look for trend, season, and noise.",
        84.4,
    ),
    "m10-statistics-scatter/scatter-fit": (
        "Scatter and line of best fit",
        "Eye-ball a line through the cloud of points.",
        [
            [("(x, y) pairs", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "scatter", "ORANGE_TERM", 1.2, 1.0),
             ("draw a line close to most points", "GREEN_OK", 1.0, (0, 0.4, 0.0), "fit", None, 1.4, 1.4)],
            [("balance points above and below", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "balance", None, 1.4, 1.0),
             ("follow the trend, not the outliers", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "ignore outliers", None, 1.4, 1.0),
             ("line goes through (\\bar{x},\\bar{y})", "GREEN_OK", 0.95, (0, -1.0, 0.0), "mean point", None, 1.6, 1.4)],
            [("slope = \\dfrac{\\text{rise}}{\\text{run}}", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "use the line", None, 1.4, 1.0),
             ("y = mx + b", "GREEN_OK", 1.0, (0, 0.0, 0.0), "equation", None, 1.4, 1.4)],
        ],
        "\text{line of best fit: balance above and below}",
        "Draw the line that balances the points above and below; it passes through the mean point.",
        76.3,
    ),
    "m10-statistics-scatter/interpolation-causation": (
        "Interpolation vs causation",
        "Between points is interpolation; outside is extrapolation. Correlation is not cause.",
        [
            [("between data points \\to interpolate", "BLUE_TERM", 0.9, (0, 1.4, 0.0), "safe", "ORANGE_TERM", 1.4, 1.0),
             ("outside data \\to extrapolate", "ORANGE_TERM", 0.9, (0, 0.4, 0.0), "risky", None, 1.4, 1.4)],
            [("temperature vs ice-cream sales", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "positive correlation", None, 1.4, 1.0),
             ("temp 25°C \\Rightarrow sales approx 200", "GREEN_OK", 0.85, (0, 0.0, 0.0), "interpolate", None, 1.4, 1.4),
             ("temperature does NOT cause the sale", "ORANGE_TERM", 0.85, (0, -1.0, 0.0), "no causation", None, 1.4, 1.4)],
            [("interpolation is safe; extrapolation is not", "BLUE_TERM", 0.85, (0, 1.2, 0.0), "guideline", None, 1.4, 1.0),
             ("correlation \\neq causation", "GREEN_OK", 0.85, (0, 0.0, 0.0), "always", None, 1.4, 1.4)],
        ],
        "\text{interpolate in range,\; extrapolate with caution}",
        "Use the line between points; outside that range is guessing, not data.",
        84.5,
    ),
    "m10-statistics-two-way/build-read": (
        "Build and read two-way tables",
        "Two variables, one grid of counts.",
        [
            [("rows: category 1", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "first variable", "ORANGE_TERM", 1.2, 1.0),
             ("columns: category 2", "GREEN_OK", 1.0, (0, 0.4, 0.0), "second variable", None, 1.2, 1.4)],
            [("total row + total column", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "margins", None, 1.4, 1.0),
             ("read joint frequency from a cell", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "inside", None, 1.4, 1.0),
             ("read marginal from a total", "GREEN_OK", 0.95, (0, -1.0, 0.0), "edges", None, 1.4, 1.4)],
            [("check row totals match column totals", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "sanity check", None, 1.4, 1.4)],
        ],
        "\text{rows}\times\text{columns}=\text{two-way table}",
        "Rows are one category, columns the other; totals lie on the edges.",
        80.5,
    ),
    "m10-statistics-two-way/percentages-association": (
        "Percentages and association",
        "Compare column percentages to see which group has the higher rate.",
        [
            [("compare percentages, not counts", "BLUE_TERM", 0.95, (0, 1.4, 0.0), "fair comparison", "ORANGE_TERM", 1.4, 1.4)],
            [("Group A: 30/100 = 30% pass", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "A", None, 1.4, 1.0),
             ("Group B: 20/50 = 40% pass", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "B", None, 1.4, 1.4),
             ("B has the higher rate", "GREEN_OK", 1.0, (0, -1.2, 0.0), "even though n differs", None, 1.4, 1.4)],
            [("column percentages = within-column comparisons", "BLUE_TERM", 0.85, (0, 1.2, 0.0), "rule", None, 1.6, 1.0),
             ("row percentages = within-row comparisons", "GREEN_OK", 0.85, (0, 0.0, 0.0), "rule", None, 1.6, 1.4)],
        ],
        "\text{column % = within-column rate}",
        "Use percentages (not counts) when the group sizes differ.",
        73.7,
    ),
    "m10-probability-conditional/conditional-language": (
        "Conditional probability language",
        "P(A|B) means A given B.",
        [
            [("P(A|B) = probability of A given B", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "definition", "ORANGE_TERM", 1.6, 1.4)],
            [("B has happened, so restrict to B", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "given B", None, 1.4, 1.0),
             ("then ask P(A inside B)", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "restricted sample", None, 1.4, 1.4),
             ("P(A|B) \\neq P(B|A)", "GREEN_OK", 1.0, (0, -1.2, 0.0), "do not swap", None, 1.4, 1.4)],
            [("language: given that", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "wording", None, 1.4, 1.0),
             ("if I know B, what is the chance of A?", "GREEN_OK", 0.85, (0, 0.0, 0.0), "think", None, 1.6, 1.4)],
        ],
        "P(A|B)=\dfrac{P(A\cap B)}{P(B)}",
        "Read P(A|B) as probability of A given that B has happened.",
        81.9,
    ),
    "m10-probability-conditional/real-world": (
        "Real-world conditional probability",
        "Filter the sample space, then count.",
        [
            [("disease: 1% have it", "BLUE_TERM", 0.95, (0, 1.4, 0.0), "prevalence", "ORANGE_TERM", 1.4, 1.0),
             ("test: 95% sensitivity", "BLUE_TERM", 0.95, (0, 0.4, 0.0), "test stats", None, 1.4, 1.0),
             ("P(positive | disease) = 0.95", "GREEN_OK", 0.9, (0, -0.6, 0.0), "sensitivity", None, 1.6, 1.4)],
            [("P(disease | positive) \\neq 0.95", "ORANGE_TERM", 0.95, (0, 1.2, 0.0), "the trick", None, 1.6, 1.0),
             ("most positives are false positives", "GREEN_OK", 0.95, (0, 0.0, 0.0), "rare disease", None, 1.6, 1.0),
             ("use Bayes' theorem", "GREEN_OK", 1.0, (0, -1.0, 0.0), "the tool", None, 1.4, 1.4)],
        ],
        "P(A|B)=\dfrac{P(B|A)P(A)}{P(B)}",
        "P(A|B) is not the same as P(B|A). Use Bayes when you flip the order.",
        94.5,
    ),
    "m10-probability-conditional/simulation": (
        "Simulate conditional probability",
        "Run trials when the formula is too hard.",
        [
            [("simulate \\to estimate", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "method", "ORANGE_TERM", 1.4, 1.0)],
            [("1. draw N random cases", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "step 1", None, 1.4, 1.0),
             ("2. count B's, then A inside B", "ORANGE_TERM", 0.95, (0, 0.0, 0.0), "step 2", None, 1.4, 1.0),
             ("3. ratio = P(A|B)", "GREEN_OK", 0.95, (0, -1.0, 0.0), "step 3", None, 1.4, 1.4)],
            [("more trials \\Rightarrow better estimate", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "law of large numbers", None, 1.6, 1.0),
             ("watch for bias in your model", "GREEN_OK", 0.9, (0, 0.0, 0.0), "caveat", None, 1.4, 1.4)],
        ],
        "\text{simulate: trials}\to\text{ratio}",
        "Run many trials; the ratio converges to the conditional probability.",
        82.6,
    ),
    "m10-probability-conditional/trees-without-replacement": (
        "Probability trees without replacement",
        "Each branch shrinks the pool.",
        [
            [("draw two balls without putting back", "BLUE_TERM", 0.9, (0, 1.4, 0.0), "without replacement", "ORANGE_TERM", 1.4, 1.0)],
            [("P(red 1st) = \\dfrac{5}{12}", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "branch 1", None, 1.4, 1.0),
             ("P(blue 2nd | red 1st) = \\dfrac{7}{11}", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "branch 2", None, 1.4, 1.0),
             ("P(red, then blue) = \\dfrac{5}{12}\\cdot \\dfrac{7}{11}=\\dfrac{35}{132}", "GREEN_OK", 1.0, (0, -1.2, 0.0), "multiply", None, 1.8, 1.4)],
            [("without replacement: counts shrink", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "rule", None, 1.4, 1.0),
             ("with replacement: counts stay the same", "GREEN_OK", 0.9, (0, 0.0, 0.0), "contrast", None, 1.4, 1.4)],
        ],
        "P(A\text{ then }B)=P(A)\cdot P(B|A)",
        "Each branch reduces the count: multiply along, add across.",
        91.4,
    ),
    "m10-probability-conditional/two-way-venn": (
        "Two-way tables and Venn diagrams",
        "Overlap shows the joint probability.",
        [
            [("A and B", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "overlap", "ORANGE_TERM", 1.2, 1.0),
             ("A only + A and B = P(A)", "GREEN_OK", 1.0, (0, 0.4, 0.0), "partition", None, 1.4, 1.4)],
            [("P(A) = 0.6, \\; P(B) = 0.5", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "values", None, 1.4, 1.0),
             ("P(A\\cap B) = 0.3", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "overlap", None, 1.2, 1.0),
             ("P(A\\cup B) = 0.6 + 0.5 - 0.3 = 0.8", "GREEN_OK", 1.0, (0, -1.2, 0.0), "inclusion-exclusion", None, 1.8, 1.4)],
            [("P(A|B) = \\dfrac{P(A\\cap B)}{P(B)}", "BLUE_TERM", 0.95, (0, 1.2, 0.0), "from the picture", None, 1.4, 1.0),
             ("= \\dfrac{0.3}{0.5} = 0.6", "GREEN_OK", 1.0, (0, 0.0, 0.0), "evaluate", None, 1.4, 1.4)],
        ],
        "P(A\cup B)=P(A)+P(B)-P(A\cap B)",
        "Draw a Venn: total = union, joint is the overlap.",
        96.7,
    ),
    "m10-probability-experiments/tree-diagrams": (
        "Tree diagrams with replacement",
        "Branches multiply, columns sum.",
        [
            [("P(heads) = \\tfrac{1}{2}, P(tails) = \\tfrac{1}{2}", "BLUE_TERM", 0.95, (0, 1.4, 0.0), "one flip", "ORANGE_TERM", 1.4, 1.0)],
            [("P(HH) = \\tfrac{1}{2}\\cdot\\tfrac{1}{2}=\\tfrac{1}{4}", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "two flips", None, 1.4, 1.0),
             ("P(HT) = \\tfrac{1}{4}", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "branch", None, 1.2, 1.0),
             ("P(TH) = \\tfrac{1}{4}", "GREEN_OK", 1.0, (0, -1.0, 0.0), "branch", None, 1.2, 1.0),
             ("P(TT) = \\tfrac{1}{4}", "GREEN_OK", 1.0, (0, -2.0, 0.0), "branch", None, 1.2, 1.4),
             ("total = 1", "GREEN_OK", 1.0, (0, -3.0, 0.0), "check", None, 1.2, 1.4)],
            [("3 flips: 2^{3} = 8 leaves", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "extension", None, 1.4, 1.0),
             ("each leaf = \\tfrac{1}{8}", "GREEN_OK", 0.9, (0, 0.0, 0.0), "fair", None, 1.4, 1.4)],
        ],
        "\text{multiply along branches, sum down columns}",
        "Multiply along the branches, sum down the columns.",
        75.9,
    ),
    "m10-probability-experiments/replacement-independence": (
        "Replacement and independence",
        "With replacement, trials are independent.",
        [
            [("with replacement: independent", "BLUE_TERM", 1.0, (0, 1.4, 0.0), "key idea", "ORANGE_TERM", 1.4, 1.0),
             ("P(A\\cap B) = P(A)\\cdot P(B)", "GREEN_OK", 1.0, (0, 0.4, 0.0), "independence", None, 1.4, 1.4)],
            [("P(red 1st) = \\tfrac{5}{12}", "BLUE_TERM", 1.0, (0, 1.2, 0.0), "branch 1", None, 1.4, 1.0),
             ("put back: P(red 2nd) = \\tfrac{5}{12}", "ORANGE_TERM", 1.0, (0, 0.0, 0.0), "with replacement", None, 1.4, 1.0),
             ("P(both red) = \\tfrac{5}{12}\\cdot\\tfrac{5}{12}", "GREEN_OK", 1.0, (0, -1.0, 0.0), "multiply", None, 1.4, 1.4)],
            [("sampling with replacement approximates large population", "BLUE_TERM", 0.9, (0, 1.2, 0.0), "use case", None, 1.4, 1.0),
             ("small population \\Rightarrow without replacement", "GREEN_OK", 0.9, (0, 0.0, 0.0), "contrast", None, 1.4, 1.4)],
        ],
        "P(A\cap B)=P(A)P(B)\text{ when independent}",
        "With replacement, trials are independent; multiply the probabilities.",
        87.0,
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

    write("_render_all_year10_part3.sh", pairs)
    for shard in range(4):
        rows = [(t, l, c) for i, (t, l, c) in enumerate(pairs) if i % 4 == shard]
        write(f"_render_year10_part3_{shard}.sh", rows)
    print(f"wrote {len(pairs)} part3 pairs")


if __name__ == "__main__":
    main()