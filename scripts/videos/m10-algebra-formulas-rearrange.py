"""Manim scene for lesson `rearrange` (topic `m10-algebra-formulas`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraFormulasRearrangeScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Rearrange a formula',
            subtitle='Move letters to the side you want.',
            beats=[
        [
            Step(r'''A=lw''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='rectangle area', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''l=\dfrac{A}{w}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='solve for l', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''w=\dfrac{A}{l}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='solve for w', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''A/w = l''', color='GREEN_OK', scale=0.9, anchor=(0, -1.2, 0.0), sub='check by substitution', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''v=u+at''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='velocity', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''a=\dfrac{v-u}{t}''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='solve for a', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4),
            Step(r'''t=\dfrac{v-u}{a}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.6, 0.0), sub='solve for t', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{apply inverse operations to isolate the letter}''',
            takeaway_sub=r'''Use inverse operations to bring the letter to one side.''',
            audio_seconds=80.7,
        )
