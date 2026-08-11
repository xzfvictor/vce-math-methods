"""Manim scene for lesson `factor-monic` (topic `m10-algebra-binomial`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraBinomialFactorMonicScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Factor a monic quadratic',
            subtitle='Find two numbers that multiply to c and add to b.',
            beats=[
        [
            Step(r'''x^{2}+bx+c''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='monic quadratic', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''x^{2}+5x+6''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='worked example', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''\text{find } m,n\text{ with } mn=6,\;m+n=5''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='conditions', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''m=2,\;n=3''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='2*3=6, 2+3=5', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''(x+2)(x+3)''', color='GREEN_OK', scale=1.1, anchor=(0, -2.2, 0.0), sub='factorised', sub_color=None, write_time=1.4, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''x^{2}-7x+12''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='negative middle', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''mn=12,\;m+n=-7 \;\Rightarrow\; m=-3,\;n=-4''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='both negative', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4),
            Step(r'''(x-3)(x-4)''', color='GREEN_OK', scale=1.1, anchor=(0, -1.2, 0.0), sub='factorised', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''x^{2}+bx+c=(x+m)(x+n),\;\;mn=c,\;m+n=b''',
            takeaway_sub=r'''Two numbers that multiply to c and add to b.''',
            audio_seconds=65.1,
        )
