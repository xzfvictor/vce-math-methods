"""Manim scene for lesson `refine` (topic `m10-algebra-numerical`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraNumericalRefineScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Bisection refinement',
            subtitle='Halve the interval each iteration.',
            beats=[
        [
            Step(r'''f(1)=-1,\;f(2)=5''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='bracket the root', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''midpoint m=1.5''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='halve the interval', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''f(1.5)=1.375''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='positive, so root is in [1, 1.5]', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''new bracket [1, 1.5]''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='keep the sign-change interval', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''repeat: midpoint, evaluate, narrow''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='iteration', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''interval shrinks by half each step''', color='GREEN_OK', scale=0.9, anchor=(0, -0.4, 0.0), sub='converges fast', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{bisection halves the bracket each iteration}''',
            takeaway_sub=r'''Take the midpoint, keep the half that still has a sign change.''',
            audio_seconds=103.3,
        )
