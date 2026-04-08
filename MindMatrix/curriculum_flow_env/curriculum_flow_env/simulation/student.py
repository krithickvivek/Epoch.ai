"""Student cognitive model with 5 learner archetypes."""

import math
import random
from collections import deque

from curriculum_flow_env.simulation.curriculum import NUM_TOPICS, TOPIC_DIFFICULTIES
from curriculum_flow_env.simulation.topic_graph import TopicGraph


ARCHETYPES = {
    "fast":       {"base_learning_rate": 0.22, "forgetting_rate": 0.015, "engagement_decay": 0.01},
    "steady":     {"base_learning_rate": 0.14, "forgetting_rate": 0.02,  "engagement_decay": 0.005},
    "struggling": {"base_learning_rate": 0.08, "forgetting_rate": 0.04,  "engagement_decay": 0.02},
    "bursty":     {"base_learning_rate": 0.18, "forgetting_rate": 0.035, "engagement_decay": 0.015},
    "anxious":    {"base_learning_rate": 0.11, "forgetting_rate": 0.025, "engagement_decay": 0.03},
}


class StudentModel:
    """Simulates a student working through the curriculum."""

    def __init__(self, topic_graph: TopicGraph, archetype: str | None = None):
        self.topic_graph = topic_graph
        self.archetype: str = ""
        self.base_learning_rate: float = 0.0
        self.forgetting_rate: float = 0.0
        self.engagement_decay: float = 0.0
        self.mastery: dict[int, float] = {}
        self.engagement: float = 0.0
        self.recent_responses: deque = deque(maxlen=10)
        self.time_since_review: dict[int, int] = {}
        self.current_topic: int = 0
        self.reset(archetype)

    def reset(self, archetype: str | None = None) -> None:
        if archetype is None:
            archetype = random.choice(list(ARCHETYPES.keys()))
        self.archetype = archetype
        params = ARCHETYPES[archetype]
        self.base_learning_rate = params["base_learning_rate"]
        self.forgetting_rate = params["forgetting_rate"]
        self.engagement_decay = params["engagement_decay"]
        self.mastery = {t: 0.0 for t in range(NUM_TOPICS)}
        self.engagement = 0.8
        self.recent_responses = deque(maxlen=10)
        self.time_since_review = {t: 0 for t in range(NUM_TOPICS)}
        self.current_topic = 0

    def prerequisite_bonus(self, topic_id: int) -> float:
        prereqs = self.topic_graph.get_prerequisites(topic_id)
        if not prereqs:
            return 1.25
        mean_mastery = sum(self.mastery[p] for p in prereqs) / len(prereqs)
        return 1.0 + 0.5 * mean_mastery

    def attempt_problem(self, topic_id: int, difficulty: int) -> bool:
        self.current_topic = topic_id
        # Base probability includes discovery floor (natural guessing ability)
        discovery_floor = max(0.05, 0.3 - 0.04 * difficulty)
        base_prob = discovery_floor + self.mastery[topic_id] * (1 - 0.08 * difficulty)
        engagement_modifier = 0.6 + 0.4 * self.engagement
        prob_correct = max(0.1, min(0.95, base_prob * engagement_modifier))
        result = random.random() < prob_correct

        if result:
            bonus = self.prerequisite_bonus(topic_id)
            self.mastery[topic_id] += self.base_learning_rate * max(0.3, self.engagement) * bonus
            self.engagement = min(1.0, self.engagement + 0.06)
        else:
            # Small mastery penalty, learn a little even from failure
            self.mastery[topic_id] -= 0.005
            self.mastery[topic_id] += self.base_learning_rate * 0.1  # exposure learning
            self.engagement = max(0.0, self.engagement - 0.03)

        # Natural engagement recovery toward baseline (mean-reversion)
        self.engagement += (0.5 - self.engagement) * 0.01

        self.recent_responses.append(result)
        self.time_since_review[topic_id] = 0

        # Increment time and apply forgetting for other topics
        for t in range(NUM_TOPICS):
            if t != topic_id:
                self.time_since_review[t] += 1
                # Forgetting only kicks in after a grace period of 3 steps
                if self.time_since_review[t] > 3:
                    idle = self.time_since_review[t] - 3
                    decay = self.forgetting_rate * math.log(1 + idle) * 0.3
                    self.mastery[t] = max(0.0, self.mastery[t] - decay)

        # Clamp all mastery
        for t in range(NUM_TOPICS):
            self.mastery[t] = max(0.0, min(1.0, self.mastery[t]))

        return result

    def take_assessment(self, topic_id: int) -> float:
        difficulty = TOPIC_DIFFICULTIES[topic_id]
        correct = 0
        for _ in range(5):
            discovery_floor = max(0.05, 0.3 - 0.04 * difficulty)
            base_prob = discovery_floor + self.mastery[topic_id] * (1 - 0.08 * difficulty)
            engagement_modifier = 0.6 + 0.4 * self.engagement
            prob = max(0.1, min(0.95, base_prob * engagement_modifier))
            if random.random() < prob:
                correct += 1
        return correct / 5.0

    def get_observation(self) -> dict:
        mastery_list = [self.mastery[t] for t in range(NUM_TOPICS)]
        tsr_list = [min(self.time_since_review[t], 50) for t in range(NUM_TOPICS)]
        recent = list(self.recent_responses)
        recent_acc = recent + [0.0] * (10 - len(recent))  # pad to 10
        return {
            "mastery": mastery_list,
            "engagement": self.engagement,
            "recent_accuracy": [float(r) for r in recent_acc],
            "time_since_review": tsr_list,
            "current_topic": self.current_topic,
        }
