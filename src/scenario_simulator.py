import random
from datetime import timedelta
from models import Conversation

def advance_days(base_date, days):
    return base_date + timedelta(days=days)

def simulate_conversations_static(member, team, start_date):
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

    # Generate repeated member queries every two weeks for 8 weeks (approx. 2 months)
    for month_week in range(2 * 4):
        conv_id += 1
        recipient = random.choice([tm.name for tm in team if tm.name != member.name])
        conversations.append(Conversation(
            id=conv_id,
            timestamp=advance_days(start_date, 2 + month_week * 14),
            sender=member.name,
            sender_role="Member",
            recipient=recipient,
            message=f"Week {(month_week // 4) + 1}, Query {(month_week % 4) + 1}: Read about Omega-3. Should I supplement?",
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

def simulate_conversations_dynamic(member, team, start_date, plans, interventions, metrics):
    conversations = []
    conv_id = 1000  # Starting at 1000 to avoid ID conflicts

    # Initial greeting
    conversations.append(Conversation(
        id=conv_id,
        timestamp=start_date,
        sender=member.name,
        sender_role="Member",
        recipient="Ruby",
        message="Hi Ruby!",
        message_type="query"
    ))
    conv_id += 1

    num_weeks = 32  # approx 8 months

    for week in range(num_weeks):
        current_date = start_date + timedelta(weeks=week)

        # Weekly check-in message from PT every 2 weeks
        if week % 2 == 0:
            conversations.append(Conversation(
                id=conv_id,
                timestamp=current_date,
                sender="Rachel",
                sender_role="PT",
                recipient=member.name,
                message=f"Time for your exercise program update for week {week+1}. We'll adapt based on your progress.",
                message_type="plan_update"
            ))
            conv_id += 1

            conversations.append(Conversation(
                id=conv_id,
                timestamp=current_date + timedelta(days=1),
                sender=member.name,
                sender_role="Member",
                recipient="Rachel",
                message="Travelling to US next week. Can you send hotel-friendly exercise suggestions?",
                message_type="query"
            ))
            conv_id += 1

            conversations.append(Conversation(
                id=conv_id,
                timestamp=current_date + timedelta(days=2),
                sender="Rachel",
                sender_role="PT",
                recipient=member.name,
                message="Here is a hotel gym circuit for your travel week. Let me know if any equipment is missing.",
                message_type="plan_update"
            ))
            conv_id += 1

        # Monitor exercise metric and respond if below threshold
        week_metric = next((m for m in metrics if m.date.isocalendar()[1] == current_date.isocalendar()[1]
                           and m.metric_type == "ExerciseMinutes"), None)
        if week_metric and week_metric.value < 120:
            # Add a plan update message indicating adjustment
            conversations.append(Conversation(
                id=conv_id,
                timestamp=current_date + timedelta(hours=10),
                sender="Rachel",
                sender_role="PT",
                recipient=member.name,
                message="We noticed your exercise log dropped. Adjusting your plan for a better
