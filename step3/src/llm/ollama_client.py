import ollama


class OllamaClient:

    def __init__(self, model="qwen3:1.7b"):
        self.model = model

    def generate(self, messages):

        response = ollama.chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]