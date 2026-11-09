
import ollama

print("VALUE INVESTING COPILOT")
print("-" * 40)

response = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": "Explain value investing and its three key principles."
        }
    ],
    stream=False
)
print("-" * 40)
print("\nNON-STREAMING RESPONSE:\n")
print(response["message"]["content"])
print("-" * 40)
print("-" * 40)
print("-" * 40)
print("\n")



response = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": "Explain value investing and its three key principles."
        }
    ],
    stream=True
)

print("-" * 40)
print("\nSTREAMING RESPONSE:\n")
print("-" * 40)

for chunk in response:
    content = chunk["message"]["content"]

    print(content, end="", flush=True)

print("\n\nGeneration completed.")