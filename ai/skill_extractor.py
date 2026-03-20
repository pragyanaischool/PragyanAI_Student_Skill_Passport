from ai.groq_client import generate_response

def extract_skills_from_project(project_text):
    prompt = f"""
    Extract skills from this project.
    Categorize into:
    - Technical
    - Tools
    - Soft Skills

    Project:
    {project_text}

    Return JSON format.
    """

    return generate_response(prompt)
