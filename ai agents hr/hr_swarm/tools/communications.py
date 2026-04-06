def send_email(to_address: str, subject: str, body: str) -> bool:
    """Mock tool to send an email"""
    print(f"\n[EMAIL SENT] To: {to_address} | Subject: {subject}")
    print(f"Body:\n{body}\n")
    return True

def send_slack_message(channel: str, message: str) -> bool:
    """Mock tool to post to Slack"""
    print(f"[SLACK MESSAGE] #{channel}: {message}")
    return True
