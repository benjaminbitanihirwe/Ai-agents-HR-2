from .base import AgentBase
from core.state import HRState

class CultureAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Culture_Agent_v1",
            role="Engagement & Culture Ambassador",
            goal="Monitor employee morale, organize team building, and ensure cultural alignment.",
            backstory="An empathetic and proactive planner who builds community and psychological safety."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        if "culture" in state.natural_language_query.lower() or "survey" in state.natural_language_query.lower():
            self.report(state, "SEND_SURVEY", "Deploying weekly pulse survey to Slack.")
            return {"status": "success"}
        return {"status": "skipped"}
