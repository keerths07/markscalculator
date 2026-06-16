import streamlit as st

from backend.i18n import get_locale, translate

locale = get_locale()


def t(key):
    return translate(locale, key)


st.title(t("home.title"))
st.write(t("home.welcome"))
st.info(t("home.info"))
