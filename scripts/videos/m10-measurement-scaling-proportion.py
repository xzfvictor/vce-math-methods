"""Manim scene for lesson `proportion` (topic `m10-measurement-scaling`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementScalingProportionScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Direct proportion',
            subtitle='When one doubles, the other doubles too.',
            beats=[
        [
            Step(r'''y = kx''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='directly proportional', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''x=2 \Rightarrow y=2k''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='double x', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=4 \Rightarrow y=4k''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='double again', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''ratio y/x = k \text{ (constant)}''', color='GREEN_OK', scale=0.95, anchor=(0, -1.2, 0.0), sub='the test', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''5 kg of flour costs \$12''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='real-world', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''8 kg costs \dfrac{8}{5}\cdot 12 = 19.2''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='scale up', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''\dfrac{y_{1}}{x_{1}}=\dfrac{y_{2}}{x_{2}}''',
            takeaway_sub=r'''If y/x stays constant, y and x are directly proportional.''',
            audio_seconds=99.4,
        )
