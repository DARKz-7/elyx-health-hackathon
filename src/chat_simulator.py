from datetime import datetime
from models import Member, TeamMember
from scenario_simulator import (
    simulate_conversations_static,
    simulate_conversations_dynamic,
    create_personalized_plan,
    create_interventions,
    create_metrics,
    create_diagnostic_tests
)
from model_validation_demo import (
    validate_member,
    validate_team,
    validate_conversation,
    validate_diagnostic_tests,
    validate_plans,
    validate_interventions,
    validate_metrics
)
from data_io import save_to_csv, save_to_json


def create_team():
    return [
        TeamMember(id=201, name="Dr. Warren", role="Medical Strategist"),
        TeamMember(id=202, name="Ruby", role="Concierge"),
        TeamMember(id=203, name="Advik", role="Performance Scientist"),
        TeamMember(id=204, name="Carla", role="Nutritionist"),
        TeamMember(id=205, name="Rachel", role="PT"),
        TeamMember(id=206, name="Neel", role="Concierge Lead"),
    ]


def create_member():
    return Member(
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
            "Annual health screening"
        ],
        chronic_conditions=["POTS"],
        personal_assistant="Sarah Tan",
        support_network=["Wife", "2 kids", "Cook at home"]
    )


def main():
    start_date = datetime(2025, 1, 15, 9, 0)

    team = create_team()
    member = create_member()
    diagnostic_tests = create_diagnostic_tests(member)
    plan = create_personalized_plan(member, start_date)
    interventions = create_interventions(member, start_date)
    metrics = create_metrics(member, start_date, num_weeks=32)

    conversations = simulate_conversations_static(member, team, start_date)
    conversations += simulate_conversations_dynamic(member, team, start_date, [plan], interventions, metrics)
    conversations.sort(key=lambda c: c.timestamp)

    validate_member(member)
    validate_team(team)
    validate_conversation(conversations)
    validate_diagnostic_tests(diagnostic_tests)
    validate_plans([plan])
    validate_interventions(interventions)
    validate_metrics(metrics)

    save_to_csv('conversations.csv', conversations,
                ['id', 'timestamp', 'sender', 'sender_role', 'recipient', 'message',
                 'message_type', 'related_event', 'attachments'])
    save_to_json('conversations.json', conversations)

    save_to_csv('diagnostics.csv', diagnostic_tests,
                ['id', 'member_id', 'test_type', 'test_date', 'results', 'ordered_by', 'summary'])
    save_to_json('diagnostics.json', diagnostic_tests)

    save_to_csv('plans.csv', [plan],
                ['id', 'member_id', 'created_by', 'created_at', 'summary', 'interventions', 'version'])
    save_to_json('plans.json', [plan])

    save_to_csv('interventions.csv', interventions,
                ['id', 'member_id', 'created_by', 'type', 'start_date', 'end_date', 'details',
                 'status', 'rationale', 'linked_conversation_id'])
    save_to_json('interventions.json', interventions)

    save_to_csv('metrics.csv', metrics,
                ['id', 'member_id', 'metric_type', 'value', 'date', 'source'])
    save_to_json('metrics.json', metrics)

    for conv in conversations:
        print(f"[{conv.timestamp.strftime('%Y-%m-%d %H:%M')}] {conv.sender} ({conv.sender_role}): {conv.message}")


if __name__ == "__main__":
    main()
