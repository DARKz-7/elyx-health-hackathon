from datetime import datetime
from models import Member, TeamMember
from data_io import save_to_csv, save_to_json
from scenario_simulator import simulate_conversations, simulate_advanced_conversations
from model_validation_demo import validate_member, validate_team, validate_conversation
from models import DiagnosticTest
from datetime import datetime
from model_validation_demo import validate_member, validate_team, validate_conversation, validate_diagnostic_tests

def main():
    team = create_team()
    member = create_member()
    start_date = datetime(2025, 1, 15, 9, 0)

    conversations = simulate_conversations(member, team, start_date)
    conversations += simulate_advanced_conversations(member, team, start_date)
    conversations.sort(key=lambda c: c.timestamp)

    diagnostic_tests = create_diagnostic_tests(member)

    # Run validations
    validate_member(member)
    validate_team(team)
    validate_conversation(conversations)
    validate_diagnostic_tests(diagnostic_tests)

    # Save/export as CSV and JSON
    save_to_csv('data/diagnostics.csv', diagnostic_tests,
                ['id', 'member_id', 'test_type', 'test_date', 'results', 'ordered_by', 'summary'])
    save_to_json('data/diagnostics.json', diagnostic_tests)

def create_diagnostic_tests(member):
    # Example diagnostic test data for your hackathon simulation
    return [
        DiagnosticTest(
            id=101,
            member_id=member.id,
            test_type="Full Blood Panel",
            test_date=datetime(2025, 4, 15, 9, 0),
            results={"ApoB": 105, "hs-CRP": 2.7, "Glucose": 90},
            ordered_by=201,  # Dr. Warren
            summary="ApoB slightly elevated; CRP mild inflammation; glucose normal."
        ),
        DiagnosticTest(
            id=102,
            member_id=member.id,
            test_type="Lipid Profile",
            test_date=datetime(2025, 7, 15, 9, 0),
            results={"LDL": 135, "HDL": 45, "Triglycerides": 140},
            ordered_by=201,
            summary="LDL moderately high, HDL low-normal, Triglycerides normal."
        )
    ]

def main():
    team = create_team()
    member = create_member()
    start_date = datetime(2025, 1, 15, 9, 0)

    conversations = simulate_conversations(member, team, start_date)
    conversations += simulate_advanced_conversations(member, team, start_date)
    conversations.sort(key=lambda c: c.timestamp)

    # Run validations before proceeding
    validate_member(member)
    validate_team(team)
    validate_conversation(conversations)

    # If validation passes, save and print
    save_to_csv('data/conversations.csv', conversations,
                ['id', 'timestamp', 'sender', 'sender_role', 'recipient', 'message', 'message_type', 'related_event', 'attachments'])
    save_to_json('data/conversations.json', conversations)

    for conv in conversations:
        print(f"[{conv.timestamp.strftime('%Y-%m-%d %H:%M')}] {conv.sender} ({conv.sender_role}): {conv.message}")


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
    team = create_team()
    member = create_member()
    start_date = datetime(2025, 1, 15, 9, 0)

    conversations = simulate_conversations(member, team, start_date)
    conversations += simulate_advanced_conversations(member, team, start_date)
    conversations.sort(key=lambda c: c.timestamp)

    save_to_csv('data/conversations.csv', conversations,
                ['id', 'timestamp', 'sender', 'sender_role', 'recipient', 'message', 'message_type', 'related_event', 'attachments'])
    save_to_json('data/conversations.json', conversations)

    for conv in conversations:
        print(f"[{conv.timestamp.strftime('%Y-%m-%d %H:%M')}] {conv.sender} ({conv.sender_role}): {conv.message}")

if __name__ == "__main__":
    main()

from data_io import save_to_json

save_to_json('data/conversations.json', conversations)
print("Exported latest conversations to data/conversations.json!")
