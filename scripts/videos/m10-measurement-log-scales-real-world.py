"""Manim scene for lesson `real-world` (topic `m10-measurement-log-scales`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementLogScalesRealWorldScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Log scales in the real world',
            subtitle='They compress huge ranges onto a single chart.',
            beats=[
        [
            Step(r'''sound intensity (dB)''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='log10 axis', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''pH (acidity)''', color='BLUE_TERM', scale=1.0, anchor=(0, 0.4, 0.0), sub='log10 axis', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''Richter (earthquake)''', color='BLUE_TERM', scale=1.0, anchor=(0, -0.6, 0.0), sub='log10 axis', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''whisper ~ 30 dB''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='quiet', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''rock concert ~ 110 dB''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='loud', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''ratio = 10^{8}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='intensity ratio', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4),
            Step(r'''dB = 10\log_{10}\dfrac{I}{I_0}''', color='GREEN_OK', scale=0.9, anchor=(0, -2.2, 0.0), sub='definition', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''log scale lets huge numbers fit on one chart''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='takeaway', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{log scale: each tick is a power of the base}''',
            takeaway_sub=r'''Log scales compress wide-ranging data so small and huge values fit together.''',
            audio_seconds=82.6,
        )
