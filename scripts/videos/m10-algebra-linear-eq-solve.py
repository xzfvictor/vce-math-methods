"""Manim scene for lesson `solve` (topic `m10-algebra-linear-eq`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraLinearEqSolveScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Solve a linear equation',
            subtitle='Undo each operation to isolate the variable.',
            beats=[
        [
            Step(r'''2x+3=11''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='example', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''2x+3=11''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='start', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''2x=8''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.2, 0.0), sub='subtract 3', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=4''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='divide by 2', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''\dfrac{x+2}{3}=5''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='try this', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x+2=15''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='multiply by 3', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=13''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='subtract 2', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{apply the inverse operation to both sides}''',
            takeaway_sub=r'''Work outwards from the variable until it stands alone.''',
            audio_seconds=82.0,
        )
