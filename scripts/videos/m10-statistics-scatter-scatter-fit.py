"""Manim scene for lesson `scatter-fit` (topic `m10-statistics-scatter`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsScatterScatterFitScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Scatter and line of best fit',
            subtitle='Eye-ball a line through the cloud of points.',
            beats=[
        [
            Step(r'''(x, y) pairs''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='scatter', sub_color='ORANGE_TERM', write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''draw a line close to most points''', color='GREEN_OK', scale=1.0, anchor=(0, 0.4, 0.0), sub='fit', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''balance points above and below''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='balance', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''follow the trend, not the outliers''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='ignore outliers', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''line goes through (\bar{x},\bar{y})''', color='GREEN_OK', scale=0.95, anchor=(0, -1.0, 0.0), sub='mean point', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''slope = \dfrac{\text{rise}}{\text{run}}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='use the line', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''y = mx + b''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='equation', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{line of best fit: balance above and below}''',
            takeaway_sub=r'''Draw the line that balances the points above and below; it passes through the mean point.''',
            audio_seconds=76.3,
        )
