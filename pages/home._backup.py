import streamlit as st

from backend.i18n import get_locale, translate

locale = get_locale()


def t(key):
    return translate(locale, key)


st.title(t("home"))
st.write(t("home_intro"))
st.info(t("home_features"))
