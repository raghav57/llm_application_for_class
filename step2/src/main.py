import ollama

response = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "system",
            # "content": "You are Warren Buffett explaining investment concepts to a 15-year-old. Use simple language, practical analogies and avoid technical financial jargon."
            "content": "You are a professional value investing analyst. Explain financial concepts in simple language suitable for beginners."
        },
        {
            "role": "user",
            "content": "Explain value investing."
        }
    ]
)

print("EXPERIMENT 2: SYSTEM + USER MESSAGE")
print(response["message"]["content"])
