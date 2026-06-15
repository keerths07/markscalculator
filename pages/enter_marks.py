 

from pathlib import Path

import pandas as pd
import streamlit as st

from frontend.components.language_switcher import language_switcher
from frontend.i18n import t

DATA_FILE = Path("data/marks.csv")
DATA_FILE.parent.mkdir(exist_ok=True)

language = language_switcher()

st.title(t("marks.title", language))

student_id = st.text_input(
    t("student.id", language),
    key="enter_marks_student_id",
)

maths = st.number_input(
    t("marks.maths", language),
    min_value=0,
    max_value=100,
    key="enter_marks_maths",
)

science = st.number_input(
    t("marks.science", language),
    min_value=0,
    max_value=100,
    key="enter_marks_science",
)

english = st.number_input(
    t("marks.english", language),
    min_value=0,
    max_value=100,
    key="enter_marks_english",
)

if st.button(
    t("marks.save_button", language),
    key="enter_marks_save",
):
    if not student_id.strip():
        st.warning(t("marks.validation", language))
    else:
        total = maths + science + english
        percentage = round(total / 3, 2)

        marks_data = pd.DataFrame(
            {
                "Student ID": [student_id.strip()],
                "Maths": [maths],
                "Science": [science],
                "English": [english],
                "Total": [total],
                "Percentage": [percentage],
            }
        )

        if DATA_FILE.exists():
            old_data = pd.read_csv(DATA_FILE)
            updated_data = pd.concat(
                [old_data, marks_data],
                ignore_index=True,
            )
        else:
            updated_data = marks_data

        updated_data.to_csv(
            DATA_FILE,
            index=False,
        )

        st.success(t("marks.success", language))