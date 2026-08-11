"""Manim scene for lesson `arrays-matrices` (topic `m10-algebra-algorithms`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraAlgorithmsArraysMatricesScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Arrays and matrices',
            subtitle='A row-by-column grid of numbers.',
            beats=[
        [
            Step(r'''A=\begin{pmatrix}1&2\\3&4\end{pmatrix}''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.4, 0.0), sub='2x2 matrix', sub_color='ORANGE_TERM', write_time=2.0, post_wait=1.4, pre_wait=0.4),
            Step(r'''A[1,1]=1''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='row 1 col 1', sub_color=None, write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''A[2,1]=3''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='row 2 col 1', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''rows=2, cols=2''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='shape', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''list A[1]=[1,2]''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='first row', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''sum A=1+2+3+4=10''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='sum of all entries', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''A[i,j]	ext{ reads row }i,	ext{ column }j''',
            takeaway_sub=r'''A matrix is just a grid — row first, column second.''',
            audio_seconds=87.3,
        )
