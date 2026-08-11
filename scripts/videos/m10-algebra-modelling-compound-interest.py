"""Manim scene for lesson `compound-interest` (topic `m10-algebra-modelling`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraModellingCompoundInterestScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Compound interest model',
            subtitle='Balance grows by a fixed percentage each period.',
            beats=[
        [
            Step(r'''A = P(1+r)^{n}''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='compound interest', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''P=1000,\;r=0.05,\;n=3''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='values', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''A=1000(1.05)^{3}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='substitute', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''A=1000(1.1576)\approx 1157.6''', color='GREEN_OK', scale=0.95, anchor=(0, -1.2, 0.0), sub='evaluate', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''interest is added each period''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='vs simple interest', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''growth accelerates''', color='GREEN_OK', scale=0.9, anchor=(0, -0.4, 0.0), sub='exponential curve', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''A=P(1+r)^{n}''',
            takeaway_sub=r'''Each period the balance is multiplied by (1 + rate), not just added.''',
            audio_seconds=97.0,
        )
