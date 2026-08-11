"""Manim scene for lesson `difference-of-squares` (topic `m10-algebra-binomial`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraBinomialDifferenceOfSquaresScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Difference of squares',
            subtitle='Square minus square factors instantly.',
            beats=[
        [
            Step(r'''a^{2}-b^{2}''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='two perfect squares, minus', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''x^{2}-9''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='example', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''=x^{2}-3^{2}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='write as squares', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''=(x+3)(x-3)''', color='GREEN_OK', scale=1.1, anchor=(0, -1.2, 0.0), sub='drop out', sub_color=None, write_time=1.4, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''4x^{2}-25''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='with a coefficient', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''=(2x)^{2}-5^{2}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='recognise squares', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''=(2x+5)(2x-5)''', color='GREEN_OK', scale=1.1, anchor=(0, -1.2, 0.0), sub='factorised', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''a^{2}-b^{2}=(a+b)(a-b)''',
            takeaway_sub=r'''Spot two squares being subtracted — answer drops out instantly.''',
            audio_seconds=78.0,
        )
