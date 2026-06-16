import streamlit as st

from frontend.components.language_switcher import language_switcher
from frontend.i18n import t

st.set_page_config(
    page_title="Student Management System",
    page_icon=":mortar_board:",
    layout="wide",
)

language = language_switcher()

st.title(t("app.title", language))
st.write(t("home.welcome", language))
st.info(t("home.description", language))
