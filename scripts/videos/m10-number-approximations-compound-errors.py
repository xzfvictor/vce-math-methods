"""Manim scene for lesson `compound-errors` (topic `m10-number-approximations`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10NumberApproximationsCompoundErrorsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Compound errors',
            subtitle='Errors stack when measurements multiply.',
            beats=[
        [
            Step(r'''error = \dfrac{|\text{approx}-\text{true}|}{|\text{true}|}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='relative error', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''length measured off by 1%, width off by 1%''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='two errors', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''area error \approx 1% + 1% = 2%''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='area', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''volume error \approx 3 \times 1% = 3%''', color='GREEN_OK', scale=0.9, anchor=(0, -1.0, 0.0), sub='volume', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''area error \neq 1% \times 1%''', color='GREEN_OK', scale=0.9, anchor=(0, -2.0, 0.0), sub='common mistake', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''more measurements \Rightarrow more error''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='compounding', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''minimise the chain of measurements''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='strategy', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{length errors add for area (2D) and volume (3D)}''',
            takeaway_sub=r'''Errors add when a derived quantity combines measurements.''',
            audio_seconds=91.8,
        )
