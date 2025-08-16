from models import Member, TeamMember, Conversation
from models import validate_member, validate_team, validate_conversation
from datetime import datetime

def validate_diagnostic_tests(tests):
    for test in tests:
        assert test.test_type, f"DiagnosticTest ID {test.id} missing test_type"
        assert test.test_date, f"DiagnosticTest ID {test.id} missing test_date"
        assert isinstance(test.results, dict), f"DiagnosticTest ID {test.id} results must be dict"
    print("All diagnostic tests validated successfully.")

def validate_plans(plans):
    for plan in plans:
        assert plan.summary, f"Plan ID {plan.id} missing summary"
        assert isinstance(plan.interventions, list), f"Plan ID {plan.id} interventions must be list"
    print("All plans validated successfully.")

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
