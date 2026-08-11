"""Manim scene for lesson `model` (topic `m10-algebra-linear-eq`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraLinearEqModelScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Model with a linear equation',
            subtitle='Translate the words into x and an equation.',
            beats=[
        [
            Step(r'''a taxi charges \$3 plus \$2 per km''', color='BLUE_TERM', scale=0.85, anchor=(0, 1.4, 0.0), sub='scenario', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''cost = 3 + 2 \cdot km''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='model', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''y = 2x + 3''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='linear form', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''km=5 \Rightarrow y = 13''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='evaluate', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''plan: 100 min + \$0.10 per text''', color='BLUE_TERM', scale=0.85, anchor=(0, 1.2, 0.0), sub='second model', sub_color=None, write_time=1.8, post_wait=1.0, pre_wait=0.4),
            Step(r'''cost = 0.10n + 100''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='n = number of texts', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{cost = fixed + rate}	imes	ext{quantity}''',
            takeaway_sub=r'''Identify the fixed part and the rate, then write cost = fixed + rate × variable.''',
            audio_seconds=93.6,
        )
