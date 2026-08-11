"""Manim scene for lesson `negative-zero-indices` (topic `m10-algebra-exponent-laws`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraExponentLawsNegativeZeroIndicesScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Negative and zero indices',
            subtitle='Flip the term over when the exponent is negative.',
            beats=[
        [
            Step(r'''a^{0}=1''', color='BLUE_TERM', scale=1.1, anchor=(-3.0, 1.2, 0.0), sub='anything^0 = 1', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4),
            Step(r'''a^{-n}=\dfrac{1}{a^{n}}''', color='ORANGE_TERM', scale=1.1, anchor=(3.0, 1.2, 0.0), sub='negative flips', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4),
            Step(r'''a^{m-n}=\dfrac{a^{m}}{a^{n}}''', color='GREEN_OK', scale=0.95, anchor=(0, -0.4, 0.0), sub='subtract or divide', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''2^{0}=1''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='example', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''5^{-2}=\dfrac{1}{5^{2}}=\dfrac{1}{25}''', color='ORANGE_TERM', scale=0.95, anchor=(3.0, 1.2, 0.0), sub='example', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4),
            Step(r'''\dfrac{2^{3}}{2^{5}}=\dfrac{1}{2^{2}}=\dfrac{1}{4}''', color='GREEN_OK', scale=0.95, anchor=(0, -0.4, 0.0), sub='rewrite with positive exponent', sub_color=None, write_time=2.0, post_wait=1.8, pre_wait=0.4)
        ],
        [
            Step(r'''x^{-2}=x^{2}\;\;\text{(wrong)}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='negative sign matters', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.4, pre_wait=0.4),
            Step(r'''x^{-2}=\dfrac{1}{x^{2}}''', color='GREEN_OK', scale=1.1, anchor=(0, -0.4, 0.0), sub='flips to the denominator', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''a^{0}=1,\qquad a^{-n}=\dfrac{1}{a^{n}}''',
            takeaway_sub=r'''Move a negative-exponent term to the denominator and flip its sign.''',
            audio_seconds=92.8,
        )
