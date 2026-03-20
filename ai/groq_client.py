import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_response(prompt, model="llama-3.3-70b-versatile"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content
