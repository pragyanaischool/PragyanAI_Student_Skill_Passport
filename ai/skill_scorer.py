def compute_skill_score(skill_data):
    # Example logic
    score = (
        0.4 * skill_data["project_weight"] +
        0.3 * skill_data["certifications"] +
        0.3 * skill_data["assessments"]
    )
    return round(score * 100, 2)
