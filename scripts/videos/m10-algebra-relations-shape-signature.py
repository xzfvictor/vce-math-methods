"""Manim scene for lesson `shape-signature` (topic `m10-algebra-relations`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraRelationsShapeSignatureScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Shape of a relation',
            subtitle='Sketch from the form of the rule.',
            beats=[
        [
            Step(r'''y = 2x^{2}''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.4, 0.0), sub='quadratic', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''y = 3^{x}''', color='ORANGE_TERM', scale=1.0, anchor=(3.0, 1.4, 0.0), sub='exponential', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''y=2x^{2}: parabola''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='U-shape through (0,0)', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''y=3^{x}: curves up''', color='ORANGE_TERM', scale=1.0, anchor=(0, -0.2, 0.0), sub='always positive', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''y=\tfrac{1}{x}: hyperbola''', color='GREEN_OK', scale=1.0, anchor=(0, -1.6, 0.0), sub='two branches', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{shape comes from the family, not the numbers}''',
            takeaway_sub=r'''Read the form: x^2 makes a parabola, a^x curves, 1/x has two branches.''',
            audio_seconds=90.6,
        )
