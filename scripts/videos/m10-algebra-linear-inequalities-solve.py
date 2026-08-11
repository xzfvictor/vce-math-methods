"""Manim scene for lesson `solve` (topic `m10-algebra-linear-inequalities`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraLinearInequalitiesSolveScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Solve a linear inequality',
            subtitle='Same steps as an equation; flip the sign when dividing by a negative.',
            beats=[
        [
            Step(r'''2x+3 > 11''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='example', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''2x+3 > 11''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='start', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''2x > 8''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.2, 0.0), sub='subtract 3', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''x > 4''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='divide by 2', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''-3x < 12''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='negative coefficient', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x > -4''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='flip the sign', sub_color=None, write_time=1.4, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{solve like an equation;}	ext{ divide by a negative flips the sign}''',
            takeaway_sub=r'''Treat it like an equation, but flip the inequality when multiplying or dividing by a negative.''',
            audio_seconds=80.6,
        )
