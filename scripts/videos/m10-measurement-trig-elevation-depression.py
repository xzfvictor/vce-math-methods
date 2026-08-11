"""Manim scene for lesson `elevation-depression` (topic `m10-measurement-trig`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementTrigElevationDepressionScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Angles of elevation and depression',
            subtitle='Above or below the horizontal line of sight.',
            beats=[
        [
            Step(r'''horizontal line of sight''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='reference', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''elevation = above horizontal''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='look up', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''depression = below horizontal''', color='ORANGE_TERM', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='look down', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''eye height = 1.7 m, \; angle = 30°''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='setup', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''tan(30°) = h / 30''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='right triangle', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''h = 30\tan(30°) \approx 17.3 m''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='evaluate', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4),
            Step(r'''total = 1.7 + 17.3 = 19 m''', color='GREEN_OK', scale=1.0, anchor=(0, -2.2, 0.0), sub='include eye height', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	an(	ext{angle}) = \dfrac{	ext{opp}}{	ext{adj}}''',
            takeaway_sub=r'''Elevation: angle above horizontal. Depression: angle below horizontal.''',
            audio_seconds=79.4,
        )
