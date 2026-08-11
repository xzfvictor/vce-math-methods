"""Manim scene for lesson `common-factor` (topic `m10-algebra-factorisation`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraFactorisationCommonFactorScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Common factor',
            subtitle='Pull the greatest thing out the front.',
            beats=[
        [
            Step(r'''6x^{2} + 9x''', color='BLUE_TERM', scale=1.05, anchor=(-3.0, 1.3, 0.0), sub='two terms', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''\text{GCD}(6,9)=3''', color='ORANGE_TERM', scale=0.95, anchor=(3.0, 1.3, 0.0), sub='numerical part', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''\text{lowest power of } x = x''', color='GREEN_OK', scale=0.9, anchor=(-3.0, -0.4, 0.0), sub='variable part', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4),
            Step(r'''\text{GCF} = 3x''', color='GREEN_OK', scale=1.1, anchor=(3.0, -0.4, 0.0), sub='combine', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''6x^{2} + 9x = 3x(2x + 3)''', color='GREEN_OK', scale=1.2, anchor=(0, 1.2, 0.0), sub='pull 3x out the front', sub_color='BLUE_TERM', write_time=2.0, post_wait=2.0, pre_wait=0.4),
            Step(r'''\dfrac{6x^{2}}{3x}=2x,\;\dfrac{9x}{3x}=3''', color='ORANGE_TERM', scale=0.9, anchor=(0, -0.4, 0.0), sub='divide each term', sub_color=None, write_time=1.8, post_wait=1.6, pre_wait=0.4)
        ],
        [
            Step(r'''3(2x+3) \;\neq\; 3x(2x+3)''', color='RED_REJECT', scale=1.0, anchor=(0, 1.2, 0.0), sub='missing the variable x', sub_color='BLUE_TERM', write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''\text{always include }x\text{ if every term has }x''', color='GREEN_OK', scale=0.85, anchor=(0, -0.4, 0.0), sub='rule', sub_color=None, write_time=1.6, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''ab+ac=a(b+c)''',
            takeaway_sub=r'''Pull out the greatest common factor; expand to check.''',
            audio_seconds=99.6,
        )
