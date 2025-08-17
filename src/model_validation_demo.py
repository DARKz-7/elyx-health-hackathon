from models import Member, TeamMember, Conversation, DiagnosticTest, Plan, Intervention, Metric
from datetime import datetime

def validate_member(member):
    assert member.name, "Member name cannot be empty."
    assert isinstance(member.health_goals, list), "Member health_goals should be a list."
    assert isinstance(member.travel_hubs, list), "Member travel_hubs should be a list."
    print(f"Member '{member.name}' validated successfully.")

def validate_team(team):
    for tm in team:
        assert tm.name, "Team member name is required."
        assert tm.role, f"Team member '{tm.name}' must have a role."
    print("All team members validated successfully.")

def validate_conversation(conversations):
    for conv in conversations:
        assert conv.message, f"Conversation ID {conv.id} must have non-empty message."
        assert conv.sender, f"Conversation ID {conv.id} has empty sender."
        assert conv.recipient, f"Conversation ID {conv.id} has empty recipient."
        assert isinstance(conv.timestamp, datetime), f"Conversation ID {conv.id} must have valid timestamp."
    print("All conversations validated successfully.")

def validate_diagnostic_tests(tests):
    for test in tests:
        assert test.test_type, f"Diagnostic test ID {test.id} type cannot be empty."
        assert isinstance(test.test_date, datetime), f"Diagnostic test ID {test.id} must have valid date."
        assert isinstance(test.results, dict), f"Diagnostic test ID {test.id} results must be a dictionary."
        assert test.summary, f"Diagnostic test ID {test.id} summary is missing."
    print("All diagnostic tests validated successfully.")

def validate_plans(plans):
    for plan in plans:
        assert plan.summary, f"Plan ID {plan.id} missing summary."
        assert isinstance(plan.interventions, list), f"Plan ID {plan.id} interventions must be a list."
    print("All plans validated successfully.")

def validate_interventions(interventions):
    for inter in interventions:
        assert inter.type, f"Intervention ID {inter.id} missing type."
        assert inter.details, f"Intervention ID {inter.id} missing details."
        assert inter.status in {"active", "changed", "completed"}, \
            f"Intervention ID {inter.id} has invalid status '{inter.status}'."
    print("All interventions validated successfully.")

def validate_metrics(metrics):
    for metric in metrics:
        assert metric.metric_type, f"Metric ID {metric.id} missing metric_type."
        assert metric.value is not None, f"Metric ID {metric.id} missing value."
        assert isinstance(metric.date, datetime), f"Metric ID {metric.id} must have valid date."
    print("All metrics validated successfully.")
