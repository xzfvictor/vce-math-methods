"""Manim scene for lesson `combined-applications` (topic `m10-algebra-exponent-laws`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraExponentLawsCombinedApplicationsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Combined index laws',
            subtitle='Apply product, quotient and power-of-power in order.',
            beats=[
        [
            Step(r'''\dfrac{(2x)^{3}}{x^{2}}\cdot \dfrac{1}{x}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='the question', sub_color=None, write_time=1.8, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''(2x)^{3}=2^{3}x^{3}=8x^{3}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='expand power-of-power', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4),
            Step(r'''x^{2}\cdot x = x^{3}''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='denominator: add exponents', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4),
            Step(r'''\dfrac{8x^{3}}{x^{3}} = 8''', color='GREEN_OK', scale=1.1, anchor=(0, -1.2, 0.0), sub="the x's cancel", sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''\dfrac{4a^{2}}{2a}''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='try this one', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''=2a''', color='GREEN_OK', scale=1.1, anchor=(3.0, 1.2, 0.0), sub='4/2 = 2, a^2/a = a', sub_color=None, write_time=1.4, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''a^{m}\cdot a^{n}=a^{m+n},\;\;a^{m}/a^{n}=a^{m-n}''',
            takeaway_sub=r'''Apply one law at a time and cancel common terms.''',
            audio_seconds=73.5,
        )
