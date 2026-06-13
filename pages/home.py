import streamlit as st

from frontend.components.language_switcher import language_switcher
from frontend.i18n import t


language = language_switcher()

st.title(t("home.title", language))
st.write(t("home.welcome", language))
st.info(t("home.description", language))
