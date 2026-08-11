"""Manim scene for lesson `matching-bases` (topic `m10-algebra-exponentials`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraExponentialsMatchingBasesScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Match the bases',
            subtitle='Rewrite both sides with the same base, then line up exponents.',
            beats=[
        [
            Step(r'''9^{x}=27''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='exponential equation', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''9=3^{2}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='left as base 3', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''27=3^{3}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='right as base 3', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''(3^{2})^{x}=3^{3}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='same base', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''2x=3 \Rightarrow x=\tfrac{3}{2}''', color='GREEN_OK', scale=1.0, anchor=(0, -2.2, 0.0), sub='solve the linear equation', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''8^{x}=2^{6}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='try this', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''(2^{3})^{x}=2^{6} \Rightarrow 3x=6 \Rightarrow x=2''', color='GREEN_OK', scale=0.9, anchor=(0, -0.4, 0.0), sub='same approach', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''a^{m}=a^{n} \Rightarrow m=n	ext{ (when }a>0,\;a
eq 1)''',
            takeaway_sub=r'''Rewrite both sides with the same base, then solve the linear equation in the exponent.''',
            audio_seconds=64.8,
        )
