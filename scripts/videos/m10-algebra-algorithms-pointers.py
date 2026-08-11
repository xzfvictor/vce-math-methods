"""Manim scene for lesson `pointers` (topic `m10-algebra-algorithms`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraAlgorithmsPointersScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Pointers and references',
            subtitle='An address that points to a value in memory.',
            beats=[
        [
            Step(r'''x=10''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='x holds the value 10', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''p=&x''', color='ORANGE_TERM', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='p points to x', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''*p=10''', color='GREEN_OK', scale=1.0, anchor=(0, -0.2, 0.0), sub='dereference p to read', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''*p = 20''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='change via pointer', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x becomes 20''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='they share storage', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=20,\;p\text{ unchanged}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub="only x's value moved", sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''p	ext{ is the address of }x;\; *p	ext{ dereferences }p''',
            takeaway_sub=r'''A pointer stores an address; dereference to read or write through it.''',
            audio_seconds=80.9,
        )
