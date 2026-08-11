"""Manim scene for lesson `grouping-in-pairs` (topic `m10-algebra-factorisation`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraFactorisationGroupingInPairsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Grouping in pairs',
            subtitle='Factor each pair, then pull out the common bracket.',
            beats=[
        [
            Step(r'''x^{2}+3x+xy+3y''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='four terms', sub_color='ORANGE_TERM', write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''(x^{2}+3x)+(xy+3y)''', color='ORANGE_TERM', scale=1.05, anchor=(0, 1.4, 0.0), sub='group into pairs', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4),
            Step(r'''x(x+3) + y(x+3)''', color='GREEN_OK', scale=1.05, anchor=(0, 0.0, 0.0), sub='factor each pair', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4),
            Step(r'''(x+3)(x+y)''', color='GREEN_OK', scale=1.15, anchor=(0, -1.2, 0.0), sub='pull out the common bracket', sub_color=None, write_time=1.8, post_wait=2.0, pre_wait=0.4)
        ],
        [
            Step(r'''ab + 2a + 3b + 6''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='try again', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''(ab+2a)+(3b+6)=a(b+2)+3(b+2)''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='common bracket b+2', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4),
            Step(r'''(b+2)(a+3)''', color='GREEN_OK', scale=1.1, anchor=(0, -1.2, 0.0), sub='final form', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''a(b+c)+d(b+c) = (a+d)(b+c)''',
            takeaway_sub=r'''Spot the common bracket across the two pair-factors.''',
            audio_seconds=81.9,
        )
