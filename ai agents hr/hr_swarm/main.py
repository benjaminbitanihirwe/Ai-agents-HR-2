import uuid
from core.state import HRState
from supervisor.graph import SupervisorGraph

def handle_request(query: str):
    print("\n" + "="*60)
    print(f"📥 Received HR Request: {query}")
    print("="*60)
    
    # Initialize Context
    state = HRState(
        tenant_id="ACME_CORP",
        request_id=str(uuid.uuid4())[:8],
        natural_language_query=query
    )
    
    # Initialize Graph
    swarm = SupervisorGraph()
    
    # Execute Graph
    final_state = swarm.run(state)
    
    print("\n" + "="*60)
    print("✅ Execution Complete. Exporting Audit Log...")
    final_state.export_audit_log(f"audit_{final_state.request_id}.json")
    print(f"📄 Audit Log saved: audit_{final_state.request_id}.json")
    print("="*60)

if __name__ == "__main__":
    banner = """
    ╔════════════════════════════════════════╗
    ║       HR SWARM - OPENCLAW AGENTS       ║
    ║   10-Agent Production System (2026)    ║
    ╚════════════════════════════════════════╝
    """
    print(banner)
    
    # Example 1: Day-to-day query
    handle_request("What is our remote work policy?")
    
    # Example 2: Sensitive action requiring HITL
    handle_request("Process payroll for the engineering team for March.")
    
    # Example 3: Multi-agent pipeline
    handle_request("We need to hire a new Senior Engineer in New York.")
