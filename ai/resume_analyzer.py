from ai.groq_client import generate_response

def analyze_resume(resume_text):
    prompt = f"""
    Analyze resume and extract:
    - Skills
    - Experience level
    - Missing skills

    Resume:
    {resume_text}
    """

    return generate_response(prompt)
