import streamlit as st

from backend.i18n import get_locale, translate

locale = get_locale()
t = lambda key: translate(locale, key)

st.title(t("home"))
st.write(t("home_intro"))
st.info(t("home_features"))
