"""Manim scene for lesson `reading-scale` (topic `m10-measurement-log-scales`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementLogScalesReadingScaleScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Read a log scale',
            subtitle='Each gridline jumps by a power of the base.',
            beats=[
        [
            Step(r'''pH scale''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='logarithmic axis', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''each step = x10 concentration''', color='GREEN_OK', scale=0.9, anchor=(0, 0.4, 0.0), sub='powers of 10', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''pH=3''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='position 3', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''=10^{-3} M''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='convert', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4),
            Step(r'''pH=5''', color='BLUE_TERM', scale=1.0, anchor=(0, -1.2, 0.0), sub='two steps to the right', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''=10^{-5} M \;\text{(100x less)}''', color='GREEN_OK', scale=0.9, anchor=(0, -2.2, 0.0), sub='two orders of magnitude', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''Richter scale: each +1 \Rightarrow \times 10''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='log10 axis', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''magnitude 5 vs magnitude 7''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='compare', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''magnitude 7 \Rightarrow 100\times energy''', color='GREEN_OK', scale=0.9, anchor=(0, -1.2, 0.0), sub='factor of 100', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''\log_{10}	ext{ scale: each tick} = 	imes 10''',
            takeaway_sub=r'''Each major tick on a log scale multiplies by the base.''',
            audio_seconds=88.2,
        )
