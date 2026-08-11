"""Manim scene for lesson `percentages-association` (topic `m10-statistics-two-way`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsTwoWayPercentagesAssociationScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Percentages and association',
            subtitle='Compare column percentages to see which group has the higher rate.',
            beats=[
        [
            Step(r'''compare percentages, not counts''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.4, 0.0), sub='fair comparison', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''Group A: 30/100 = 30% pass''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='A', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''Group B: 20/50 = 40% pass''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='B', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4),
            Step(r'''B has the higher rate''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='even though n differs', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''column percentages = within-column comparisons''', color='BLUE_TERM', scale=0.85, anchor=(0, 1.2, 0.0), sub='rule', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''row percentages = within-row comparisons''', color='GREEN_OK', scale=0.85, anchor=(0, 0.0, 0.0), sub='rule', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{column % = within-column rate}''',
            takeaway_sub=r'''Use percentages (not counts) when the group sizes differ.''',
            audio_seconds=73.7,
        )
