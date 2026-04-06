from .base import AgentBase
from core.state import HRState
from knowledge.vector_store import knowledge_store

class SupportAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Support_Agent_v1",
            role="24/7 Employee Support Concierge",
            goal="Answer day-to-day HR queries (PTO balance, policy questions).",
            backstory="A friendly, infinitely patient assistant that knows the handbook inside out and resolves tickets instantly."
        )

    def execute(self, state: HRState, input_data: dict) -> dict:
        self.report(state, "QUERY_RECEIVED", f"Processing: {state.natural_language_query}")
        # Always run as a default handler if others skip
        answers = knowledge_store.search(state.natural_language_query, top_k=1)
        if answers:
            response = {"status": "answered", "answer": answers[0]["content"], "source": answers[0]["source"]}
            self.report(state, "SUPPORT_REPLY", f"Answered from {answers[0]['source']}", sources=[answers[0]["source"]])
            return response
        return {"status": "unknown"}
