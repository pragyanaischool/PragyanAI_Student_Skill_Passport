import streamlit as st
from ui.student_dashboard import show_student_dashboard
from ui.recruiter_dashboard import show_recruiter_dashboard

st.set_page_config(page_title="PragyanAI Skill Passport")

menu = st.sidebar.selectbox(
    "Select Role",
    ["Student", "Recruiter"]
)

if menu == "Student":
    show_student_dashboard()

elif menu == "Recruiter":
    show_recruiter_dashboard()
