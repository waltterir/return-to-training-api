def long_brake_rule(days_since_last_workout: int) -> dict | None:
    if days_since_last_workout >= 7:
        return {
            "rule": "long_brake_rule",
            "reason": f"More than 7 days since last workout ({days_since_last_workout} days)"
        }
    return None