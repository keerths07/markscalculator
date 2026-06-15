import json
from pathlib import Path

SETTINGS_FILE = Path("data/settings.json")

DEFAULT_SETTINGS = {
    "language": "en",
    "ai_provider": "Ollama",
    "model": "llama3",
    "ollama_url": "http://localhost:11434",
    "api_keys": {
        "OpenAI": "",
        "Gemini": ""
    }
}


def get_settings():
    SETTINGS_FILE.parent.mkdir(exist_ok=True)

    if not SETTINGS_FILE.exists():
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
        saved_settings = json.load(file)

    settings = DEFAULT_SETTINGS.copy()
    settings.update(saved_settings)
    settings["api_keys"] = {
        **DEFAULT_SETTINGS["api_keys"],
        **saved_settings.get("api_keys", {}),
    }
    return settings


def save_settings(settings):
    SETTINGS_FILE.parent.mkdir(exist_ok=True)

    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=2)
