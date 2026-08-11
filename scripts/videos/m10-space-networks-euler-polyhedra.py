"""Manim scene for lesson `euler-polyhedra` (topic `m10-space-networks`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10SpaceNetworksEulerPolyhedraScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title="Euler's formula for polyhedra",
            subtitle='V - E + F = 2 for every convex polyhedron.',
            beats=[
        [
            Step(r'''cube: V=8, E=12, F=6''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='count', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''8-12+6 = 2''', color='GREEN_OK', scale=1.0, anchor=(0, 0.2, 0.0), sub='Euler', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''tetrahedron: V=4, E=6, F=4''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='count', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''4-6+4 = 2''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='Euler', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4),
            Step(r'''icosahedron: V=12, E=30, F=20''', color='BLUE_TERM', scale=0.95, anchor=(0, -1.0, 0.0), sub='count', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''12-30+20 = 2''', color='GREEN_OK', scale=1.0, anchor=(0, -2.0, 0.0), sub='Euler', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''Euler's formula: V - E + F = 2''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.2, 0.0), sub='general', sub_color=None, write_time=1.6, post_wait=1.2, pre_wait=0.4),
            Step(r'''works for every convex polyhedron''', color='GREEN_OK', scale=0.9, anchor=(0, -0.2, 0.0), sub='caveat', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''V - E + F = 2''',
            takeaway_sub=r'''Count vertices, edges, faces on any convex polyhedron — they always sum to 2.''',
            audio_seconds=93.6,
        )
