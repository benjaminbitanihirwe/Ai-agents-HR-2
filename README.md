# HR Swarm – 10-Agent OpenClaw Production System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-1.5.0+-green.svg)](https://github.com/openclaw)

Enterprise-grade HR automation swarm that processes natural language requests using a supervisor‑orchestrated multi‑agent system. Built with OpenClaw, FAISS, and Pydantic.

## Features

- **10 specialized agents** coordinated by a `SupervisorGraph`
- **Natural language understanding** of HR queries (policies, payroll, hiring, etc.)
- **Human‑in‑the‑loop (HITL)** for sensitive actions (e.g., payroll approval)
- **Per‑request audit logging** – JSON export with full trace
- **Multi‑tenant ready** – each request carries a `tenant_id`
- **Vector search** (FAISS) for policy retrieval

## Architecture

The system uses a directed graph where a supervisor agent routes the incoming query to the appropriate worker agents. Example agents include:

- Intent Classifier  
- Policy Retriever (FAISS‑based)  
- Payroll Processor  
- Hiring Coordinator  
- Human‑in‑the‑Loop Gateway  
- Audit Logger  

Each agent is stateless; state is carried in the `HRState` object through the graph.

## Installation

```bash
git clone https://github.com/your-org/hr-swarm.git
cd hr-swarm
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
