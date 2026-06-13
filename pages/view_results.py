import os

import pandas as pd
import streamlit as st

from backend.ai_assistant import build_marks_prompt, generate_with_byok, generate_with_ollama
from backend.i18n import get_locale, language_name, translate


locale = get_locale()
t = lambda key: translate(locale, key)

st.title(t("view_results"))

if os.path.exists("students.csv") and os.path.exists("marks.csv"):
    students = pd.read_csv("students.csv")
    marks = pd.read_csv("marks.csv")

    results = pd.merge(
        students,
        marks,
        on="Student ID",
    )

    st.dataframe(results)

    st.subheader(t("ai_insights"))

    ai_provider = st.radio(
        t("ai_provider"),
        [t("local_ai"), t("byok")],
        horizontal=True,
    )

    prompt = build_marks_prompt(results.to_csv(index=False))
    prompt = f"{prompt}\n\nRespond in {language_name(locale)}."

    if ai_provider == t("local_ai"):
        ollama_url = st.text_input(t("ollama_url"), value="http://localhost:11434")
        ollama_model = st.text_input(t("ollama_model"), value="llama3.2")

        if st.button(t("generate_ai_insights")):
            with st.spinner(t("generating_local")):
                try:
                    insights = generate_with_ollama(
                        prompt,
                        model=ollama_model,
                        base_url=ollama_url,
                    )
                    st.write(insights)
                except RuntimeError as error:
                    st.error(str(error))

    else:
        api_base_url = st.text_input(t("ai_base_url"), value="https://api.openai.com/v1")
        byok_model = st.text_input(t("model"), value="gpt-4.1-mini")
        api_key = st.text_input(t("api_token"), type="password")

        if st.button(t("generate_ai_insights")):
            if not api_key:
                st.warning(t("enter_api_token"))
            else:
                with st.spinner(t("generating_byok")):
                    try:
                        insights = generate_with_byok(
                            prompt,
                            api_key=api_key,
                            model=byok_model,
                            base_url=api_base_url,
                        )
                        st.write(insights)
                    except RuntimeError as error:
                        st.error(str(error))

else:
    st.warning(t("no_data"))
