from core.state import HRState
from agents import (
    RecruiterAgent, OnboardingAgent, PayrollAgent, PerformanceAgent, 
    CultureAgent, ComplianceAgent, LearningAgent, OffboardingAgent, 
    AnalyticsAgent, SupportAgent
)
from tools.compliance_checker import require_human_approval

class HumanInTheLoopInterrupt(Exception):
    pass

class SupervisorGraph:
    """
    Supervisor / Orchestrator Agent.
    Manages the graph routing between the 10 specialized agents using openclaw-style execution.
    """
    def __init__(self):
        self.agents = {
            "recruiter": RecruiterAgent(),
            "onboarding": OnboardingAgent(),
            "payroll": PayrollAgent(),
            "performance": PerformanceAgent(),
            "culture": CultureAgent(),
            "compliance": ComplianceAgent(),
            "learning": LearningAgent(),
            "offboarding": OffboardingAgent(),
            "analytics": AnalyticsAgent(),
            "support": SupportAgent()
        }

    def determine_route(self, state: HRState) -> list:
        """
        Orchestration logic: determine which agents need to process this request.
        A real implementation would use an LLM router here. For this script, we map keywords.
        """
        query = state.natural_language_query.lower()
        route = []
        
        # All actions go through compliance first if they look like state changes
        if any(w in query for w in ["hire", "terminate", "payroll", "promote"]):
            route.append("compliance")

        if "hire" in query or "recruit" in query:
            route.append("recruiter")
        elif "onboard" in query:
            route.append("onboarding")
        elif "payroll" in query or "pay" in query:
            route.append("payroll")
        elif "review" in query or "performance" in query:
            route.append("performance")
        elif "culture" in query or "survey" in query:
            route.append("culture")
        elif "learn" in query or "training" in query:
            route.append("learning")
        elif "terminate" in query or "offboard" in query:
            route.append("offboarding")
        elif "report" in query or "metrics" in query:
            route.append("analytics")
        else:
            route.append("support")
            
        return route

    def run(self, state: HRState):
        route = self.determine_route(state)
        state.log_action("Supervisor", "EVALUATE_ROUTE", f"Determined execution path: {route}")
        
        for agent_name in route:
            agent = self.agents[agent_name]
            print(f"\n--- Yielding to {agent.name} ---")
            
            result = agent.execute(state, {})
            state.agent_outputs[agent_name] = result
            
            # Sub-graph human approval check
            if state.requires_human_approval:
                approved = require_human_approval(agent.name, state.approval_reason)
                state.human_approval_granted = approved
                state.log_action(agent.name, "HITL_CHECK", f"Approval granted: {approved}")
                
                if not approved:
                    print(f"❌ Execution paused or aborted due to human rejection.")
                    break
                else:
                    state.requires_human_approval = False # Reset post approval
                    
        return state
