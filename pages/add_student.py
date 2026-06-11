import streamlit as st
import pandas as pd
import os

st.title("➕ Add Student")

student_id = st.text_input("Student ID")
student_name = st.text_input("Student Name")

if st.button("Add Student"):

    new_student = pd.DataFrame({
        "Student ID": [student_id],
        "Name": [student_name]
    })

    if os.path.exists("students.csv"):
        old_data = pd.read_csv("students.csv")
        updated_data = pd.concat(
            [old_data, new_student],
            ignore_index=True
        )
    else:
        updated_data = new_student

    updated_data.to_csv(
        "students.csv",
        index=False
    )

    st.success("Student Added Successfully!")