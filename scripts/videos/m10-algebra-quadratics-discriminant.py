"""Manim scene for lesson `discriminant` (topic `m10-algebra-quadratics`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraQuadraticsDiscriminantScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='The discriminant',
            subtitle='b^2 - 4ac tells you how many real roots there are.',
            beats=[
        [
            Step(r'''\Delta = b^{2}-4ac''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='under the square root', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''\Delta > 0''', color='GREEN_OK', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='two real roots', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''\Delta = 0''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='one repeated root', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''\Delta < 0''', color='ORANGE_TERM', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='no real roots', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''x^{2}+4x+1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='example 1', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''\Delta=16-4=12>0''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='two roots', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4),
            Step(r'''x^{2}+4x+4''', color='BLUE_TERM', scale=1.0, anchor=(0, -1.2, 0.0), sub='example 2', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''\Delta=16-16=0''', color='GREEN_OK', scale=1.0, anchor=(0, -2.2, 0.0), sub='one root', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r"""Delta = b^2 - 4ac, sign tells you how many real roots""",
            takeaway_sub=r'''Read the sign of b^2 - 4ac to know how many real roots the quadratic has.''',
            audio_seconds=79.7,
        )
