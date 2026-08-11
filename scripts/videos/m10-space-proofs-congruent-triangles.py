"""Manim scene for lesson `congruent-triangles` (topic `m10-space-proofs`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10SpaceProofsCongruentTrianglesScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Congruent triangles',
            subtitle='SSS, SAS, AAS, RHS give matching sides and angles.',
            beats=[
        [
            Step(r'''triangle \cong triangle''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='congruent', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''SSS: 3 sides match''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='side-side-side', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''SAS: 2 sides + included angle''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='side-angle-side', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''AAS: 2 angles + 1 side''', color='GREEN_OK', scale=0.95, anchor=(0, -1.0, 0.0), sub='angle-angle-side', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''RHS: right angle, hypotenuse, side''', color='GREEN_OK', scale=0.95, anchor=(0, -2.0, 0.0), sub='right triangle', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''CPCTC: corresponding parts equal''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='conclusion', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''all corresponding angles equal''', color='GREEN_OK', scale=0.95, anchor=(0, 0.0, 0.0), sub='then sides too', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''\text{SSS, SAS, AAS, RHS}\Rightarrow\triangle\cong\triangle''',
            takeaway_sub=r'''Match the right combination of sides and angles, then every part matches.''',
            audio_seconds=100.2,
        )
