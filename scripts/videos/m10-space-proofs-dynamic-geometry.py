"""Manim scene for lesson `dynamic-geometry` (topic `m10-space-proofs`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10SpaceProofsDynamicGeometryScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Dynamic geometry software',
            subtitle='Sketch, drag, measure — geometry you can see move.',
            beats=[
        [
            Step(r'''GeoGebra / Cabri''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='common tools', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''1. sketch the construction''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='step 1', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''2. measure key lengths''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='step 2', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''3. drag a vertex and watch''', color='GREEN_OK', scale=0.95, anchor=(0, -1.0, 0.0), sub='step 3', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4),
            Step(r'''4. conjecture: what stays the same?''', color='GREEN_OK', scale=0.95, anchor=(0, -2.0, 0.0), sub='step 4', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''useful for exploring conjectures''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='role', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''not a substitute for proof''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='limitation', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{measure, drag, conjecture, then prove}''',
            takeaway_sub=r'''Drag the figure — measure what's invariant, then write the proof.''',
            audio_seconds=86.2,
        )
