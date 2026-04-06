def schedule_interview(candidate_email: str, panel_emails: list, time_slot: str) -> str:
    """Mock API to schedule across GSuite/Outlook"""
    print(f"[CALENDAR API] Scheduled interview on {time_slot} for {candidate_email} with {panel_emails}")
    return "MEET-9921"

def schedule_review(employee_id: str, manager_id: str, date: str) -> str:
    print(f"[CALENDAR API] Scheduled Perf Review for {employee_id} on {date}")
    return "MEET-8822"
