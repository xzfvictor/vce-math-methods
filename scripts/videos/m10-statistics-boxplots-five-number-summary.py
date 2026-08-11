"""Manim scene for lesson `five-number-summary` (topic `m10-statistics-boxplots`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsBoxplotsFiveNumberSummaryScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Five-number summary',
            subtitle='Min, Q1, median, Q3, max.',
            beats=[
        [
            Step(r'''min, Q1, median, Q3, max''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.4, 0.0), sub='five numbers', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''data: 2, 4, 5, 7, 9, 12, 15''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='example', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''min=2,\; max=15''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='extremes', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''median=7''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='middle', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''Q1=4,\; Q3=12''', color='GREEN_OK', scale=1.0, anchor=(0, -2.0, 0.0), sub='quartiles', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''IQR = Q3 - Q1 = 8''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='interquartile range', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''spread of the middle 50%''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='what it measures', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{IQR}=Q_{3}-Q_{1}''',
            takeaway_sub=r'''Five-number summary: min, Q1, median, Q3, max — the IQR measures the middle 50%.''',
            audio_seconds=99.5,
        )
