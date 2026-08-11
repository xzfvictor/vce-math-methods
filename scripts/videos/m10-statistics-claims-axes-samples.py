"""Manim scene for lesson `axes-samples` (topic `m10-statistics-claims`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsClaimsAxesSamplesScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Axes, units and samples',
            subtitle='Always label both axes and state the sample size.',
            beats=[
        [
            Step(r'''x-axis: independent variable''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='what you change', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''y-axis: dependent variable''', color='GREEN_OK', scale=1.0, anchor=(0, 0.4, 0.0), sub='what you measure', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''scale: starts at zero?''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='check 1', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''units labelled?''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='check 2', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''n = ?''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='check 3', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''small n \Rightarrow read with care''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='small sample', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''big n \Rightarrow more reliable''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='big sample', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{label axes, units, sample size}''',
            takeaway_sub=r'''Label every axis, the units, and the sample size n.''',
            audio_seconds=76.2,
        )
