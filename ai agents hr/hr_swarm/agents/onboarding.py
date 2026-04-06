from .base import AgentBase
from core.state import HRState

class OnboardingAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Onboarding_Agent_v1",
            role="Onboarding Specialist",
            goal="Ensure smooth transition for new hires (IT setup, intro meetings).",
            backstory="Detail-oriented coordinator who ensures new employees feel welcomed and equipped from day one."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        if state.target_action == "onboard" or "onboard" in state.natural_language_query.lower():
            self.report(state, "PROVISION_IT", f"Requested laptop and accounts for {state.candidate_id or state.employee_id}")
            return {"status": "success", "action": "ONBOARDING_INITIALIZED"}
        return {"status": "skipped"}
