from backend.services.ai.gemini_provider import GeminiProvider
from backend.services.ai.ollama_provider import OllamaProvider
from backend.services.ai.openai_provider import OpenAIProvider
from backend.services.settings_service import get_settings


class AIService:
    def __init__(self):
        self.settings = get_settings()

    def _provider(self):
        provider = self.settings.get("ai_provider", "Ollama")
        model = self.settings.get("model", "llama3")

        if provider == "Ollama":
            return OllamaProvider(
                base_url=self.settings.get("ollama_url", "http://localhost:11434"),
                model=model,
            )

        api_key = self.settings.get("api_keys", {}).get(provider, "")
        if not api_key:
            raise ValueError(f"{provider} API key is missing.")

        if provider == "OpenAI":
            return OpenAIProvider(api_key=api_key, model=model)

        if provider == "Gemini":
            return GeminiProvider(api_key=api_key, model=model)

        raise ValueError(f"Unsupported AI provider: {provider}")

    def summarize_student_results(self, results_text, language="en"):
        prompt = f"""
Analyze this student marks data.

Return a short, useful academic performance summary with:
1. Strengths
2. Weaknesses
3. Suggestions

Use this language code for the answer: {language}

Data:
{results_text}
"""
        return self._provider().generate(prompt)
