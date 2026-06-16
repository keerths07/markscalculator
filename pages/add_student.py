from pathlib import Path

import pandas as pd
import streamlit as st

from frontend.components.language_switcher import language_switcher
from frontend.i18n import t

DATA_FILE = Path("data/students.csv")
DATA_FILE.parent.mkdir(exist_ok=True)

language = language_switcher()

st.title(t("student.add_title", language))

student_id = st.text_input(
    t("student.id", language),
    key="add_student_id",
)
student_name = st.text_input(
    t("student.name", language),
    key="add_student_name",
)

if st.button(t("student.add_button", language), key="add_student_submit"):
    student_id = student_id.strip()
    student_name = student_name.strip()

    if not student_id or not student_name:
        st.warning(t("student.validation", language))
    else:
        new_student = pd.DataFrame(
            {
                "Student ID": [student_id],
                "Name": [student_name],
            }
        )

        if DATA_FILE.exists():
            old_data = pd.read_csv(DATA_FILE)
            updated_data = pd.concat(
                [old_data, new_student],
                ignore_index=True,
            )
        else:
            updated_data = new_student

        updated_data.to_csv(DATA_FILE, index=False)
        st.success(t("student.success", language))
