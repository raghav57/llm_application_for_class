
import ollama

print("VALUE INVESTING COPILOT")
print("-" * 40)
print("Type /quit to exit.\n")

# Initialize conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful value investing assistant."
    }
]

while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() == "/quit":
        print("\nConversation ended.")
        break

    if not user_input:
        continue

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Send conversation to Ollama
    response = ollama.chat(
        model="qwen3:1.7b",
        messages=messages
    )

    # Extract assistant response
    assistant_reply = response["message"]["content"]

    print("\nAssistant:", assistant_reply)

    # Store assistant response
    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    # Extract token usage
    prompt_tokens = response["prompt_eval_count"]
    generated_tokens = response["eval_count"]

    print("\nTOKEN USAGE")
    print("Input tokens:", prompt_tokens)
    print("Generated tokens:", generated_tokens)
    print("Total tokens:", prompt_tokens + generated_tokens)

print("\nTotal messages stored:", len(messages))
