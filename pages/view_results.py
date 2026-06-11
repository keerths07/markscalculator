import streamlit as st
import pandas as pd
import os

st.title("📊 View Results")

if os.path.exists("students.csv") and os.path.exists("marks.csv"):

    students = pd.read_csv("students.csv")
    marks = pd.read_csv("marks.csv")

    results = pd.merge(
        students,
        marks,
        on="Student ID"
    )

    st.dataframe(results)

else:
    st.warning(
        "No student or marks data found."
    )