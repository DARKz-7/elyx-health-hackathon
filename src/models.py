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
