"""Manim scene for lesson `perpendicular` (topic `m10-algebra-gradients`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraGradientsPerpendicularScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Perpendicular lines',
            subtitle='Gradients multiply to -1.',
            beats=[
        [
            Step(r'''m_{1} \cdot m_{2} = -1''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='perpendicular condition', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''m_{1}=2''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='given', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''m_{2} = -\dfrac{1}{2}''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='flip, negate', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4),
            Step(r'''(2)(-\tfrac{1}{2}) = -1''', color='GREEN_OK', scale=1.0, anchor=(0, -1.6, 0.0), sub='check', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''m_{1}=-\tfrac{1}{3}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='negative gradient', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''m_{2}=3''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='flip, drop sign', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''m_{1}\cdot m_{2}=-1''',
            takeaway_sub=r'''Perpendicular gradients are negative reciprocals of each other.''',
            audio_seconds=85.7,
        )
