import ollama

response = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": "Explain value investing in three sentences."
        }
    ]
)

print(response["message"]["content"])
