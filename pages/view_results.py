import os
from pathlib import Path

import pandas as pd
import streamlit as st

from backend.ai_assistant import (build_marks_prompt, generate_with_byok,
                                  generate_with_ollama)
from backend.i18n import get_locale, language_name, translate
from backend.services.ai.service import AIService
from frontend.components.language_switcher import language_switcher
from frontend.i18n import local_number, t

locale = get_locale()
translate_text = lambda key: translate(locale, key)

STUDENTS_FILE = Path("data/students.csv")
MARKS_FILE = Path("data/marks.csv")

language = language_switcher()

st.title(t("results.title", language))

if STUDENTS_FILE.exists() and MARKS_FILE.exists():
    try:
        students = pd.read_csv(STUDENTS_FILE)
        marks = pd.read_csv(MARKS_FILE)

        # Merge using matching column names
        results = pd.merge(
            students,
            marks,
            left_on="student_id",
            right_on="Student ID",
            how="inner",
        )

        # Display results table
        localized_results = results.copy()

        for column in ["Maths", "Science", "English", "Total", "Percentage"]:
            if column in localized_results.columns:
                localized_results[column] = localized_results[column].apply(
                    lambda value: local_number(value, language)
                )

        st.dataframe(localized_results)

        # AI Insights
        st.subheader(translate_text("ai_insights"))

        ai_provider = st.radio(
            translate_text("ai_provider"),
            [translate_text("local_ai"), translate_text("byok")],
            horizontal=True,
            key="results_ai_provider",
        )

        prompt = build_marks_prompt(results.to_csv(index=False))
        prompt = f"{prompt}\n\nRespond in {language_name(locale)}."

        if ai_provider == translate_text("local_ai"):

            ollama_url = st.text_input(
                translate_text("ollama_url"),
                value="http://localhost:11434",
                key="results_ollama_url",
            )

            ollama_model = st.text_input(
                translate_text("ollama_model"),
                value="llama3.2",
                key="results_ollama_model",
            )

            if st.button(
                translate_text("generate_ai_insights"),
                key="results_generate_local",
            ):
                with st.spinner(translate_text("generating_local")):
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

            api_base_url = st.text_input(
                translate_text("ai_base_url"),
                value="https://api.openai.com/v1",
                key="results_api_base",
            )

            byok_model = st.text_input(
                translate_text("model"),
                value="gpt-4.1-mini",
                key="results_byok_model",
            )

            api_key = st.text_input(
                translate_text("api_token"),
                type="password",
                key="results_api_key",
            )

            if st.button(
                translate_text("generate_ai_insights"),
                key="results_generate_byok",
            ):
                if not api_key:
                    st.warning(translate_text("enter_api_token"))
                else:
                    with st.spinner(translate_text("generating_byok")):
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

        if st.button(
            t("results.ai_button", language),
            key="results_summary_button",
        ):
            try:
                summary = AIService().summarize_student_results(
                    results.to_string(index=False),
                    language,
                )
                st.subheader(t("results.ai_summary", language))
                st.write(summary)
            except Exception as exc:
                st.error(f"{t('results.ai_error', language)} {exc}")

    except Exception as exc:
        st.error(f"Error loading results: {exc}")

else:
    st.warning(t("results.no_data", language))
