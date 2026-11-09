
import ollama

print("VALUE INVESTING COPILOT")
print("-" * 40)

try:

    response = ollama.chat(
        # model="qwen3:1.7b",
        model="qwen3:999b",
        messages=[
            {
                "role": "user",
                "content": "Explain what value investing means in two sentences."
            }
        ]
    )

    print("\nLLM RESPONSE:")
    print(response["message"]["content"])

except ollama.ResponseError as error:

    print("\nOLLAMA API ERROR:")
    print(error)

except Exception as error:

    print("\nCONNECTION OR UNEXPECTED ERROR:")
    print(error)

except ollama.ResponseError as error:
    print("\nOLLAMA API ERROR:")
    print(error)
