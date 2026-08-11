"""Manim scene for lesson `scale` (topic `m10-measurement-scaling`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementScalingScaleScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Linear scale factor',
            subtitle='Lengths scale by k, areas by k^2, volumes by k^3.',
            beats=[
        [
            Step(r'''scale factor k''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='one dimension', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''length = k \cdot L''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='linear', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''area = k^{2} \cdot A''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='2D', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''volume = k^{3} \cdot V''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='3D', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''k=2: length \times 2''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='example', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''area = 4\cdot A,\; volume = 8\cdot V''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='k^{2}=4,\\;k^{3}=8', sub_color=None, write_time=1.6, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{length }k,\;	ext{area }k^{2},\;	ext{volume }k^{3}''',
            takeaway_sub=r'''Linear: k. Area: k². Volume: k³.''',
            audio_seconds=77.4,
        )
