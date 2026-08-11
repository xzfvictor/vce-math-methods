"""Manim scene for lesson `transformations` (topic `m10-algebra-relations`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraRelationsTransformationsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Transformations of relations',
            subtitle='Shift, stretch and reflect to move the graph.',
            beats=[
        [
            Step(r'''y = x^{2}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='starting parabola', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''y = x^{2} + 3''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='shift up 3', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''y = (x-2)^{2}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='shift right 2', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''y = 2x^{2}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='stretch vertically by 2', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''y = -x^{2}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='reflect across x-axis', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''y = (x-1)^{2} - 2''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='combine: shift right 1, down 2', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{inside parentheses shifts along }x,\; 	ext{outside shifts along }y''',
            takeaway_sub=r'''Outside the bracket shifts the graph up or down; inside the bracket shifts left or right.''',
            audio_seconds=81.3,
        )
