from ai.skill_extractor import extract_skills_from_project

def process_student_project(project_text):
    skills = extract_skills_from_project(project_text)

    return {
        "skills": skills
    }
