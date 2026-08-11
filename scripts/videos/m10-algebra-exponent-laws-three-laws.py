"""Manim scene for lesson `three-laws` (topic `m10-algebra-exponent-laws`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraExponentLawsThreeLawsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Three exponent laws',
            subtitle='Product, quotient and power of a power.',
            beats=[
        [
            Step(r'''a^{m}\cdot a^{n}=a^{m+n}''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='product law', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4),
            Step(r'''\dfrac{a^{m}}{a^{n}}=a^{m-n}''', color='ORANGE_TERM', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='quotient law', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4),
            Step(r'''(a^{m})^{n}=a^{mn}''', color='GREEN_OK', scale=1.0, anchor=(0, -0.6, 0.0), sub='power of a power', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''2^{3}\cdot 2^{4} = 2^{7} = 128''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.2, 0.0), sub='3+4=7', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4),
            Step(r'''\dfrac{5^{6}}{5^{2}} = 5^{4} = 625''', color='ORANGE_TERM', scale=1.1, anchor=(0, -0.4, 0.0), sub='6-2=4', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''(x^{2})^{3}=x^{6}''', color='GREEN_OK', scale=1.1, anchor=(0, 1.2, 0.0), sub='multiply exponents', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4),
            Step(r'''x^{2}\cdot x^{3}=x^{5}''', color='GREEN_OK', scale=1.1, anchor=(0, -0.4, 0.0), sub='not x^{6}', sub_color=None, write_time=1.6, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''a^{m+n},\;a^{m-n},\;a^{mn}''',
            takeaway_sub=r'''Keep the base the same; add, subtract or multiply the exponents.''',
            audio_seconds=90.1,
        )
