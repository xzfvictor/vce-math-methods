"""Manim scene for lesson `expand-foil` (topic `m10-algebra-binomial`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraBinomialExpandFoilScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Expand with FOIL',
            subtitle='First, Outer, Inner, Last.',
            beats=[
        [
            Step(r'''(x+2)(x+3)''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='two binomials', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''F: x\cdot x = x^{2}''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='first', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''O: x\cdot 3 = 3x''', color='ORANGE_TERM', scale=1.0, anchor=(-1.0, 1.2, 0.0), sub='outer', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''I: 2\cdot x = 2x''', color='ORANGE_TERM', scale=1.0, anchor=(1.0, 1.2, 0.0), sub='inner', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''L: 2\cdot 3 = 6''', color='BLUE_TERM', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='last', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''x^{2}+5x+6''', color='GREEN_OK', scale=1.1, anchor=(0, -0.4, 0.0), sub='combine like terms', sub_color=None, write_time=1.6, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''(2x+3)(x-4)''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='try this', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''=2x^{2}-8x+3x-12''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='apply FOIL', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''=2x^{2}-5x-12''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='combine', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''(a+b)(c+d)=ac+ad+bc+bd''',
            takeaway_sub=r'''FOIL — first, outer, inner, last.''',
            audio_seconds=83.4,
        )
