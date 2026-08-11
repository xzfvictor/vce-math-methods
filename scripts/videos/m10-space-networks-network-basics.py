"""Manim scene for lesson `network-basics` (topic `m10-space-networks`)."""
import sys
sys.path.insert(0, '/home/victor/maths-decoded/scripts/videos')
from _lesson_helpers import Step, build_lesson_scene, BLUE_TERM, ORANGE_TERM, GREEN_OK, RED_REJECT
from manim import Scene


class M10SpaceNetworksNetworkBasicsScene(Scene):
    def construct(self) -> None:
        build_lesson_scene(
            self,
            title='Network basics',
            subtitle='Vertices joined by edges.',
            beats=[
        [
            Step(r'''vertex (node)''', color='BLUE_TERM', scale=1.0, anchor=(-3.0, 1.2, 0.0), sub='a point', sub_color='ORANGE_TERM', write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''edge (link)''', color='GREEN_OK', scale=1.0, anchor=(3.0, 1.2, 0.0), sub='a connection', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''degree = \# edges meeting at a vertex''', color='BLUE_TERM', scale=1.0, anchor=(0, 1.2, 0.0), sub='degree', sub_color=None, write_time=1.4, post_wait=1.0, pre_wait=0.4),
            Step(r'''vertex A degree = 3''', color='ORANGE_TERM', scale=1.0, anchor=(0, 0.0, 0.0), sub='example', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4),
            Step(r'''vertex B degree = 2''', color='GREEN_OK', scale=1.0, anchor=(0, -1.0, 0.0), sub='example', sub_color=None, write_time=1.2, post_wait=1.0, pre_wait=0.4)
        ],
        [
            Step(r'''handshake lemma: sum of degrees = 2·(\# edges)''', color='BLUE_TERM', scale=0.9, anchor=(0, 1.2, 0.0), sub='key fact', sub_color=None, write_time=1.6, post_wait=1.0, pre_wait=0.4),
            Step(r'''each edge contributes 2 to the sum''', color='GREEN_OK', scale=0.9, anchor=(0, 0.0, 0.0), sub='why', sub_color=None, write_time=1.6, post_wait=1.4, pre_wait=0.4)
        ]
    ],
            takeaway_eq=r'''\sum 	ext{degrees}=2|	ext{edges}|''',
            takeaway_sub=r'''Vertices joined by edges; the handshake lemma links degrees and edges.''',
            audio_seconds=86.0,
        )
