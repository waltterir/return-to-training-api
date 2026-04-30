def long_break_rule(days_since_last_workout: int) -> dict | None:
    if days_since_last_workout >= 7:
        return {
            "rule": "long_break_rule",
            "reason": f"More than 7 days since last workout ({days_since_last_workout} days)"
        }
    return None

    