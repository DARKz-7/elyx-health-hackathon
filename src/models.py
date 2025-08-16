from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict
from datetime import datetime

@dataclass
class TeamMember:
    id: int
    name: str
    role: str

@dataclass
class Member:
    id: int
    name: str
    dob: str
    age: int
    gender: str
    residence: str
    travel_hubs: List[str]
    occupation: str
    health_goals: List[str]
    chronic_conditions: List[str]
    personal_assistant: str
    support_network: List[str]

@dataclass
class Conversation:
    id: int
    timestamp: datetime
    sender: str
    sender_role: str
    recipient: str
    message: str
    message_type: str
    related_event: Optional[Dict[str, int]] = field(default_factory=dict)
    attachments: Optional[List[str]] = field(default_factory=list)

@dataclass
class DiagnosticTest:
    id: int
    member_id: int
    test_type: str
    test_date: datetime
    results: Dict[str, float]
    ordered_by: int
    summary: str

@dataclass
class Plan:
    id: int
    member_id: int
    created_by: int
    created_at: datetime
    summary: str
    interventions: List[int]
    version: str

@dataclass
class Intervention:
    id: int
    member_id: int
    created_by: int
    type: str
    start_date: datetime
    end_date: Optional[datetime]
    details: str
    status: str
    rationale: str
    linked_conversation_id: Optional[int]

@dataclass
class Metric:
    id: int
    member_id: int
    metric_type: str
    value: float
    date: datetime
    source: str

    # --- Model Validation Utilities ---

def validate_member(member):
    assert member.name, "Name cannot be empty"
    assert isinstance(member.health_goals, list), "Health goals should be a list"
    assert isinstance(member.travel_hubs, list), "Travel hubs should be a list"
    print(f"Member {member.name} validated successfully.")

def validate_team(team):
    for tm in team:
        assert tm.role, f"Team member {tm.name} must have a role"
    print("All team members validated successfully.")

def validate_conversation(convs):
    for conv in convs:
        assert conv.message, "All conversations must have non-empty messages"
        assert conv.sender, f"Conversation ID {conv.id} has empty sender"
        assert conv.recipient, f"Conversation ID {conv.id} has empty recipient"
    print("All conversations validated successfully.")

def validate_diagnostic_test(test):
    assert test.test_type, "DiagnosticTest must have a test_type"
    assert isinstance(test.results, dict), "Results should be a dictionary"
    print(f"DiagnosticTest ID {test.id} validated.")

def validate_plan(plan):
    assert plan.summary, "Plan must have a summary"
    assert isinstance(plan.interventions, list), "Interventions must be a list"
    print(f"Plan ID {plan.id} validated.")

def validate_intervention(inter):
    assert inter.type, "Intervention must have a type"
    assert inter.status in ["active", "completed", "changed"], "Status must be active, completed, or changed"
    print(f"Intervention ID {inter.id} validated.")

