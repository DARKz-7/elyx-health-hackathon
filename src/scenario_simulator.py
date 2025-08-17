import random
from datetime import timedelta
from models import Conversation, Plan, Intervention
from datetime import timedelta
from models import Metric, DiagnosticTest
import random

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

    for month_week in range(8):  # 8 weeks, 2 weeks interval
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
    conv_id = 1000

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

    num_weeks = 32
    for week in range(num_weeks):
        current_date = start_date + timedelta(weeks=week)

        # PT messages every 2 weeks
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

        # Check if exercise is below threshold and react
        week_metric = next(
            (m for m in metrics if m.date.isocalendar()[1] == current_date.isocalendar()[1]
             and m.metric_type == "ExerciseMinutes"), None)
        if week_metric and week_metric.value < 120:
            conversations.append(Conversation(
                id=conv_id,
                timestamp=current_date + timedelta(hours=10),
                sender="Rachel",
                sender_role="PT",
                recipient=member.name,
                message="We noticed your exercise log dropped. Adjusting your plan for a better fit.",
                message_type="plan_update"
            ))
            conv_id += 1

    return conversations


def create_personalized_plan(member, start_date):
    return Plan(
        id=1,
        member_id=member.id,
        created_by=201,  # Dr. Warren
        created_at=start_date,
        summary="Reduce cardiovascular risk with tailored exercise and nutrition.",
        interventions=[101, 102],
        version="v1.0"
    )


def create_interventions(member, start_date):
    return [
        Intervention(
            id=101,
            member_id=member.id,
            created_by=205,  # Rachel (PT)
            type="Exercise",
            start_date=start_date,
            end_date=None,
            details="Start brisk walks 5x/week, 30 min each.",
            status="active",
            rationale="Increase physical activity for heart health.",
            linked_conversation_id=None
        ),
        Intervention(
            id=102,
            member_id=member.id,
            created_by=204,  # Carla (Nutritionist)
            type="Nutrition",
            start_date=start_date,
            end_date=None,
            details="Lower sodium intake; add Omega-3 rich fish 2x/week.",
            status="active",
            rationale="Reduce salt, increase healthy fats.",
            linked_conversation_id=None
        )
    ]


def create_metrics(member, start_date, num_weeks=32):
    """
    Create sample weekly metrics for the member.
    Example metrics: ExerciseMinutes, SymptomFatigueScore
    """
    metrics = []
    metric_id = 1

    for week in range(num_weeks):
        date = start_date + timedelta(weeks=week)

        # Exercise minutes: simulate between 60 to 180 minutes per week with some variation
        exercise_minutes = random.randint(60, 180)

        metrics.append(Metric(
            id=metric_id,
            member_id=member.id,
            metric_type="ExerciseMinutes",
            value=exercise_minutes,
            date=date,
            source="WearableDevice"
        ))
        metric_id += 1

        # Fatigue symptom score: 0-10 scale, randomly varying
        fatigue_score = random.uniform(2.0, 6.0)

        metrics.append(Metric(
            id=metric_id,
            member_id=member.id,
            metric_type="SymptomFatigueScore",
            value=round(fatigue_score, 1),
            date=date,
            source="SelfReport"
        ))
        metric_id += 1

    return metrics


from datetime import datetime

def create_diagnostic_tests(member):
    dob_date = datetime.strptime(member.dob, "%Y-%m-%d")

    tests = []

    tests.append(DiagnosticTest(
        id=1,
        member_id=member.id,
        test_type="Lipid Panel",
        test_date=dob_date,   # use datetime object here
        results={
            "LDL": 130.0,
            "HDL": 45.0,
            "Triglycerides": 150.0,
            "TotalCholesterol": 210.0
        },
        ordered_by=201,
        summary="Borderline high LDL and triglycerides, recommend lifestyle changes."
    ))

    tests.append(DiagnosticTest(
        id=2,
        member_id=member.id,
        test_type="Blood Pressure",
        test_date=dob_date,
        results={
            "Systolic": 135,
            "Diastolic": 85
        },
        ordered_by=201,
        summary="Elevated blood pressure, monitor regularly."
    ))

    return tests

