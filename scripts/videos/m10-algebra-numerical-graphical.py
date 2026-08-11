"""Manim scene for lesson `graphical` (topic `m10-algebra-numerical`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraNumericalGraphicalScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Graphical root-finding',
            subtitle='Where the curve crosses the x-axis.',
            beats=[
        [
            Step(r'''y = x^{3} - x - 1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='target equation', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''x=1 \Rightarrow y=-1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='test x=1', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=2 \Rightarrow y=5''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='sign changes between', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''sign change \Rightarrow root between 1 and 2''', color='GREEN_OK', scale=0.9, anchor=(0, -1.2, 0.0), sub='intermediate value theorem', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''refine: x=1.3 \Rightarrow y\approx -0.003''', color='GREEN_OK', scale=0.85, anchor=(0, 1.2, 0.0), sub='narrower bracket', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{root} = x 	ext{ where } y(x)=0''',
            takeaway_sub=r'''Sketch the graph and read off where it crosses the x-axis.''',
            audio_seconds=87.3,
        )
