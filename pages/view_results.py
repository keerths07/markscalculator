from pathlib import Path

import pandas as pd
import streamlit as st

from backend.services.ai.service import AIService
from frontend.components.language_switcher import language_switcher
from frontend.i18n import local_number, t


STUDENTS_FILE = Path("data/students.csv")
MARKS_FILE = Path("data/marks.csv")

language = language_switcher()

st.title(t("results.title", language))

if STUDENTS_FILE.exists() and MARKS_FILE.exists():
    students = pd.read_csv(STUDENTS_FILE)
    marks = pd.read_csv(MARKS_FILE)

    results = pd.merge(students, marks, on="Student ID", how="inner")

    localized_results = results.copy()
    for column in ["Maths", "Science", "English", "Total", "Percentage"]:
        if column in localized_results.columns:
            localized_results[column] = localized_results[column].apply(
                lambda value: local_number(value, language)
            )

    st.dataframe(localized_results)

    if st.button(t("results.ai_button", language)):
        try:
            summary = AIService().summarize_student_results(
                results.to_string(index=False),
                language,
            )
            st.subheader(t("results.ai_summary", language))
            st.write(summary)
        except Exception as exc:
            st.error(f"{t('results.ai_error', language)} {exc}")
else:
    st.warning(t("results.no_data", language))
