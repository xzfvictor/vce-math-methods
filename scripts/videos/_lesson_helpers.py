"""Helpers shared by Year 10 lesson scenes.

Each scene is structured as five beats:
    1. Title + subtitle            (animated in)
    2. Concrete worked example     (animated step-by-step)
    3. Generalised formula / rule  (built up from the example)
    4. Contrast / common mistake  (shown in red, then resolved)
    5. Final takeaway             (held until the audio ends)

Use ``build_lesson_scene`` from a topic-specific scene file:

    from _lesson_helpers import build_lesson_scene, SCENE_STYLE

    class MyLessonScene(Scene):
        def construct(self):
            build_lesson_scene(self, title=..., subtitle=...,
                               beats=[Step(text, color=BLUE_TERM,
                                           anchor=UP * 1.4), ...],
                               takeaway_eq=r"a^{m/n} = \\sqrt[n]{a^m}",
                               takeaway_sub="...", audio_seconds=82.5)
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Optional

from manim import (
    Animation,
    FadeIn,
    FadeOut,
    BackgroundRectangle,
    BOLD,
    Circle,
    Create,
    Dot,
    DOWN,
    Indicate,
    LEFT,
    Line,
    MathTex,
    Rectangle,
    RIGHT,
    Scene,
    SurroundingRectangle,
    Text,
    UP,
    VGroup,
    Write,
    BLACK,
    BLUE_C,
    GREEN_C,
    ORANGE,
    PURPLE_C,
    RED_C,
    WHITE,
    YELLOW,
)


# Color name → actual color (resolved at import time so generators can
# store string names and resolve them into real ManimColor values).
COLOR_NAMES = {
    "BLUE_TERM": BLUE_C,
    "ORANGE_TERM": ORANGE,
    "GREEN_OK": GREEN_C,
    "RED_REJECT": RED_C,
    "PURPLE_ACCENT": PURPLE_C,
    "TEAL_TERM": BLUE_C,
    "YELLOW_HIGHLIGHT": YELLOW,
}


def resolve_color(value):
    """Map a string like 'BLUE_TERM' to a ManimColor. Pass-through anything else."""
    if isinstance(value, str) and value in COLOR_NAMES:
        return COLOR_NAMES[value]
    return value


from _common import (
    BAND_TITLE,
    BAND_CHART_CENTER,
    BLUE_TERM,
    TEAL_TERM,
    ORANGE_TERM,
    RED_REJECT,
    GREEN_OK,
    PURPLE_ACCENT,
    YELLOW_HIGHLIGHT,
    beat_group,
    animate_intro,
    animate_final_definition,
    make_equation_card,
    make_term_card,
)


SCENE_STYLE = {
    "BLUE_TERM": BLUE_TERM,
    "ORANGE_TERM": ORANGE_TERM,
    "GREEN_OK": GREEN_OK,
    "RED_REJECT": RED_REJECT,
    "PURPLE_ACCENT": PURPLE_ACCENT,
    "TEAL_TERM": TEAL_TERM,
    "YELLOW_HIGHLIGHT": YELLOW_HIGHLIGHT,
}


@dataclass
class Step:
    """A single term/equation that appears in a beat."""

    text: str
    color: object = BLUE_TERM
    scale: float = 1.0
    anchor: Optional[tuple[float, float, float]] = None
    sub: Optional[str] = None          # optional sub-label rendered beneath the term
    sub_color: object = None
    pre_wait: float = 0.4
    write_time: float = 1.6
    post_wait: float = 1.4


def _anchor(coord: Optional[tuple[float, float, float]]):
    """Convert an (x, y, z) tuple to a numpy array usable by Manim."""
    from manim import np

    if coord is None:
        return None
    return np.array(coord)


def _render_step(scene: Scene, step: Step, beat: list) -> None:
    """Render a single Step on screen, attaching it to a beat group."""
    eq = MathTex(step.text, color=resolve_color(step.color)).scale(step.scale)
    if step.anchor is not None:
        eq.move_to(_anchor(step.anchor))
    eq_bg = BackgroundRectangle(eq, color=BLACK, fill_opacity=1, buff=0.25)
    eq_bg.move_to(eq.get_center())
    beat.append(eq_bg)
    beat.append(eq)
    scene.play(FadeIn(eq_bg, run_time=0.4), Write(eq, run_time=step.write_time))
    if step.sub:
        sub = Text(step.sub, font_size=22, color=resolve_color(step.sub_color) or resolve_color(step.color))
        sub.next_to(eq, DOWN, buff=0.35)
        sub_bg = BackgroundRectangle(sub, color=BLACK, fill_opacity=0.95, buff=0.15)
        sub_bg.move_to(sub.get_center())
        beat.append(sub_bg)
        beat.append(sub)
        scene.play(FadeIn(sub_bg, run_time=0.4), FadeIn(sub, run_time=0.9))
        scene.wait(step.post_wait)
    else:
        scene.wait(step.post_wait)


def render_beat(scene: Scene, steps: Iterable[Step], fade_out_at_end: bool = True):
    """Show a beat (a vertical stack of steps), then fade it out."""
    beat: list = []
    for step in steps:
        scene.wait(step.pre_wait)
        _render_step(scene, step, beat)
    if fade_out_at_end:
        scene.play(FadeOut(beat_group(*beat), run_time=0.8))
    return beat_group(*beat)


def render_split_beat(scene: Scene, left_steps, right_steps, fade_out_at_end: bool = True):
    """Show two columns of stacked steps side by side."""
    left_anchor_x = -3.0
    right_anchor_x = 3.0
    beat: list = []

    def _column(steps, anchor_x):
        col_steps = []
        anchor = None
        for step in steps:
            base = step.anchor or (anchor_x, 1.0, 0.0)
            new_step = Step(
                text=step.text,
                color=step.color,
                scale=step.scale,
                anchor=base,
                sub=step.sub,
                sub_color=step.sub_color,
                pre_wait=step.pre_wait,
                write_time=step.write_time,
                post_wait=step.post_wait,
            )
            col_steps.append(new_step)
            anchor = (base[0], base[1] - 1.1, 0.0)
        # Sort by y descending so they stack top-to-bottom
        for st in col_steps:
            scene.wait(st.pre_wait)
            _render_step(scene, st, beat)
        return col_steps

    _column(list(left_steps), left_anchor_x)
    _column(list(right_steps), right_anchor_x)

    if fade_out_at_end:
        scene.play(FadeOut(beat_group(*beat), run_time=0.8))
    return beat_group(*beat)


def build_lesson_scene(
    scene: Scene,
    *,
    title: str,
    subtitle: str,
    beats: list,
    takeaway_eq: str,
    takeaway_sub: str,
    audio_seconds: float,
    intro_hold: float = 1.4,
):
    """Run the standard 5-beat structure for a Year 10 lesson."""
    animate_intro(scene, title, subtitle, hold=intro_hold)
    intro_total = intro_hold + 4.0
    remaining = max(8.0, audio_seconds - intro_total)
    n = max(1, len(beats))
    per_beat = remaining / (n + 1)
    for beat in beats:
        if isinstance(beat, dict) and beat.get("type") == "split":
            render_split_beat(
                scene,
                beat["left"],
                beat["right"],
                fade_out_at_end=True,
            )
        elif isinstance(beat, list):
            render_beat(scene, beat, fade_out_at_end=True)
        else:
            render_beat(scene, [beat], fade_out_at_end=True)
        scene.wait(per_beat * 0.2)
    # Ensure the final definition holds long enough for the full audio to finish.
    # Adding a fixed ~3 s buffer covers the few-second rendering underrun that
    # otherwise truncates the last beat of the narration.
    final_wait = max(per_beat, audio_seconds * 0.4 + 3.0)
    animate_final_definition(scene, takeaway_eq, takeaway_sub, final_wait=final_wait)


def chart_axes(scene: Scene, *, x_range, y_range, x_label="x", y_label="y",
              x_length=8.0, y_length=4.0, stroke=WHITE):
    """Return (axes, x_label, y_label). Position them in the chart band."""
    from manim import Axes
    axes = Axes(
        x_range=list(x_range),
        y_range=list(y_range),
        x_length=x_length,
        y_length=y_length,
        tips=False,
        axis_config={"color": stroke, "include_numbers": False, "stroke_width": 1.4},
    ).move_to(BAND_CHART_CENTER)
    x_lbl = MathTex(x_label, color=stroke).scale(0.9).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
    y_lbl = MathTex(y_label, color=stroke).scale(0.9).next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
    return axes, x_lbl, y_lbl


def number_line(scene: Scene, *, x_range, length=8.0, stroke=WHITE,
               label_step=1.0):
    """Return a NumberLine configured for the safe chart band."""
    from manim import NumberLine
    return NumberLine(
        x_range=list(x_range),
        length=length,
        color=stroke,
        stroke_width=1.4,
        include_numbers=False,
    ).move_to(BAND_CHART_CENTER)