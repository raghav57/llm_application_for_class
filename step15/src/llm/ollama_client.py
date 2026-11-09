import ollama

from src.config.settings import (
    OLLAMA_HOST,
    MODEL,
    TEMPERATURE
)


class OllamaClient:

    def __init__(self):

        self.client = ollama.Client(
            host=OLLAMA_HOST
        )

        self.model = MODEL
        self.temperature = TEMPERATURE

    # Step 16: Add reliability to check Ollama is available

    def check_connection(self):
        try:
            self.client.show(self.model)

            return True, (
                f"Ollama is available and model '{self.model}' is ready."
            )

        except Exception as error:
            return False, (
                f"Unable to initialize Ollama model '{self.model}'. "
                f"Details: {error}"
            )


    # --------------------------------
    # Generate a complete response
    # --------------------------------

    def generate(self, messages):

        response = self.client.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": self.temperature
            },
            stream=False
        )

        return response["message"]["content"]

    # --------------------------------
    # Generate response with token usage
    # --------------------------------

    def generate_with_usage(self, messages, json_mode=False):

        kwargs = {
            "model": self.model,
            "messages": messages,
            "options": {
                "temperature": self.temperature
            },
            "stream": False
        }

        if json_mode:
            kwargs["format"] = "json"

        response = self.client.chat(**kwargs)

        return {
            "content": response["message"]["content"],
            "input_tokens": response.get("prompt_eval_count", 0) or 0,
            "output_tokens": response.get("eval_count", 0) or 0
        }

    # --------------------------------
    # Generate a streamed response
    # --------------------------------

    def generate_stream(self, messages):

        response_stream = self.client.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": self.temperature
            },
            stream=True
        )

        for chunk in response_stream:

            content = chunk["message"]["content"]

            if content:
                yield content

    # --------------------------------
    # Stream response with token usage
    # --------------------------------

    def generate_stream_with_usage(self, messages):

        response_stream = self.client.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": self.temperature
            },
            stream=True
        )

        usage = {
            "input_tokens": 0,
            "output_tokens": 0
        }

        for chunk in response_stream:

            content = chunk["message"]["content"]

            if content:
                yield content

            # Usage metadata is available on the final chunk
            if chunk.get("done", False):

                usage["input_tokens"] = (
                    chunk.get("prompt_eval_count", 0) or 0
                )

                usage["output_tokens"] = (
                    chunk.get("eval_count", 0) or 0
                )

        return usage