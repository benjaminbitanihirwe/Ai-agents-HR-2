from .base import AgentBase
from core.state import HRState

class OffboardingAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Offboarding_Agent_v1",
            role="Offboarding Specialist",
            goal="Safely and respectfully manage employee departures, revoke access, and conduct exit interviews.",
            backstory="A professional and secure coordinator handling sensitive departure logistics."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        if "terminate" in state.natural_language_query.lower() or "offboard" in state.natural_language_query.lower():
            self.report(state, "REVOKE_ACCESS", f"Revoking IT access for {state.employee_id}")
            state.requires_human_approval = True
            state.approval_reason = f"Confirm revoking access for {state.employee_id}"
            return {"status": "pending_approval"}
        return {"status": "skipped"}
