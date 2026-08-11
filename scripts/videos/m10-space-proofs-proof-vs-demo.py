"""Manim scene for lesson `proof-vs-demo` (topic `m10-space-proofs`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10SpaceProofsProofVsDemoScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Proof versus demonstration',
            subtitle='A proof holds for everyone; a demonstration only checks cases.',
            beats=[
        [
            Step(r'''proof: a chain of reasoning''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='general', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''demonstration: a check that works for one case''', color='GREEN_OK', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='specific', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''"every angle sum is 180°"''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='claim', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''draw one triangle and measure''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='demonstration', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''checks one example only''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='not a proof', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''formal proof: angle sum = (n-2)·180°''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='general formula', sub_color=None, write_time=1.8, post_wait=1.2, pre_wait=0.4),
            Step(r'''split into triangles, sum angles''', color='GREEN_OK', scale=0.95, anchor=(0, 0.0, 0.0), sub='construction', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{proof} = 	ext{reasoning for all cases}''',
            takeaway_sub=r'''Demonstrations verify one example; proofs justify every example.''',
            audio_seconds=85.4,
        )
