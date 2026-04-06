import json
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, Dict, List, Optional
import os

class TaskMetrics(BaseModel):
    model_config = ConfigDict(extra='allow')
    start_time: datetime = datetime.now()
    end_time: Optional[datetime] = None
    status: str = "pending"

class HRState(BaseModel):
    """
    Shared Context / State for the HR Swarm.
    Maintains graph variables, active employee data, request context, and approvals.
    """
    tenant_id: str
    request_id: str
    natural_language_query: str
    
    # Context data extracted by Supervisor/Agents
    employee_id: Optional[str] = None
    candidate_id: Optional[str] = None
    target_action: Optional[str] = None # e.g. 'hire', 'onboard', 'payroll', 'terminate'
    
    # Approvals for human-in-the-loop
    requires_human_approval: bool = False
    human_approval_granted: Optional[bool] = None
    approval_reason: Optional[str] = None
    
    # Audit trail
    history: List[Dict[str, Any]] = []
    
    # Key-value store for intermediate agent outputs
    agent_outputs: Dict[str, Any] = {}

    def log_action(self, agent_name: str, action: str, details: Any, sources: List[str] = None):
        """Append to the execution history for audit transparency"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "action": action,
            "details": details,
            "sources_cited": sources or []
        }
        self.history.append(log_entry)
        
    def export_audit_log(self, filepath: str = "audit_log.json"):
        """Export the exact history of reasoning, actions, and sources"""
        with open(filepath, "w") as f:
            json.dump(self.history, f, indent=4)
