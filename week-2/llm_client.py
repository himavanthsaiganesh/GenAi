from abc import ABC, abstractmethod
import requests

# Common interface
class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt):
        pass  # pass is a placeholder. It indicates that we are not providing an implementation here.

# Ollama local provider
class OllamaProvider(LLMProvider):
    def __init__(self, model="llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["response"]

# Common client
class LLMClient:
    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)
