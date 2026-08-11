"""Manim scene for lesson `replacement-independence` (topic `m10-probability-experiments`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10ProbabilityExperimentsReplacementIndependenceScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Replacement and independence',
            subtitle='With replacement, trials are independent.',
            beats=[
        [
            Step(r'''with replacement: independent''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='key idea', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(A\cap B) = P(A)\cdot P(B)''', color='GREEN_OK', scale=1.0, anchor=(0, 0.4, 0.0), sub='independence', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''P(red 1st) = \tfrac{5}{12}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='branch 1', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''put back: P(red 2nd) = \tfrac{5}{12}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='with replacement', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(both red) = \tfrac{5}{12}\cdot\tfrac{5}{12}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='multiply', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''sampling with replacement approximates large population''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='use case', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''small population \Rightarrow without replacement''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='contrast', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''P(A\cap B)=P(A)P(B)	ext{ when independent}''',
            takeaway_sub=r'''With replacement, trials are independent; multiply the probabilities.''',
            audio_seconds=87.0,
        )
