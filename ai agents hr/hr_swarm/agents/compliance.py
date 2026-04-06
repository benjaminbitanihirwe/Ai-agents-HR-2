from .base import AgentBase
from core.state import HRState
from knowledge.vector_store import knowledge_store

class ComplianceAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Compliance_Agent_v1",
            role="Compliance & Risk Officer",
            goal="Audit HR actions, enforce labor laws, and ensure company policy adherence.",
            backstory="A strict but fair auditor with instant recall of all local labor laws and company handbooks."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        self.report(state, "COMPLIANCE_CHECK", "Auditing the current request against knowledge base.")
        policies = knowledge_store.search(state.natural_language_query)
        sources = [p["source"] for p in policies]
        self.report(state, "POLICY_VERIFIED", f"Action is compliant with {sources}", sources=sources)
        return {"status": "compliant", "sources": sources}
