"""Manim scene for lesson `causation-ethics` (topic `m10-statistics-claims`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10StatisticsClaimsCausationEthicsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Causation, ethics and claims',
            subtitle='Correlation is not causation — and the data has to be ethical.',
            beats=[
        [
            Step(r'''correlation \neq causation''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.4, 0.0), sub='key warning', sub_color='ORANGE_TERM', write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''ice-cream sales correlate with drownings''', color='BLUE_TERM', scale=0.85, anchor=(0, 1.2, 0.0), sub='spurious', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''confounder: hot weather''', color='ORANGE_TERM', scale=0.95, anchor=(0, 0.0, 0.0), sub='hidden variable', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''neither causes the other''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='spurious correlation', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ],
        [
            Step(r'''ethical data: informed consent''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='principle 1', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''anonymise respondents''', color='ORANGE_TERM', scale=0.9, anchor=(0, 0.0, 0.0), sub='principle 2', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''report sources honestly''', color='GREEN_OK', scale=0.9, anchor=(0, -1.0, 0.0), sub='principle 3', sub_color=None, write_time=1.4, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''	ext{correlation}
eq	ext{causation}''',
            takeaway_sub=r'''Always check for confounders and respect the people behind the data.''',
            audio_seconds=83.4,
        )
