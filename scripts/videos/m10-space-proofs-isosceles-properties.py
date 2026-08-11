"""Manim scene for lesson `isosceles-properties` (topic `m10-space-proofs`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10SpaceProofsIsoscelesPropertiesScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Isosceles triangle properties',
            subtitle='Equal sides give equal base angles.',
            beats=[
        [
            Step(r'''AB = AC''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='two equal sides', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''\angle B = \angle C''', color='GREEN_OK', scale=1.1, anchor=(0, 0.2, 0.0), sub='base angles', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''draw the angle bisector AD''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='proof idea', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''△ABD ≅ △ACD (SAS)''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='shared angle + AD', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''→ \angle B = \angle C''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='congruent angles', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''converse also true''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='equiangular \\Rightarrow isosceles', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''equal base angles \Rightarrow equal sides''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='converse', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	riangle ABC	ext{ isosceles}\Longleftrightarrowngle B=ngle C''',
            takeaway_sub=r'''Equal sides come with equal base angles; equal base angles come with equal sides.''',
            audio_seconds=85.1,
        )
