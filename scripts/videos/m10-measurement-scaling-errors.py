"""Manim scene for lesson `errors` (topic `m10-measurement-scaling`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementScalingErrorsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Absolute and relative error',
            subtitle='Error = measured minus true.',
            beats=[
        [
            Step(r'''error = \text{measured} - \text{true}''', color='BLUE_TERM', scale=1.05, anchor=(0, 1.4, 0.0), sub='signed error', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''|error| = \text{absolute error}''', color='GREEN_OK', scale=1.05, anchor=(0, 0.4, 0.0), sub='magnitude', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''true = 50 cm''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='exact', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''measured = 49 cm''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='off by 1', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''absolute error = 1 cm''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='|49-50|', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''relative error = 1/50 = 0.02 = 2%''', color='GREEN_OK', scale=0.95, anchor=(0, -2.2, 0.0), sub='relative', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''true = 5 km,\; measured = 4.99 km''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='different scale', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''abs error = 0.01 km = 10 m''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='same units', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''relative error = 0.01/5 = 0.002 = 0.2%''', color='GREEN_OK', scale=0.9, anchor=(0, -1.2, 0.0), sub='small relative', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{relative error}=\dfrac{|	ext{meas}-	ext{true}|}{	ext{true}}''',
            takeaway_sub=r'''Absolute error is in your units; relative error is a fraction of the true value.''',
            audio_seconds=92.8,
        )
