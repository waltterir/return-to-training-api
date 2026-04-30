def high_stress_rule(stress_level: int) -> dict | None:
    if stress_level >= 4:
        return {
            "rule": "high_stress_rule",
            "reason": f"Stress level is high ({stress_level}/5)"
        }
    return None