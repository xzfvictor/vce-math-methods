"""Manim scene for lesson `completing-square` (topic `m10-algebra-quadratics`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraQuadraticsCompletingSquareScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Completing the square',
            subtitle='Rewrite as a perfect square plus a constant.',
            beats=[
        [
            Step(r'''x^{2}+6x+5=0''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='start', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''x^{2}+6x=-5''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='move constant', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''(\tfrac{6}{2})^{2}=3^{2}=9''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='half the coefficient, square', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x^{2}+6x+9=4''', color='BLUE_TERM', scale=1.0, anchor=(0, -1.0, 0.0), sub='add 9 to both sides', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''(x+3)^{2}=4''', color='GREEN_OK', scale=1.1, anchor=(0, -2.0, 0.0), sub='perfect square', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4),
            Step(r'''x+3=\pm 2''', color='GREEN_OK', scale=1.0, anchor=(0, -3.0, 0.0), sub='take the root', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''x=-1 \text{ or } x=-5''', color='GREEN_OK', scale=1.0, anchor=(0, 1.2, 0.0), sub='subtract 3', sub_color=None, write_time=1.4, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''(x+	frac{b}{2})^{2}=	frac{b^{2}}{4}-c''',
            takeaway_sub=r'''Half the linear coefficient, square it, add to both sides.''',
            audio_seconds=75.0,
        )
