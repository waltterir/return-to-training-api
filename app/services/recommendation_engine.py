import json
from ..models.models import CheckIn
from ..rules.long_break_rule import long_break_rule
from ..rules.too_much_too_soon_rule import too_much_too_soon_rule
from ..rules.low_motivation_rule import low_motivation_rule
from ..rules.high_stress_rule import high_stress_rule

def run_rules(check_in: CheckIn) -> dict:
    triggered_rules = []
    
    rules = [
        long_break_rule(check_in.days_since_last_workout),
        low_motivation_rule(check_in.motivation_level),
        high_stress_rule(check_in.stress_level),
        too_much_too_soon_rule(check_in.days_since_last_workout, check_in.last_session_intensity)
    ]
    
    for rule in rules:
        if rule is not None:
            triggered_rules.append(rule)

    recommendation, risk_level, suggested_session, reason = determine_recommendation(triggered_rules)

    return {
        "recommendation": recommendation,
        "risk_level": risk_level,
        "suggested_session": suggested_session,
        "reason": reason,
        "triggered_rules": json.dumps(triggered_rules)
    }

def determine_recommendation(triggered_rules: list) -> tuple:
    rule_names = [r["rule"] for r in triggered_rules]

    if "too_much_too_soon_rule" in rule_names:
        return (
            "LIGHT",
            "HIGH",
            "20-40 min easy walk or gentle mobility work",
            "High risk of injury due to returning after long break with previous hard session - Start with very light activity and focus on recovery."
        )
    if "long_break_rule" in rule_names and "low_motivation_rule" in rule_names:
        return (
            "LIGHT",
            "MEDIUM",
            "20-30 min light movement or yoga",
            "Long break detected. Ease back in gradually. Low motivation may also impact recovery and performance."
        )

    if "long_break_rule" in rule_names:
        return (
            "LIGHT",
            "MEDIUM",
            "20-30 min light movement",
            "Long break detected. Ease back in gradually."
        )

    if "low_motivation_rule" in rule_names or "high_stress_rule" in rule_names:
        return (
            "LIGHT",
            "LOW",
            "20-30 min moderate training or enjoyable activity",
            "low motivation or high stress detected. Keep the session enjoyable and not too demanding to help boost motivation and reduce stress."
        )

    return (
        "MODERATE",
        "LOW",
        "30-45 min moderate training",
        "No significant risk factors detected. You can return to moderate training, but listen to your body and adjust as needed."
    )