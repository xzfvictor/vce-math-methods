"""Manim scene for lesson `choose-model` (topic `m10-algebra-modelling`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraModellingChooseModelScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Choose a model',
            subtitle='Match the trend in the data to a function family.',
            beats=[
        [
            Step(r'''linear: y = mx + b''', color='BLUE_TERM', scale=0.95, anchor=(-3.0, 1.2, 0.0), sub='steady growth', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''quadratic: y = ax^{2}''', color='ORANGE_TERM', scale=0.95, anchor=(3.0, 1.2, 0.0), sub='parabolic shape', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''exponential: y = a\cdot b^{x}''', color='GREEN_OK', scale=0.95, anchor=(0, -0.4, 0.0), sub='compound growth', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''scatter plot''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='examine shape', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''constant rate of change \Rightarrow linear''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='differences match', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''doubling \Rightarrow exponential''', color='GREEN_OK', scale=0.9, anchor=(0, -1.2, 0.0), sub='ratios match', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{linear: equal differences; quadratic: parabolic; exponential: equal ratios}''',
            takeaway_sub=r'''Linear for steady change, quadratic for parabolic data, exponential for doubling/halving.''',
            audio_seconds=76.2,
        )
