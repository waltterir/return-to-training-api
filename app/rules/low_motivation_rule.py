def low_motivation_rule(motivation_level: int) -> dict | None:
    if motivation_level <= 2:
        return {
            "rule": "low_motivation_rule",
            "reason": f"Motivation level is low ({motivation_level}/5)"
        }
    return None
