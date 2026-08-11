"""Manim scene for lesson `parallel` (topic `m10-algebra-gradients`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraGradientsParallelScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Parallel lines',
            subtitle='Equal gradients, different intercepts.',
            beats=[
        [
            Step(r'''y = 2x + 1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='line 1', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''y = 2x - 3''', color='BLUE_TERM', scale=1.0, anchor=(0, 0.4, 0.0), sub='line 2', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''both have gradient 2''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='parallel', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''parallel: m_{1}=m_{2}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='rule', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''different y-intercept''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='otherwise they coincide', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''y=3x+1''', color='BLUE_TERM', scale=0.9, anchor=(-3.0, 1.2, 0.0), sub='parallel form', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''y=3x+5''', color='GREEN_OK', scale=0.9, anchor=(3.0, 1.2, 0.0), sub='parallel partner', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{parallel lines have the same gradient, different intercept}''',
            takeaway_sub=r'''Same gradient; different y-intercept — that's a parallel.''',
            audio_seconds=76.6,
        )
