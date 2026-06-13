import json
import locale
from datetime import date, datetime
from pathlib import Path

from babel.dates import format_date, format_datetime
from babel.numbers import format_decimal, format_currency


LOCALE_DIR = Path("frontend/locales")

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "हिन्दी",
    "te": "తెలుగు",
}

LANGUAGE_OPTIONS = {
    "English": "en",
    "हिन्दी": "hi",
    "తెలుగు": "te",
}

REGIONAL_LOCALES = {
    "en": "en_IN",
    "hi": "hi_IN",
    "te": "te_IN",
}


def detect_language():
    detected_locale = locale.getlocale()[0] or "en"
    language_code = detected_locale.split("_")[0]
    return language_code if language_code in SUPPORTED_LANGUAGES else "en"


def load_translations(language):
    file_path = LOCALE_DIR / f"{language}.json"
    fallback_path = LOCALE_DIR / "en.json"

    selected_path = file_path if file_path.exists() else fallback_path
    with open(selected_path, "r", encoding="utf-8") as file:
        return json.load(file)


def t(key, language="en"):
    translations = load_translations(language)
    fallback = load_translations("en")
    return translations.get(key, fallback.get(key, key))


def regional_locale(language="en"):
    return REGIONAL_LOCALES.get(language, "en_IN")


def local_date(value, language="en"):
    if isinstance(value, str):
        return value
    if isinstance(value, datetime):
        value = value.date()
    if isinstance(value, date):
        return format_date(value, locale=regional_locale(language))
    return value


def local_datetime(value, language="en"):
    if isinstance(value, datetime):
        return format_datetime(value, locale=regional_locale(language))
    return value


def local_number(value, language="en"):
    return format_decimal(value, locale=regional_locale(language))


def local_currency(value, language="en", currency="INR"):
    return format_currency(value, currency, locale=regional_locale(language))
