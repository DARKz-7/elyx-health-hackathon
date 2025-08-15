import random
from datetime import timedelta

from models import Conversation

def advance_days(base_date, days):
    return base_date + timedelta(days=days)

def simulate_conversations(member, team, start_date):
    conv_id = 1
    conversations = []

    conversations.append(Conversation(
        id=conv_id,
        timestamp=start_date,
        sender=member.name,
        sender_role="Member",
        recipient="Ruby",
        message="Hi Ruby. My Garmin is logging high intensity minutes even on rest days. Need a medical review.",
        message_type="query"
    ))
    conv_id += 1

    conversations.append(Conversation(
        id=conv_id,
        timestamp=advance_days(start_date, 0.01),
        sender="Ruby",
        sender_role="Concierge",
        recipient=member.name,
        message="Thank you, Rohan. Are you experiencing other symptoms? I'll flag Dr. Warren.",
        message_type="update"
    ))
    conv_id += 1

    conversations.append(Conversation(
        id=conv_id,
        timestamp=advance_days(start_date, 1),
        sender="Dr. Warren",
        sender_role="Medical Strategist",
        recipient=member.name,
        message="Submission reviewed. Strongly suggests autonomic dysfunction. We'll need medical records.",
        message_type="report"
    ))
    conv_id += 1

    for month_week in range(2*4):
        conv_id += 1
        recipient = random.choice([t.name for t in team if t.name != member.name])
        conversations.append(Conversation(
            id=conv_id,
            timestamp=advance_days(start_date, 2 + month_week*2),
            sender=member.name,
            sender_role="Member",
            recipient=recipient,
            message=f"Week {(month_week//4)+1}, Query {(month_week%4)+1}: Read about Omega-3. Should I supplement?",
            message_type="query"
        ))

    conv_id += 1
    conversations.append(Conversation(
        id=conv_id,
        timestamp=advance_days(start_date, 90),
        sender="Ruby",
        sender_role="Concierge",
        recipient=member.name,
        message="Reminder: Time for your full diagnostic panel this week.",
        message_type="reminder"
    ))

    return conversations

def simulate_advanced_conversations(member, team, start_date):
    conv_id = 100
    conversations = []

    for weeks in range(0, 8, 2):
        conv_id += 1
        conversations.append(Conversation(
            id=conv_id,
            timestamp=advance_days(start_date, weeks * 7),
            sender="Rachel",
            sender_role="PT",
            recipient=member.name,
            message=f"Time for your exercise program update for week {weeks+1}. We'll adapt based on your progress.",
            message_type="plan_update"
        ))
        conv_id += 1
        conversations.append(Conversation(
            id=conv_id,
            timestamp=advance_days(start_date, weeks * 7 + 1),
            sender=member.name,
            sender_role="Member",
            recipient="Rachel",
            message="Travelling to US next week. Can you send hotel-friendly exercise suggestions?",
            message_type="query"
        ))
        conv_id += 1
        conversations.append(Conversation(
            id=conv_id,
            timestamp=advance_days(start_date, weeks * 7 + 2),
            sender="Rachel",
            sender_role="PT",
            recipient=member.name,
            message="Here is a hotel gym circuit for your travel week. Let me know if any equipment is missing.",
            message_type="plan_update"
        ))

    conv_id += 1
    conversations.append(Conversation(
        id=conv_id,
        timestamp=advance_days(start_date, 17),
        sender=member.name,
        sender_role="Member",
        recipient="Ruby",
        message="I'm getting frustrated at the slow pace of changes. Can I see a consolidated plan update?",
        message_type="feedback"
    ))
    conv_id += 1
    conversations.append(Conversation(
        id=conv_id,
        timestamp=advance_days(start_date, 18),
        sender="Neel",
        sender_role="Concierge Lead",
        recipient=member.name,
        message="Thank you for your feedback, Rohan. We will compile a priority and rationale summary ASAP.",
        message_type="update"
    ))
    return conversations
