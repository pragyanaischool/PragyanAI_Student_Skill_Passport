def match_candidate_with_jd(jd_skills, student_skills):
    matched = set(jd_skills).intersection(set(student_skills))
    score = len(matched) / len(jd_skills)

    return {
        "match_score": round(score * 100, 2),
        "matched_skills": list(matched)
    }
