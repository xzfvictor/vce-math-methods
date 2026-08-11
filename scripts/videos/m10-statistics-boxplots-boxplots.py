"""Manim scene for lesson `boxplots` (topic `m10-statistics-boxplots`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsBoxplotsBoxplotsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Boxplots',
            subtitle='A picture of the five-number summary.',
            beats=[
        [
            Step(r'''box = Q1 to Q3''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='middle 50%', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''line inside = median''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.4, 0.0), sub='Q2', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''whiskers = min and max''', color='GREEN_OK', scale=1.0, anchor=(0, -0.6, 0.0), sub='outliers excluded', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''data 2,4,5,7,9,12,15''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='example', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''left whisker to 2''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='min', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''box from 4 to 12''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='Q1-Q3', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''right whisker to 15''', color='GREEN_OK', scale=1.0, anchor=(0, -2.0, 0.0), sub='max', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''outliers plotted separately''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='1.5 IQR rule', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''skew: long whisker \Rightarrow skewed''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='shape', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{box=Q1--Q3,\; line=median,\; whiskers=min,max}''',
            takeaway_sub=r'''A boxplot shows the five-number summary as a box and whiskers.''',
            audio_seconds=92.2,
        )
