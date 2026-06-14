import streamlit as st


st.title("🎓 Student Result Management System")

st.write("Welcome to the Student Result Management System")

st.info("Use the sidebar to add students, enter marks and view results.")

from frontend.components.language_switcher import language_switcher
from frontend.i18n import t


st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide",
)

language = language_switcher()

st.title(f"🎓 {t('app.title', language)}")

st.write(t("home.welcome", language))
st.info(t("home.description", language))

