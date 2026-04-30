def too_much_too_soon_rule(days_since_last_workout: int, last_session_intensity: str) -> dict | None:
    if days_since_last_workout < 7 and last_session_intensity == "hard":
        return {
            "rule": "too_much_too_soon_rule",
            "reason": f"Returning after long break with previous hard session - High risk of injury"
        }
    return None