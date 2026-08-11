"""Manim scene for lesson `algebraic-denominators` (topic `m10-algebra-linear-fractions`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraLinearFractionsAlgebraicDenominatorsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Clear algebraic denominators',
            subtitle='Multiply through by the algebraic denominator.',
            beats=[
        [
            Step(r'''\dfrac{3}{x}+\dfrac{2}{x-1}=1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='start', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''(x)(x-1)\cdot \dfrac{3}{x}+(x)(x-1)\cdot \dfrac{2}{x-1}=(x)(x-1)''', color='ORANGE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='multiply by x(x-1)', sub_color=None, write_time=2.0, post_wait=1.2, pre_wait=0.4),
            Step(r'''3(x-1)+2x=x^{2}-x''', color='BLUE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='simplify', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''3x-3+2x=x^{2}-x''', color='ORANGE_TERM', scale=0.95, anchor=(0, -1.0, 0.0), sub='expand', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x^{2}-6x+3=0''', color='GREEN_OK', scale=0.95, anchor=(0, -2.0, 0.0), sub='bring all to one side', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''always check x\neq 0,\; x\neq 1''', color='GREEN_OK', scale=1.0, anchor=(0, 1.2, 0.0), sub='domain restriction', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{multiply every term by the algebraic LCD}''',
            takeaway_sub=r'''Multiply through by the LCD, but never forget the domain restrictions.''',
            audio_seconds=92.4,
        )
