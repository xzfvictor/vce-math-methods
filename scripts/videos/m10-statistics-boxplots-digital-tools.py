"""Manim scene for lesson `digital-tools` (topic `m10-statistics-boxplots`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsBoxplotsDigitalToolsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Digital tools for boxplots',
            subtitle='Spreadsheets and calculators draw them in seconds.',
            beats=[
        [
            Step(r'''spreadsheet / calculator''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='tools', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''1. enter the data''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='step 1', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''2. ask for quartiles''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='step 2', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''3. insert chart''', color='GREEN_OK', scale=0.95, anchor=(0, -1.0, 0.0), sub='step 3', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''4. choose box plot''', color='GREEN_OK', scale=0.95, anchor=(0, -2.0, 0.0), sub='step 4', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''always check the units on the axis''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='caveat', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''tools can mis-label outliers''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='sanity check', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{enter data 	o quartiles 	o box plot}''',
            takeaway_sub=r'''Use a spreadsheet or calculator to find the quartiles, then insert the box plot.''',
            audio_seconds=78.4,
        )
