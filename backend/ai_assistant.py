import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def build_marks_prompt(results_text):
    return (
        "You are an assistant for a student marks calculator app. "
        "Analyze the marks table and give concise, practical insights: "
        "overall performance, students needing support, strong subjects, "
        "and next-step suggestions.\n\n"
        f"Marks data:\n{results_text}"
    )

def generate_with_ollama(prompt, model="llama3.2", base_url="http://localhost:11434"):
    url = f"{base_url.rstrip('/')}/api/chat"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }

    data = _post_json(url, payload)
    return data.get("message", {}).get("content", "").strip()


def generate_with_byok(prompt, api_key, model, base_url="https://api.openai.com/v1"):
    url = f"{base_url.rstrip('/')}/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }
    headers = {"Authorization": f"Bearer {api_key}"}

    data = _post_json(url, payload, headers=headers)
    return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()


def _post_json(url, payload, headers=None):
    request_headers = {"Content-Type": "application/json"}
    if headers:
        request_headers.update(headers)

    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=request_headers,
        method="POST",
    )

    try:
        with urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"AI service returned {error.code}: {details}") from error
    except URLError as error:
        raise RuntimeError(
            f"Could not connect to AI service: {error.reason}"
        ) from error
