import os


class Settings:

    LLM_PROVIDER = os.getenv(
        "LLM_PROVIDER",
        "ollama"
    )

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "qwen2.5:7b"
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )


settings = Settings()