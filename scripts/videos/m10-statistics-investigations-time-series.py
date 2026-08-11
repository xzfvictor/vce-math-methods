"""Manim scene for lesson `time-series` (topic `m10-statistics-investigations`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsInvestigationsTimeSeriesScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Time series data',
            subtitle='Measure the same thing over time to see a trend.',
            beats=[
        [
            Step(r'''time on x-axis''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='always', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''value on y-axis''', color='GREEN_OK', scale=1.0, anchor=(0, 0.4, 0.0), sub='measurement', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''trend: long-term direction''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='trend', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''seasonal: repeats each year''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='season', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''residual: noise''', color='GREEN_OK', scale=0.95, anchor=(0, -1.0, 0.0), sub='residual', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''watch for seasonal spikes''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='be careful', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''smooth before forecasting''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='strategy', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{time on x, value on y}''',
            takeaway_sub=r'''Plot time on the x-axis; look for trend, season, and noise.''',
            audio_seconds=84.4,
        )
