"""Manim scene for lesson `clear-numerical` (topic `m10-algebra-linear-fractions`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraLinearFractionsClearNumericalScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Clear numerical denominators',
            subtitle='Multiply both sides by the common denominator.',
            beats=[
        [
            Step(r'''\dfrac{x}{2}+\dfrac{x}{3}=5''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='start', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''\text{LCD}=6''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='least common denominator', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''6\cdot \dfrac{x}{2}+6\cdot \dfrac{x}{3}=6\cdot 5''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='multiply every term', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4),
            Step(r'''3x+2x=30''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='simplify', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''5x=30 \Rightarrow x=6''', color='GREEN_OK', scale=1.0, anchor=(0, -2.2, 0.0), sub='solve', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''\dfrac{x+1}{4}=\dfrac{x-1}{6}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='two-fraction equation', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''LCD=12''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='12', sub_color=None, write_time=1.0, post_wait=1.0, pre_wait=0.4),
            Step(r'''3(x+1)=2(x-1) \Rightarrow x=-5''', color='GREEN_OK', scale=0.9, anchor=(0, -1.2, 0.0), sub='solve', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{multiply every term by the LCD}''',
            takeaway_sub=r'''Find the least common denominator, then multiply every term by it.''',
            audio_seconds=92.4,
        )
