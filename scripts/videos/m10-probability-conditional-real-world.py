"""Manim scene for lesson `real-world` (topic `m10-probability-conditional`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10ProbabilityConditionalRealWorldScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Real-world conditional probability',
            subtitle='Filter the sample space, then count.',
            beats=[
        [
            Step(r'''disease: 1% have it''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.4, 0.0), sub='prevalence', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''test: 95% sensitivity''', color='BLUE_TERM', scale=0.95, anchor=(0, 0.4, 0.0), sub='test stats', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(positive | disease) = 0.95''', color='GREEN_OK', scale=0.9, anchor=(0, -0.6, 0.0), sub='sensitivity', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''P(disease | positive) \neq 0.95''', color='ORANGE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='the trick', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''most positives are false positives''', color='GREEN_OK', scale=0.95, anchor=(0, 0.0, 0.0), sub='rare disease', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''use Bayes' theorem''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='the tool', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''P(A|B)=\dfrac{P(B|A)P(A)}{P(B)}''',
            takeaway_sub=r'''P(A|B) is not the same as P(B|A). Use Bayes when you flip the order.''',
            audio_seconds=94.5,
        )
