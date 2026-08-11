"""Manim scene for lesson `comparing-displays` (topic `m10-statistics-boxplots`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsBoxplotsComparingDisplaysScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Comparing boxplots',
            subtitle='Side-by-side boxes tell you which group is bigger or more spread out.',
            beats=[
        [
            Step(r'''two datasets, two boxplots''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='compare', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''Class A: median=65, IQR=10''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='Class A', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''Class B: median=72, IQR=12''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='Class B', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''B > A on the median''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='centre', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4),
            Step(r'''B more spread out''', color='GREEN_OK', scale=1.0, anchor=(0, -2.0, 0.0), sub='spread', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''compare centre, spread, shape''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='three checks', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''outliers: only in A''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='shape', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{centre, spread, shape, outliers}''',
            takeaway_sub=r'''Compare boxplots on centre, spread, shape and any outliers.''',
            audio_seconds=83.8,
        )
