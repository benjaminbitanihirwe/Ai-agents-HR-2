from .base import AgentBase
from core.state import HRState

class PerformanceAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Performance_Agent_v1",
            role="Performance Review Coordinator",
            goal="Track KPI progress and schedule/coordinate performance review cycles.",
            backstory="A data-driven evaluator focused on objective growth metrics and constructive feedback loops."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        if "performance" in state.natural_language_query.lower() or "review" in state.natural_language_query.lower():
            self.report(state, "SCHEDULE_REVIEW", f"Initiating 360 review for {state.employee_id or 'all staff'}")
            return {"status": "success", "action": "REVIEW_CYCLE_STARTED"}
        return {"status": "skipped"}
