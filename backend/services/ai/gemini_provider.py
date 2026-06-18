import requests

from backend.services.ai.provider import AIProvider


class GeminiProvider(AIProvider):
    def __init__(self, api_key, model="gemini-1.5-flash"):
        self.api_key = api_key
        self.model = model or "gemini-1.5-flash"

    def generate(self, prompt):
        base_url = "https://generativelanguage.googleapis.com/v1beta/models/"
        url = base_url + f"{self.model}:generateContent"

        payload = {"contents": [{"parts": [{"text": prompt}]}]}

        response = requests.post(
            url,
            params={"key": self.api_key},
            json=payload,
            timeout=120,
        )

        response.raise_for_status()
        data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]
