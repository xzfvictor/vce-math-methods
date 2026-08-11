"""Manim scene for lesson `trees-without-replacement` (topic `m10-probability-conditional`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10ProbabilityConditionalTreesWithoutReplacementScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Probability trees without replacement',
            subtitle='Each branch shrinks the pool.',
            beats=[
        [
            Step(r'''draw two balls without putting back''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.4, 0.0), sub='without replacement', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''P(red 1st) = \dfrac{5}{12}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='branch 1', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(blue 2nd | red 1st) = \dfrac{7}{11}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='branch 2', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''P(red, then blue) = \dfrac{5}{12}\cdot \dfrac{7}{11}=\dfrac{35}{132}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='multiply', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''without replacement: counts shrink''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='rule', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''with replacement: counts stay the same''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='contrast', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''P(A	ext{ then }B)=P(A)\cdot P(B|A)''',
            takeaway_sub=r'''Each branch reduces the count: multiply along, add across.''',
            audio_seconds=91.4,
        )
