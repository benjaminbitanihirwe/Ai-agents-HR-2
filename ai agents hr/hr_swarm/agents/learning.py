from .base import AgentBase
from core.state import HRState

class LearningAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Learning_Agent_v1",
            role="Learning & Development Coach",
            goal="Identify skill gaps and recommend training modules or courses.",
            backstory="A lifelong learner dedicated to upskilling employees based on their performance data."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        if "training" in state.natural_language_query.lower() or "learn" in state.natural_language_query.lower():
            self.report(state, "RECOMMEND_COURSE", "Suggested 'Advanced AI Agents 2026' to Engineering.")
            return {"status": "success"}
        return {"status": "skipped"}
