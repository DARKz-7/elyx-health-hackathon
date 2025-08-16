from models import Member, TeamMember, Conversation
from datetime import datetime

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

def validate_diagnostic_tests(tests):
    for test in tests:
        assert test.test_type, f"Diagnostic test {test.id} type cannot be empty"
        assert test.test_date, f"Diagnostic test {test.id} date missing"
        assert isinstance(test.results, dict), f"Diagnostic test {test.id} results must be a dictionary"
        assert test.summary, f"Diagnostic test {test.id} summary missing"
    print("All diagnostic tests validated successfully.")

def validate_plans(plans):
    for plan in plans:
        assert plan.summary, f"Plan ID {plan.id} missing summary"
        assert isinstance(plan.interventions, list), f"Plan ID {plan.id} interventions must be list"
    print("All plans validated successfully.")

# Example data below for testing validations
member = Member(
    id=1,
    name="Rohan Patel",
    dob="1979-03-12",
    age=46,
    gender="Male",
    residence="Singapore",
    travel_hubs=["UK", "US", "Jakarta"],
    occupation="Regional Head of Sales",
    health_goals=["Reduce risk of heart disease"],
    chronic_conditions=["POTS"],
    personal_assistant="Sarah Tan",
    support_network=["Wife", "2 kids"]
)

team = [
    TeamMember(id=201, name="Dr. Warren", role="Medical Strategist"),
    TeamMember(id=202, name="Ruby", role="Concierge")
]

conv = [
    Conversation(
        id=1,
        timestamp=datetime.now(),
        sender=member.name,
        sender_role="Member",
        recipient="Ruby",
        message="Hi Ruby!",
        message_type="query"
    )
]

# Run validations
validate_member(member)
validate_team(team)
validate_conversation(conv)
