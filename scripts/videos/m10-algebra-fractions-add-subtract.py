"""Manim scene for lesson `add-subtract` (topic `m10-algebra-fractions`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraFractionsAddSubtractScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Algebraic fractions',
            subtitle='Find a common denominator, then add or subtract.',
            beats=[
        [
            Step(r'''add and subtract fractions''', color='ORANGE_TERM', scale=0.9, anchor=(0, 1.3, 0.0), sub='rule', sub_color='BLUE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''\dfrac{3}{x}+\dfrac{5}{x}=\dfrac{3+5}{x}=\dfrac{8}{x}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='same denominator', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4),
            Step(r'''\dfrac{2}{x}+\dfrac{3}{2x}=\dfrac{4+3}{2x}=\dfrac{7}{2x}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='denominator doubled', sub_color=None, write_time=2.0, post_wait=1.4, pre_wait=0.4),
            Step(r'''\dfrac{4}{x+1}-\dfrac{2}{x+1}=\dfrac{2}{x+1}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='subtract', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''\dfrac{2}{x}+\dfrac{3}{x+1}\;(\text{not }\dfrac{5}{x})''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='different denominators', sub_color='GREEN_OK', write_time=1.8, post_wait=1.4, pre_wait=0.4),
            Step(r'''=\dfrac{2(x+1)+3x}{x(x+1)}=\dfrac{5x+2}{x(x+1)}''', color='GREEN_OK', scale=0.95, anchor=(0, -0.4, 0.0), sub='expand and combine', sub_color=None, write_time=2.0, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''\dfrac{a}{d}\pm\dfrac{b}{d}=\dfrac{a\pm b}{d}''',
            takeaway_sub=r'''Match denominators, then add or subtract numerators.''',
            audio_seconds=86.8,
        )
