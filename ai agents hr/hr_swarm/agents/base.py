from pydantic import BaseModel, Field
from typing import List, Callable, Any
from core.state import HRState

class AgentBase(BaseModel):
    """
    Base openclaw Agent encapsulation handling definitions, backstory, 
    and task execution wrapping with audit logging.
    """
    name: str
    role: str
    goal: str
    backstory: str
    tools: List[Callable] = Field(default_factory=list)
    
    def execute(self, state: HRState, input_data: Any) -> Any:
        """
        Executes the agent's logic on the input_data.
        To be implemented by subclasses.
        """
        raise NotImplementedError("Each agent must implement its own execution logic.")
    
    def _reason(self, state: HRState, prompt: str) -> str:
        """
        Mock of LLM reasoning step matching openclaw's ReAct pattern.
        """
        # In a real openclaw implementation, we would call:
        # response = openclaw.llm.invoke(prompt, tools=self.tools)
        return f"{self.name} considered: {prompt}"

    def report(self, state: HRState, action: str, details: str, sources: List[str] = None):
        """Standardized reporting mechanism connected to Audit Logs"""
        state.log_action(self.name, action, details, sources)
        print(f"🤖 [{self.name}]: {action} - {details}")
