import streamlit as st
from services.recruiter_service import rank_candidates

def show_recruiter_dashboard():
    st.title("🏢 Recruiter Dashboard")

    jd = st.text_area("Paste Job Description")

    if st.button("Find Candidates"):
        # Dummy data
        students = [
            {"name": "S1", "skills": ["Python", "NLP"]},
            {"name": "S2", "skills": ["Java", "React"]}
        ]

        jd_skills = ["Python", "NLP"]

        ranked = rank_candidates(jd_skills, students)

        for student, score in ranked:
            st.write(f"{student['name']} → {score}% match")
