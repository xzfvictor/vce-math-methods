"""Manim scene for lesson `interpolation-causation` (topic `m10-statistics-scatter`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsScatterInterpolationCausationScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Interpolation vs causation',
            subtitle='Between points is interpolation; outside is extrapolation. Correlation is not cause.',
            beats=[
        [
            Step(r'''between data points \to interpolate''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.4, 0.0), sub='safe', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''outside data \to extrapolate''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.4, 0.0), sub='risky', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''temperature vs ice-cream sales''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='positive correlation', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''temp 25°C \Rightarrow sales approx 200''', color='GREEN_OK', scale=0.85, anchor=(0, 0.0, 0.0), sub='interpolate', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4),
            Step(r'''temperature does NOT cause the sale''', color='ORANGE_TERM', scale=0.85, anchor=(0, -1.0, 0.0), sub='no causation', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''interpolation is safe; extrapolation is not''', color='BLUE_TERM', scale=0.85, anchor=(0, 1.2, 0.0), sub='guideline', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''correlation \neq causation''', color='GREEN_OK', scale=0.85, anchor=(0, 0.0, 0.0), sub='always', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{interpolate in range,\; extrapolate with caution}''',
            takeaway_sub=r'''Use the line between points; outside that range is guessing, not data.''',
            audio_seconds=84.5,
        )
