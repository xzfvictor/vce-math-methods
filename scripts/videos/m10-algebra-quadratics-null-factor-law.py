"""Manim scene for lesson `null-factor-law` (topic `m10-algebra-quadratics`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraQuadraticsNullFactorLawScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Null factor law',
            subtitle='Two things multiplied to zero means at least one is zero.',
            beats=[
        [
            Step(r'''(x+2)(x+3)=0''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='factored to zero', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''AB=0''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='general form', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''A=0\text{ or }B=0''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='null factor law', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x+2=0 \Rightarrow x=-2''', color='ORANGE_TERM', scale=1.0, anchor=(0, -1.2, 0.0), sub='first bracket', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x+3=0 \Rightarrow x=-3''', color='ORANGE_TERM', scale=1.0, anchor=(0, -2.2, 0.0), sub='second bracket', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''first factorise, then apply''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='x^{2}+5x+6=0 \\Rightarrow (x+2)(x+3)=0', sub_color=None, write_time=1.8, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=-2\text{ or }x=-3''', color='GREEN_OK', scale=0.9, anchor=(0, -0.4, 0.0), sub='two roots', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''AB=0 \Longleftrightarrow A=0	ext{ or }B=0''',
            takeaway_sub=r'''Once you have two brackets multiplied to zero, each bracket gives a root.''',
            audio_seconds=82.3,
        )
