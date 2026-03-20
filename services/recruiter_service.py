from ai.jd_matcher import match_candidate_with_jd

def rank_candidates(jd_skills, students):
    ranked = []

    for student in students:
        result = match_candidate_with_jd(jd_skills, student["skills"])
        ranked.append((student, result["match_score"]))

    return sorted(ranked, key=lambda x: x[1], reverse=True)
