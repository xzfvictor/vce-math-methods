"""Manim scene for lesson `quadratic-formula` (topic `m10-algebra-quadratics`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraQuadraticsQuadraticFormulaScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Quadratic formula',
            subtitle='Works for any quadratic ax^2 + bx + c = 0.',
            beats=[
        [
            Step(r'''ax^{2}+bx+c=0''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='standard form', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''x = \dfrac{-b\pm\sqrt{b^{2}-4ac}}{2a}''', color='GREEN_OK', scale=1.0, anchor=(0, 0.2, 0.0), sub='the formula', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''2x^{2}+5x-3=0''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='worked example', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''a=2,\;b=5,\;c=-3''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='identify a, b, c', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''x = \dfrac{-5\pm\sqrt{25+24}}{4}=\dfrac{-5\pm 7}{4}''', color='GREEN_OK', scale=0.85, anchor=(0, -1.2, 0.0), sub='substitute', sub_color=None, write_time=2.0, post_wait=1.2, pre_wait=0.4),
            Step(r'''x=\tfrac{1}{2} \text{ or } x=-3''', color='GREEN_OK', scale=1.0, anchor=(0, -2.2, 0.0), sub='two roots', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''discriminant \Delta = b^{2}-4ac''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='under the square root', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''\Delta>0: two roots''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='crosses x-axis twice', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''\Delta=0: one root''', color='GREEN_OK', scale=0.9, anchor=(0, -1.0, 0.0), sub='touches x-axis', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''x=\dfrac{-b\pm\sqrt{b^{2}-4ac}}{2a}''',
            takeaway_sub=r'''Plug a, b, c into the formula; the discriminant tells you how many roots.''',
            audio_seconds=86.2,
        )
