import streamlit as st

from backend.services.settings_service import get_settings, save_settings
from frontend.components.language_switcher import language_switcher
from frontend.i18n import LANGUAGE_OPTIONS, t

language = language_switcher()
settings = get_settings()

st.title(t("settings.title", language))

language_labels = list(LANGUAGE_OPTIONS.keys())
language_codes = list(LANGUAGE_OPTIONS.values())
current_language_index = language_codes.index(settings.get("language", language))

selected_language_label = st.selectbox(
    t("settings.language"),
    language_labels,
    index=current_language_index,
    key="settings_language",
)

provider_options = ["Ollama", "OpenAI", "Gemini"]
selected_provider = st.selectbox(
    t("settings.provider", language),
    provider_options,
    index=provider_options.index(settings.get("ai_provider", "Ollama")),
)

model = st.text_input(
    t("settings.model", language),
    value=settings.get("model", "llama3"),
)

ollama_url = st.text_input(
    t("settings.ollama_url", language),
    value=settings.get("ollama_url", "http://localhost:11434"),
)

api_keys = settings.get("api_keys", {})
api_key = ""
if selected_provider != "Ollama":
    api_key = st.text_input(
        t("settings.api_key", language),
        value=api_keys.get(selected_provider, ""),
        type="password",
    )

if st.button(t("settings.save_button", language)):
    selected_language = LANGUAGE_OPTIONS[selected_language_label]

    updated_api_keys = {
        **api_keys,
        selected_provider: api_key,
    }

    save_settings(
        {
            "language": selected_language,
            "ai_provider": selected_provider,
            "model": model,
            "ollama_url": ollama_url,
            "api_keys": updated_api_keys,
        }
    )

    st.session_state.language = selected_language
    st.success(t("settings.success", selected_language))
