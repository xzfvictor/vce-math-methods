"""Manim scene for lesson `multiply-divide` (topic `m10-algebra-fractions`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraFractionsMultiplyDivideScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Multiply and divide fractions',
            subtitle='Multiply across; flip the divisor when dividing.',
            beats=[
        [
            Step(r'''\dfrac{a}{b}\cdot\dfrac{c}{d}=\dfrac{ac}{bd}''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='multiply', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''\dfrac{a}{b}\div\dfrac{c}{d}=\dfrac{a}{b}\cdot\dfrac{d}{c}''', color='ORANGE_TERM', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='flip and multiply', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''\dfrac{2}{3}\cdot\dfrac{5}{7}=\dfrac{10}{21}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='basic example', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''\dfrac{3x}{4}\cdot\dfrac{8}{9x}=\dfrac{24x}{36x}=\dfrac{2}{3}''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='cancel before multiplying', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4),
            Step(r'''\dfrac{x^{2}}{y}\div\dfrac{x}{y^{2}}=\dfrac{x^{2}}{y}\cdot\dfrac{y^{2}}{x}=xy''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='division', sub_color=None, write_time=2.0, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''\dfrac{1}{x}\div\dfrac{1}{x}=1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='reciprocal of itself', sub_color='GREEN_OK', write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''\dfrac{a/b}{c/d}=\dfrac{a}{b}\cdot\dfrac{d}{c}=\dfrac{ad}{bc}''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='generalised rule', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''\dfrac{a}{b}\cdot\dfrac{c}{d}=\dfrac{ac}{bd},\;\;\dfrac{a}{b}\div\dfrac{c}{d}=\dfrac{ad}{bc}''',
            takeaway_sub=r'''Cancel common factors first, then multiply numerators and denominators.''',
            audio_seconds=79.4,
        )
