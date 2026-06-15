import streamlit as st

from backend.services.settings_service import get_settings, save_settings
from frontend.i18n import LANGUAGE_OPTIONS, detect_language


def language_switcher():
    settings = get_settings()

    if "language" not in st.session_state:
        st.session_state.language = settings.get("language") or detect_language()

    current_language = st.session_state.language
    labels = list(LANGUAGE_OPTIONS.keys())
    codes = list(LANGUAGE_OPTIONS.values())
    current_index = codes.index(current_language) if current_language in codes else 0

    selected_label = st.sidebar.selectbox(
    "Language / भाषा / భాష",
    labels,
    index=current_index,
    key="language_selector_add_student"
)

    selected_language = LANGUAGE_OPTIONS[selected_label]
    st.session_state.language = selected_language

    if settings.get("language") != selected_language:
        settings["language"] = selected_language
        save_settings(settings)

    return selected_language
