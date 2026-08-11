"""Manim scene for lesson `two-way-venn` (topic `m10-probability-conditional`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10ProbabilityConditionalTwoWayVennScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Two-way tables and Venn diagrams',
            subtitle='Overlap shows the joint probability.',
            beats=[
        [
            Step(r'''A and B''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='overlap', sub_color='ORANGE_TERM', write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''A only + A and B = P(A)''', color='GREEN_OK', scale=1.0, anchor=(0, 0.4, 0.0), sub='partition', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''P(A) = 0.6, \; P(B) = 0.5''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='values', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(A\cap B) = 0.3''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='overlap', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(A\cup B) = 0.6 + 0.5 - 0.3 = 0.8''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='inclusion-exclusion', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''P(A|B) = \dfrac{P(A\cap B)}{P(B)}''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='from the picture', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''= \dfrac{0.3}{0.5} = 0.6''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='evaluate', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''P(A\cup B)=P(A)+P(B)-P(A\cap B)''',
            takeaway_sub=r'''Draw a Venn: total = union, joint is the overlap.''',
            audio_seconds=96.7,
        )
