"""Manim scene for lesson `using-logs` (topic `m10-algebra-exponentials`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10AlgebraExponentialsUsingLogsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Use logarithms',
            subtitle='Take the log of both sides to bring the exponent down.',
            beats=[
        [
            Step(r'''10^{x}=250''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='exponential equation', sub_color='ORANGE_TERM', write_time=1.4, post_wait=1.2, pre_wait=0.4)
        ],
        [
            Step(r'''\log(10^{x})=\log(250)''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='log both sides', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x\log(10)=\log(250)''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='bring down the exponent', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=\dfrac{\log(250)}{\log(10)} \approx 2.40''', color='GREEN_OK', scale=0.95, anchor=(0, -1.2, 0.0), sub='solve', sub_color=None, write_time=1.8, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''2^{x}=5''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='different base', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''x=\dfrac{\log 5}{\log 2} \approx 2.32''', color='GREEN_OK', scale=0.95, anchor=(0, -0.4, 0.0), sub='change-of-base', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r"""x = \dfrac{\log(\text{RHS})}{\log(\text{base})}""",
            takeaway_sub=r'''Take the log of both sides; the exponent comes down and becomes a multiplier.''',
            audio_seconds=76.0,
        )
