from typing import Dict, Any

def get_employee_data(employee_id: str) -> Dict[str, Any]:
    """Mock API to fetch employee details from HRIS (e.g., Workday/BambooHR)"""
    return {
        "employee_id": employee_id,
        "name": "Jane Doe",
        "department": "Engineering",
        "role": "Senior Engineer",
        "start_date": "2023-01-15",
        "salary_band": "L5"
    }

def update_employee_record(employee_id: str, updates: Dict[str, Any]) -> bool:
    """Mock API to update employee details"""
    print(f"[HRIS API] Updated {employee_id} record with: {updates}")
    return True

def create_job_requisition(department: str, title: str, requirements: str) -> str:
    """Mock API to create a new job opening in ATS"""
    print(f"[ATS API] Created requisition for {title} in {department}")
    return "REQ-9981"
