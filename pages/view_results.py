import pandas as pd
import streamlit as st
from pathlib import Path

from backend.i18n import get_locale, translate
from frontend.components.language_switcher import language_switcher
from frontend.i18n import local_number

locale = get_locale()
def t(key):
    return translate(locale, key)
language = language_switcher()

STUDENTS_FILE = Path("data/students.csv")
MARKS_FILE = Path("data/marks.csv")

st.title(t("results.title"))

if STUDENTS_FILE.exists() and MARKS_FILE.exists():

    students = pd.read_csv(STUDENTS_FILE)
    marks = pd.read_csv(MARKS_FILE)

    results = pd.merge(students, marks, on="Student ID", how="left")

    st.subheader(t("ai_insights"))
    st.dataframe(results)

else:
    st.warning(t("results.no_data"))