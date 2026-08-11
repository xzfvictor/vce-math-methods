"""Manim scene for lesson `pythagoras-trig` (topic `m10-measurement-trig`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10MeasurementTrigPythagorasTrigScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Pythagoras and trigonometry',
            subtitle='Right triangle → opposite, adjacent, hypotenuse.',
            beats=[
        [
            Step(r'''a^{2}+b^{2}=c^{2}''', color='BLUE_TERM', scale=1.1, anchor=(0, 1.4, 0.0), sub='Pythagoras', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4),
            Step(r'''\sin\theta=\tfrac{o}{c},\;\cos\theta=\tfrac{a}{c},\;\tan\theta=\tfrac{o}{a}''', color='GREEN_OK', scale=0.95, anchor=(0, 0.2, 0.0), sub='trig ratios', sub_color=None, write_time=2.0, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''opp=3,\; adj=4''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='given', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''hyp = \sqrt{9+16} = 5''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='Pythagoras', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''\tan\theta = \tfrac{3}{4}''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='opposite over adjacent', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''\sin\theta = \tfrac{3}{5},\;\cos\theta = \tfrac{4}{5}''', color='GREEN_OK', scale=0.95, anchor=(0, -2.0, 0.0), sub='opp/hyp, adj/hyp', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''picking the right ratio saves time''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='strategy', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''know OAH \Rightarrow pick sin/cos/tan''', color='GREEN_OK', scale=0.9, anchor=(0, -0.2, 0.0), sub='match the question', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''\sin=	frac{O}{H},\;\cos=	frac{A}{H},\;	an=	frac{O}{A}''',
            takeaway_sub=r'''Pythagoras gives the third side; trig ratios give angles or sides.''',
            audio_seconds=87.7,
        )
