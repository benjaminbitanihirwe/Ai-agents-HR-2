# Ai-agents-HR-2
OpenClaw-based 10-agent HR system: processes natural language requests (policy, payroll, hiring) via SupAervisorGraph, uses HRState with audit log exportThe entry point (main.py) initializes an HRState with tenant ID, request ID, and a user query, then runs a SupervisorGraph that orchestrates specialized agents
