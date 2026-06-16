
from pathlib import Path

import pandas as pd
import streamlit as st

from frontend.components.language_switcher import language_switcher
from frontend.i18n import t

DATA_FILE = Path("data/students.csv")
DATA_FILE.parent.mkdir(exist_ok=True)

language = language_switcher()

st.title(t("student.add_title", language))

student_id = st.text_input(t("student.id", language))
student_name = st.text_input(t("student.name", language))

if st.button(t("student.add_button", language)):
    if not student_id.strip() or not student_name.strip():
        st.warning(t("student.validation", language))
    else:
        new_student = pd.DataFrame(
            
               {
    "student_id": [student_id.strip()],
    "name": [student_name.strip()],
    "class": [""]
}
        )

        if DATA_FILE.exists():
            old_data = pd.read_csv(DATA_FILE)
            updated_data = pd.concat([old_data, new_student], ignore_index=True)
        else:
            updated_data = new_student

        updated_data.to_csv(DATA_FILE, index=False)
        st.success(t("student_added", language))