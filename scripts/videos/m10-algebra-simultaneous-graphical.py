"""Manim scene for lesson `graphical` (topic `m10-algebra-simultaneous`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraSimultaneousGraphicalScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Graphical solution',
            subtitle='Read the intersection off the graph.',
            beats=[
        [
            Step(r'''y = 2x + 1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='line 1', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''y = -x + 7''', color='BLUE_TERM', scale=1.0, anchor=(0, 0.4, 0.0), sub='line 2', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''2x+1 = -x+7''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub="set y's equal", sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''3x = 6 \Rightarrow x = 2''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='solve', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''y = 2(2)+1 = 5''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='substitute back', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''(2, 5) lies on both lines''', color='GREEN_OK', scale=1.0, anchor=(0, 1.2, 0.0), sub='intersection', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''(x,y)	ext{ satisfying both equations is where the lines cross}''',
            takeaway_sub=r'''Plot both lines; the intersection is the solution.''',
            audio_seconds=74.9,
        )
