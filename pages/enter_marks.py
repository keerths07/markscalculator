<<<<<<< HEAD
import os

import pandas as pd
import streamlit as st

from backend.i18n import get_locale, translate


locale = get_locale()
t = lambda key: translate(locale, key)

st.title(t("enter_marks"))

student_id = st.text_input(t("student_id"))

maths = st.number_input(
    t("maths_marks"),
    min_value=0,
    max_value=100,
)

science = st.number_input(
    t("science_marks"),
    min_value=0,
    max_value=100,
)

english = st.number_input(
    t("english_marks"),
    min_value=0,
    max_value=100,
)

if st.button(t("save_marks")):
    total = maths + science + english
    percentage = total / 3

    marks_data = pd.DataFrame({
        "Student ID": [student_id],
        "Maths": [maths],
        "Science": [science],
        "English": [english],
        "Total": [total],
        "Percentage": [percentage],
    })

    if os.path.exists("marks.csv"):
        old_data = pd.read_csv("marks.csv")
        updated_data = pd.concat(
            [old_data, marks_data],
            ignore_index=True,
        )
=======
from pathlib import Path

import pandas as pd
import streamlit as st

from frontend.components.language_switcher import language_switcher
from frontend.i18n import t


DATA_FILE = Path("data/marks.csv")
DATA_FILE.parent.mkdir(exist_ok=True)

language = language_switcher()

st.title(t("marks.title", language))

student_id = st.text_input(t("student.id", language))

maths = st.number_input(t("marks.maths", language), min_value=0, max_value=100)
science = st.number_input(t("marks.science", language), min_value=0, max_value=100)
english = st.number_input(t("marks.english", language), min_value=0, max_value=100)

if st.button(t("marks.save_button", language)):
    if not student_id.strip():
        st.warning(t("marks.validation", language))
>>>>>>> 8b52ab5aab620069d441cd947d3da60ba3dc8cd1
    else:
        total = maths + science + english
        percentage = total / 3

<<<<<<< HEAD
    updated_data.to_csv(
        "marks.csv",
        index=False,
    )

    st.success(t("marks_saved"))
=======
        marks_data = pd.DataFrame({
            "Student ID": [student_id.strip()],
            "Maths": [maths],
            "Science": [science],
            "English": [english],
            "Total": [total],
            "Percentage": [percentage],
        })

        if DATA_FILE.exists():
            old_data = pd.read_csv(DATA_FILE)
            updated_data = pd.concat([old_data, marks_data], ignore_index=True)
        else:
            updated_data = marks_data

        updated_data.to_csv(DATA_FILE, index=False)
        st.success(t("marks.success", language))
>>>>>>> 8b52ab5aab620069d441cd947d3da60ba3dc8cd1
