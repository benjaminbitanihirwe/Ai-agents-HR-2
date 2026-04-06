from .base import AgentBase
from core.state import HRState

class AnalyticsAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Analytics_Agent_v1",
            role="HR Analytics & Reporting",
            goal="Generate actionable insights from HR data (turnover, compensation equity, time-to-hire).",
            backstory="A math-wizard who spots trends in massive datasets before humans do."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        if "report" in state.natural_language_query.lower() or "metrics" in state.natural_language_query.lower():
            self.report(state, "GENERATE_REPORT", "Compiling Q2 HR Metrics Dashboards.")
            return {"status": "success", "report_url": "https://hr-dashboard.internal/q2"}
        return {"status": "skipped"}
