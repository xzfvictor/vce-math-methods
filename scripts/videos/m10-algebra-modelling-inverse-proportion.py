"""Manim scene for lesson `inverse-proportion` (topic `m10-algebra-modelling`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraModellingInverseProportionScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Inverse proportion',
            subtitle='When one doubles, the other halves.',
            beats=[
        [
            Step(r'''y = \dfrac{k}{x}''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='inverse proportion', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''xy = k''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='product is constant', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=2 \Rightarrow y=\tfrac{k}{2}''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='double x, halve y', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=4 \Rightarrow y=\tfrac{k}{4}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.2, 0.0), sub='double again', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''speed \times time = distance''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='fixed trip', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''t=\dfrac{d}{v}''', color='GREEN_OK', scale=0.9, anchor=(0, -0.4, 0.0), sub='time shrinks with speed', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''y=\dfrac{k}{x}\Longleftrightarrow xy=k''',
            takeaway_sub=r'''When x doubles, y halves — the product xy stays the same.''',
            audio_seconds=76.2,
        )
