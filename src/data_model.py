from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import datetime

# ---- Team Member (the expert staff) ----
@dataclass
class TeamMember:
    id: int
    name: str
    role: str                # e.g., Doctor, PT, Nutritionist
    description: Optional[str] = None

# ---- Member (the user/client) ----
@dataclass
class Member:
    id: int
    name: str
    dob: str                 # Date of birth, e.g., "1979-03-12"
    age: int
    gender: str
    residence: str
    travel_hubs: List[str]
    occupation: str
    health_goals: List[str]
    chronic_conditions: List[str]
    personal_assistant: Optional[str] = None
    support_network: Optional[List[str]] = field(default_factory=list)

# ---- Conversation (WhatsApp-style message) ----
@dataclass
class Conversation:
    id: int
    timestamp: datetime
    sender: str              # "Rohan Patel" or Elyx team member name
    sender_role: str         # "Member", "PT", "Doctor", etc.
    recipient: str
    message: str
    message_type: str        # "query", "plan_update", "report", "reminder", etc.
    related_intervention_id: Optional[int] = None
    attachments: Optional[List[str]] = field(default_factory=list)  # e.g., ["blood_panel.pdf"]

# ---- Plan (Overall journey plan - versioned) ----
@dataclass
class Plan:
    id: int
    member_id: int
    created_by: int          # TeamMember id
    created_at: datetime
    summary: str
    interventions: List[int] = field(default_factory=list)  # List of Intervention ids
    version: str = "v1.0"

# ---- Intervention (action, therapy, exercise, supplement, etc.) ----
@dataclass
class Intervention:
    id: int
    member_id: int
    created_by: int           # TeamMember id
    type: str                 # "exercise", "medication", "nutrition", etc.
    start_date: datetime
    end_date: Optional[datetime]
    details: str
    status: str               # "active", "completed", "changed"
    rationale: str            # Why this was started/changed
    linked_conversation_id: Optional[int] = None

# ---- DiagnosticTest (lab, scan, assessment) ----
@dataclass
class DiagnosticTest:
    id: int
    member_id: int
    test_type: str            # e.g., "Full Blood Panel", "MRI"
    test_date: datetime
    results: Dict[str, float] # e.g., {"ApoB": 105, "hs-CRP": 2.7}
    ordered_by: int           # TeamMember id
    summary: str              # Key findings and recommendations

# ---- Metric (measurement tracked over time) ----
@dataclass
class Metric:
    id: int
    member_id: int
    metric_type: str          # e.g., "HRV", "Sleep Score", "ApoB"
    value: float
    date: datetime
    source: str               # e.g., "Whoop", "Blood Test", "Manual Entry"

# ---- Example: Creating sample instances ----

if __name__ == "__main__":
    # Example team member
    doc = TeamMember(id=201, name="Dr. Warren", role="Medical Strategist")

    # Example member
    rohan = Member(
        id=1,
        name="Rohan Patel",
        dob="1979-03-12",
        age=46,
        gender="Male",
        residence="Singapore",
        travel_hubs=["UK", "US", "South Korea", "Jakarta"],
        occupation="Regional Head of Sales",
        health_goals=[
            "Reduce risk of heart disease",
            "Enhance cognitive function",
            "Annual health screening"],
        chronic_conditions=["POTS"],
        personal_assistant="Sarah Tan"
    )

    # Example diagnostic test
    blood_test = DiagnosticTest(
        id=101,
        member_id=1,
        test_type="Full Blood Panel",
        test_date=datetime(2025, 3, 28),
        results={"ApoB": 105, "hs-CRP": 2.7, "Glucose": 90},
        ordered_by=201,
        summary="ApoB slightly elevated; CRP mild inflammation; glucose normal."
    )

    print(rohan)
    print(doc)
    print(blood_test)
