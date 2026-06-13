import os

import pandas as pd
import streamlit as st

from backend.i18n import get_locale, translate


locale = get_locale()
t = lambda key: translate(locale, key)

st.title(t("add_student"))

student_id = st.text_input(t("student_id"))
student_name = st.text_input(t("student_name"))

if st.button(t("add_student_button")):
    new_student = pd.DataFrame({
        "Student ID": [student_id],
        "Name": [student_name],
    })

    if os.path.exists("students.csv"):
        old_data = pd.read_csv("students.csv")
        updated_data = pd.concat(
            [old_data, new_student],
            ignore_index=True,
        )
    else:
        updated_data = new_student

    updated_data.to_csv(
        "students.csv",
        index=False,
    )

    st.success(t("student_added"))
