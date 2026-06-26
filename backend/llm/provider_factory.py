from backend.providers.ollama_provider import OllamaProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        return OllamaProvider()