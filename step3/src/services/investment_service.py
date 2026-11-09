from src.llm.ollama_client import OllamaClient
from src.prompts.system_prompt import SYSTEM_PROMPT


class InvestmentService:

    def __init__(self):
        self.llm = OllamaClient()

    def analyze(self, user_question):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_question
            }
        ]

        response = self.llm.generate(messages)

        return response