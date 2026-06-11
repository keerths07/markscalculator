import streamlit as st

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Management System")

st.write("""
Welcome to the Student Management System.

Use the sidebar to navigate:
- Home
- Add Student
- Enter Marks
- View Results
""")