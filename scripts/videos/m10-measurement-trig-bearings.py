"""Manim scene for lesson `bearings` (topic `m10-measurement-trig`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementTrigBearingsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Bearings',
            subtitle='A three-digit angle clockwise from North.',
            beats=[
        [
            Step(r'''000° = North''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='zero', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''090° = East''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='quarter turn', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''180° = South''', color='BLUE_TERM', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='half turn', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''270° = West''', color='GREEN_OK', scale=1.0, anchor=(0, 0.0, 0.0), sub='three-quarter', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''plane bears 120°''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='turn 120° from N', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''draw N-S line at start''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='reference', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''draw perpendicular to get right triangle''', color='GREEN_OK', scale=0.85, anchor=(0, -1.2, 0.0), sub='N-S/E-W', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4),
            Step(r'''opp/adj \Rightarrow tan or sin/cos''', color='GREEN_OK', scale=0.9, anchor=(0, -2.2, 0.0), sub='trig', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''remember 3 digits: 045°, 120°, 270°''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='always', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''clockwise from North''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='never anticlockwise', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''B = 000°	ext{ to }359°,\;	ext{clockwise from N}''',
            takeaway_sub=r'''Bearings are three digits, always clockwise from North.''',
            audio_seconds=77.0,
        )
