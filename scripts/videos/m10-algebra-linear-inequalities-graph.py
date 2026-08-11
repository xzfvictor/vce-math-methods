"""Manim scene for lesson `graph` (topic `m10-algebra-linear-inequalities`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraLinearInequalitiesGraphScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Graph an inequality',
            subtitle='The boundary line and which side to shade.',
            beats=[
        [
            Step(r'''y < 2x+1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='example', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''boundary: y = 2x+1''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='draw the line', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''y < : dashed line''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='strict inequality', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''shade below the line''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='y values less than', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''x \geq 3''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='vertical line', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x = 3: solid line''', color='GREEN_OK', scale=1.0, anchor=(0, -0.4, 0.0), sub='include the boundary', sub_color=None, write_time=1.4, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{boundary line + correct side;}\; <	ext{ dashed, }\le	ext{ solid}''',
            takeaway_sub=r'''Draw the boundary line, then shade the side that satisfies the inequality.''',
            audio_seconds=81.7,
        )
