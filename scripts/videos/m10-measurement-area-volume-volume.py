"""Manim scene for lesson `volume` (topic `m10-measurement-area-volume`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementAreaVolumeVolumeScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Volume',
            subtitle='Length × cross-section area.',
            beats=[
        [
            Step(r'''V = \text{base area} \times \text{height}''', color='BLUE_TERM', scale=1.05, anchor=(0, 1.4, 0.0), sub='prism rule', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''V = l\times w\times h''', color='BLUE_TERM', scale=1.05, anchor=(0, 1.2, 0.0), sub='rectangular prism', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''l=4,\;w=3,\;h=2 \Rightarrow V=24''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='example', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4),
            Step(r'''V = \pi r^{2} h''', color='ORANGE_TERM', scale=1.0, anchor=(0, -1.2, 0.0), sub='cylinder', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''V = \tfrac{1}{3}\pi r^{2} h''', color='GREEN_OK', scale=1.0, anchor=(0, -2.2, 0.0), sub='cone', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''V = \tfrac{4}{3}\pi r^{3}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='sphere', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''r=3 \Rightarrow V = 36\pi''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='evaluate', sub_color=None, write_time=1.4, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''V=	ext{base area}	imes 	ext{height}''',
            takeaway_sub=r'''Volume = area of the base times the perpendicular height.''',
            audio_seconds=83.7,
        )
