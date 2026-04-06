def generate_offer_letter(candidate_id: str, details: dict) -> str:
    """Mock PDF Template Generation"""
    print(f"[DOC GEN] Creating Offer Letter PDF for {candidate_id}")
    return f"offer_{candidate_id}.pdf"

def send_for_esignature(document_path: str, email: str) -> str:
    """Mock DocuSign/HelloSign Integration"""
    print(f"[E-SIGN] Sent {document_path} to {email} for signing.")
    return "ENV-1002931X"
