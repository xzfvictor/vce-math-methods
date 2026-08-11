"""Manim scene for lesson `rounding-truncation` (topic `m10-number-approximations`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10NumberApproximationsRoundingTruncationScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Rounding vs truncation',
            subtitle='Round to nearest; truncate chops the digits off.',
            beats=[
        [
            Step(r'''3.14159…''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='full value', sub_color='ORANGE_TERM', write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''to 2 d.p.: round \Rightarrow 3.14''', color='GREEN_OK', scale=1.0, anchor=(0, 0.4, 0.0), sub='look at next digit', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''to 2 d.p.: truncate \Rightarrow 3.14''', color='ORANGE_TERM', scale=1.0, anchor=(0, -0.4, 0.0), sub='chop', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''next digit \geq 5 \Rightarrow round up''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='round rule', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''next digit < 5 \Rightarrow round down''', color='BLUE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='round rule', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''2.456 \to 2.46 (round), \to 2.45 (truncate)''', color='GREEN_OK', scale=0.95, anchor=(0, -1.2, 0.0), sub='example', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''truncate always rounds toward zero''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='warning', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''truncation introduces systematic error''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='use round in practice', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{round: nearest; truncate: cut}''',
            takeaway_sub=r'''Rounding looks at the next digit; truncation just chops.''',
            audio_seconds=83.9,
        )
