"""Manim scene for lesson `conditional-language` (topic `m10-probability-conditional`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10ProbabilityConditionalConditionalLanguageScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Conditional probability language',
            subtitle='P(A|B) means A given B.',
            beats=[
        [
            Step(r'''P(A|B) = probability of A given B''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='definition', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''B has happened, so restrict to B''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='given B', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''then ask P(A inside B)''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='restricted sample', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4),
            Step(r'''P(A|B) \neq P(B|A)''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='do not swap', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''language: given that''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='wording', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''if I know B, what is the chance of A?''', color='GREEN_OK', scale=0.85, anchor=(0, 0.0, 0.0), sub='think', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''P(A|B)=\dfrac{P(A\cap B)}{P(B)}''',
            takeaway_sub=r'''Read P(A|B) as probability of A given that B has happened.''',
            audio_seconds=81.9,
        )
