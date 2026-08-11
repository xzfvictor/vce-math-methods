"""Manim scene for lesson `surface-area` (topic `m10-measurement-area-volume`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementAreaVolumeSurfaceAreaScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Surface area',
            subtitle="Add up every face's area.",
            beats=[
        [
            Step(r'''rectangular prism''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='3 pairs of faces', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''length=4,\;width=3,\;height=2''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='dimensions', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''top+bottom = 2(4\cdot 3) = 24''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='pair of faces', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4),
            Step(r'''front+back = 2(4\cdot 2) = 16''', color='ORANGE_TERM', scale=0.9, anchor=(0, -1.0, 0.0), sub='another pair', sub_color=None, write_time=1.8, post_wait=1.0, pre_wait=0.4),
            Step(r'''sides = 2(3\cdot 2) = 12''', color='ORANGE_TERM', scale=0.9, anchor=(0, -2.0, 0.0), sub='third pair', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''surface area = 24+16+12 = 52''', color='GREEN_OK', scale=1.05, anchor=(0, -3.0, 0.0), sub='total', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''sphere: SA = 4\pi r^{2}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='curved surface', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''cylinder: SA = 2\pi r^{2} + 2\pi r h''', color='GREEN_OK', scale=0.9, anchor=(0, -0.2, 0.0), sub='two circles plus rectangle', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''SA_{	ext{box}}=2(lw+lh+wh)''',
            takeaway_sub=r'''Surface area = sum of the areas of every face.''',
            audio_seconds=88.2,
        )
