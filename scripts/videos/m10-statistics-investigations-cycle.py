"""Manim scene for lesson `cycle` (topic `m10-statistics-investigations`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsInvestigationsCycleScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Statistical investigation cycle',
            subtitle='Plan, collect, process, analyse, communicate.',
            beats=[
        [
            Step(r'''1. plan the question''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='step 1', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''2. collect data''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.4, 0.0), sub='step 2', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''3. process & analyse''', color='GREEN_OK', scale=1.0, anchor=(0, -0.6, 0.0), sub='step 3', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''4. communicate results''', color='GREEN_OK', scale=1.0, anchor=(0, -1.6, 0.0), sub='step 4', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''plan \to collect \to analyse \to communicate''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='order matters', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''loops back to plan if results surprise''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='iterative', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{plan}	o	ext{collect}	o	ext{analyse}	o	ext{communicate}''',
            takeaway_sub=r'''Investigations cycle: plan, collect, process, analyse, communicate.''',
            audio_seconds=86.4,
        )
