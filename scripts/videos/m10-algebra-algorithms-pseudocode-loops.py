"""Manim scene for lesson `pseudocode-loops` (topic `m10-algebra-algorithms`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraAlgorithmsPseudocodeLoopsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Pseudocode loops',
            subtitle='Repeat a block until a condition is met.',
            beats=[
        [
            Step(r'''for i = 1 to 10:''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='for loop', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''print(i)''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.2, 0.0), sub='body', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''end for''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='end block', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''while x > 0:''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='while loop', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x = x - 1''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='reduce', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''end while''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='end block', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{for: known repeats};\; 	ext{while: repeat until condition fails}''',
            takeaway_sub=r'''for when you know the count, while when you don't.''',
            audio_seconds=66.0,
        )
