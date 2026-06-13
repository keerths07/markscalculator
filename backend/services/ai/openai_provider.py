import requests

from backend.services.ai.provider import AIProvider


class OpenAIProvider(AIProvider):
    def __init__(self, api_key, model="gpt-4o-mini"):
        self.api_key = api_key
        self.model = model or "gpt-4o-mini"

    def generate(self, prompt):
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
