"""20-node prerequisite DAG for the mathematics curriculum."""

import networkx as nx

from curriculum_flow_env.simulation.curriculum import (
    TOPIC_NAMES,
    TOPIC_DIFFICULTIES,
    PREREQUISITE_EDGES,
    NUM_TOPICS,
    MASTERY_THRESHOLD,
    UNLOCK_THRESHOLD,
)


class TopicGraph:
    """Directed acyclic graph encoding topic prerequisites."""

    def __init__(self):
        self.graph = nx.DiGraph()
        for tid, name in TOPIC_NAMES.items():
            self.graph.add_node(tid, name=name, difficulty=TOPIC_DIFFICULTIES[tid])
        self.graph.add_edges_from(PREREQUISITE_EDGES)

    def get_unlocked_topics(self, mastery_dict: dict[int, float]) -> list[int]:
        """All topics are unlocked — open learning paths."""
        return list(range(NUM_TOPICS))

    def get_topic_difficulty(self, topic_id: int) -> int:
        return TOPIC_DIFFICULTIES[topic_id]

    def get_prerequisites(self, topic_id: int) -> list[int]:
        return list(self.graph.predecessors(topic_id))

    def is_mastered(self, topic_id: int, mastery_dict: dict[int, float]) -> bool:
        return mastery_dict.get(topic_id, 0.0) >= MASTERY_THRESHOLD

    def completion_rate(self, mastery_dict: dict[int, float]) -> float:
        mastered = sum(1 for t in range(NUM_TOPICS) if self.is_mastered(t, mastery_dict))
        return mastered / NUM_TOPICS
