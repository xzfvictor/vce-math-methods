"""Manim scene for lesson `simulation` (topic `m10-probability-conditional`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10ProbabilityConditionalSimulationScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Simulate conditional probability',
            subtitle='Run trials when the formula is too hard.',
            beats=[
        [
            Step(r'''simulate \to estimate''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='method', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''1. draw N random cases''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='step 1', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''2. count B's, then A inside B''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='step 2', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''3. ratio = P(A|B)''', color='GREEN_OK', scale=0.95, anchor=(0, -1.0, 0.0), sub='step 3', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''more trials \Rightarrow better estimate''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='law of large numbers', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''watch for bias in your model''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='caveat', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{simulate: trials}	o	ext{ratio}''',
            takeaway_sub=r'''Run many trials; the ratio converges to the conditional probability.''',
            audio_seconds=82.6,
        )
