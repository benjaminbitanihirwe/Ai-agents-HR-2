from .base import AgentBase
from core.state import HRState
from tools.hris_api import create_job_requisition
from tools.communications import send_email

class RecruiterAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Recruiter_Agent_v1",
            role="Technical Sourcer & Recruiter",
            goal="Identify, screen, and manage the hiring pipeline for new roles.",
            backstory="A seasoned talent acquisition specialist capable of analyzing job reqs, sourcing candidates, and handling interview logistics.",
            tools=[create_job_requisition, send_email]
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        self.report(state, "EVALUATE_REQ", "Analyzing request to hire...")
        # Human in the loop would occur at supervisor level or here before extending an offer
        if "hire" in state.natural_language_query.lower():
            req_id = create_job_requisition("Engineering", "Senior Engineer", "Python, Agents")
            self.report(state, "CREATED_REQ", f"Created Req: {req_id}")
            state.candidate_id = "CAND-991"
            return {"status": "success", "action": "REQ_CREATED", "candidate_id": state.candidate_id}
        
        return {"status": "skipped", "reason": "No hiring intent detected"}
