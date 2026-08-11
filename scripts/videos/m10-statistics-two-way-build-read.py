"""Manim scene for lesson `build-read` (topic `m10-statistics-two-way`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsTwoWayBuildReadScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Build and read two-way tables',
            subtitle='Two variables, one grid of counts.',
            beats=[
        [
            Step(r'''rows: category 1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='first variable', sub_color='ORANGE_TERM', write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''columns: category 2''', color='GREEN_OK', scale=1.0, anchor=(0, 0.4, 0.0), sub='second variable', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''total row + total column''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='margins', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''read joint frequency from a cell''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='inside', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''read marginal from a total''', color='GREEN_OK', scale=0.95, anchor=(0, -1.0, 0.0), sub='edges', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''check row totals match column totals''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='sanity check', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{rows}	imes	ext{columns}=	ext{two-way table}''',
            takeaway_sub=r'''Rows are one category, columns the other; totals lie on the edges.''',
            audio_seconds=80.5,
        )
