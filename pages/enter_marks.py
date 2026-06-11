import streamlit as st
import pandas as pd
import os

st.title("📝 Enter Marks")

student_id = st.text_input("Student ID")

maths = st.number_input(
    "Maths Marks",
    min_value=0,
    max_value=100
)

science = st.number_input(
    "Science Marks",
    min_value=0,
    max_value=100
)

english = st.number_input(
    "English Marks",
    min_value=0,
    max_value=100
)

if st.button("Save Marks"):

    total = maths + science + english
    percentage = total / 3

    marks_data = pd.DataFrame({
        "Student ID": [student_id],
        "Maths": [maths],
        "Science": [science],
        "English": [english],
        "Total": [total],
        "Percentage": [percentage]
    })

    if os.path.exists("marks.csv"):
        old_data = pd.read_csv("marks.csv")
        updated_data = pd.concat(
            [old_data, marks_data],
            ignore_index=True
        )
    else:
        updated_data = marks_data

    updated_data.to_csv(
        "marks.csv",
        index=False
    )

    st.success("Marks Saved Successfully!")