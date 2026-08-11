"""Manim scene for lesson `surveying-design` (topic `m10-measurement-trig`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementTrigSurveyingDesignScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Surveying and design',
            subtitle='Plan a survey that minimises error and effort.',
            beats=[
        [
            Step(r'''design a survey''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='plan first', sub_color='ORANGE_TERM', write_time=1.2, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''1. identify landmarks''', color='BLUE_TERM', scale=0.95, anchor=(0, 1.2, 0.0), sub='step 1', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''2. measure baselines''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='step 2', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''3. measure angles''', color='GREEN_OK', scale=0.95, anchor=(0, -1.0, 0.0), sub='step 3', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''4. triangulate''', color='GREEN_OK', scale=1.0, anchor=(0, -2.0, 0.0), sub='step 4', sub_color=None, write_time=1.2, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''triangulation gives distance via angles''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='core idea', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''baseline + two angles = full triangle''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='law of sines', sub_color=None, write_time=1.6, post_wait=1.6, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{two angles + one side = triangle}''',
            takeaway_sub=r'''Surveying: pick landmarks, measure baseline and angles, then triangulate.''',
            audio_seconds=78.6,
        )
