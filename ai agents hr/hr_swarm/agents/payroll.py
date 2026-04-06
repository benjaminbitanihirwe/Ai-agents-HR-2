from .base import AgentBase
from core.state import HRState
from tools.payroll_processor import process_payroll_batch

class PayrollAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Payroll_Agent_v1",
            role="Payroll & Benefits Admin",
            goal="Accurately process compensation, bonuses, and manage benefits packages.",
            backstory="Meticulous financial admin with zero tolerance for errors in employee compensation."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        if "payroll" in state.natural_language_query.lower() or state.target_action == "payroll":
            self.report(state, "PROCESS_PAYROLL", "Initiating payroll processing for the current cycle.")
            # Trigger HITL
            state.requires_human_approval = True
            state.approval_reason = "Executing company-wide payroll processing."
            
            # Simulated return if approval is granted in a later tick
            # In a real graph, node yields to user here.
            process_payroll_batch(["EMP1", "EMP2"], "March 2026")
            return {"status": "processed"}
        return {"status": "skipped"}
