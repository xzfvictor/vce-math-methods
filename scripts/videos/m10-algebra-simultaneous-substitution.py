"""Manim scene for lesson `substitution` (topic `m10-algebra-simultaneous`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraSimultaneousSubstitutionScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Solve by substitution',
            subtitle='Solve one equation for x or y, then swap into the other.',
            beats=[
        [
            Step(r'''y = 2x+1''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.4, 0.0), sub='already solved', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''3x+2y = 16''', color='ORANGE_TERM', scale=1.0, anchor=(3.0, 1.4, 0.0), sub='the other equation', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''3x+2(2x+1)=16''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='substitute', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''3x+4x+2=16''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='expand', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''7x=14 \Rightarrow x=2''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='solve', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''y=2(2)+1=5''', color='GREEN_OK', scale=1.0, anchor=(0, -2.2, 0.0), sub='back-substitute', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''solution: (2, 5)''', color='GREEN_OK', scale=1.2, anchor=(0, 1.2, 0.0), sub='both equations satisfied', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{isolate, substitute, solve, then back-substitute}''',
            takeaway_sub=r'''Solve one equation for a variable, then swap into the other.''',
            audio_seconds=83.9,
        )
