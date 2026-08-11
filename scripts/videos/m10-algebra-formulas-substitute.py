"""Manim scene for lesson `substitute` (topic `m10-algebra-formulas`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraFormulasSubstituteScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Substitute into a formula',
            subtitle='Replace each letter with its number.',
            beats=[
        [
            Step(r'''P=2(l+w)''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='perimeter of rectangle', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''l=5,\;w=3''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='values', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''P=2(5+3)''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='substitute', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''=2(8)=16''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='evaluate', sub_color=None, write_time=1.4, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''A=\dfrac{1}{2}bh''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='triangle area', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''b=6,\;h=4''', color='BLUE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='values', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''A=\dfrac{1}{2}\cdot 6\cdot 4 = 12''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='evaluate', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{substitute each letter, then evaluate}''',
            takeaway_sub=r'''Replace letters with numbers and simplify.''',
            audio_seconds=68.5,
        )
