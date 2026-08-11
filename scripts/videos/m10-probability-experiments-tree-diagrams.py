"""Manim scene for lesson `tree-diagrams` (topic `m10-probability-experiments`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10ProbabilityExperimentsTreeDiagramsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Tree diagrams with replacement',
            subtitle='Branches multiply, columns sum.',
            beats=[
        [
            Step(r'''P(heads) = \tfrac{1}{2}, P(tails) = \tfrac{1}{2}''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.4, 0.0), sub='one flip', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''P(HH) = \tfrac{1}{2}\cdot\tfrac{1}{2}=\tfrac{1}{4}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='two flips', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(HT) = \tfrac{1}{4}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='branch', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(TH) = \tfrac{1}{4}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='branch', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(TT) = \tfrac{1}{4}''', color='GREEN_OK', scale=1.0, anchor=(0, -2.0, 0.0), sub='branch', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4),
            Step(r'''total = 1''', color='GREEN_OK', scale=1.0, anchor=(0, -3.0, 0.0), sub='check', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''3 flips: 2^{3} = 8 leaves''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='extension', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''each leaf = \tfrac{1}{8}''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='fair', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{multiply along branches, sum down columns}''',
            takeaway_sub=r'''Multiply along the branches, sum down the columns.''',
            audio_seconds=75.9,
        )
