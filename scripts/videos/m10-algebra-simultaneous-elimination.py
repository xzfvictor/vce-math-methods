"""Manim scene for lesson `elimination` (topic `m10-algebra-simultaneous`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraSimultaneousEliminationScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Solve by elimination',
            subtitle='Add or subtract equations to cancel one variable.',
            beats=[
        [
            Step(r'''2x + 3y = 12''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='eq 1', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''5x - 3y =  9''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.4, 0.0), sub='eq 2', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''3y and -3y cancel''', color='GREEN_OK', scale=1.0, anchor=(0, 1.2, 0.0), sub='add the equations', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''7x = 21''', color='BLUE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='result', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x = 3''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='divide by 7', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''2(3)+3y=12 \Rightarrow y=2''', color='GREEN_OK', scale=1.0, anchor=(0, -2.0, 0.0), sub='back-substitute', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''x + y = 5''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='simple case', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x - y = 1''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='subtract to cancel y', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''2x = 6 \Rightarrow x=3,\;y=2''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='solve', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{add/subtract the equations to cancel one variable}''',
            takeaway_sub=r'''If the coefficients match (or are opposites), add or subtract to drop one variable.''',
            audio_seconds=74.8,
        )
