import requests

from backend.llm.base_provider import BaseLLMProvider
from backend.config.settings import settings


class OllamaProvider(BaseLLMProvider):

    def generate(
        self,
        prompt: str
    ) -> str:

        try:

            response = requests.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": settings.OLLAMA_MODEL,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return data["response"]

        except requests.exceptions.Timeout:

            raise RuntimeError(
                "Ollama request timed out."
            )

        except requests.exceptions.ConnectionError:

            raise RuntimeError(
                "Unable to connect to the Ollama server."
            )

        except requests.exceptions.HTTPError as e:

            raise RuntimeError(
                f"Ollama HTTP error: {e}"
            )

        except Exception as e:

            raise RuntimeError(
                f"Unexpected Ollama error: {e}"
            )