
import ollama

print("VALUE INVESTING COPILOT")
print("-" * 40)
print("Ask me anything about value investing.")
print("Type /quit to exit.\n")

# 1. Initialize conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful value investing assistant."
    }
]

# 2. Start continuous conversation
while True:

    user_input = input("\nYou: ").strip()

    # 3. Check whether the user wants to exit
    if user_input.lower() == "/quit":
        print("\nConversation ended.")
        break

    # Ignore empty messages
    if not user_input:
        continue

    # 4. Add user message to conversation history
    messages.append({
        "role": "user",
        "content": user_input
    })

    # 5. Send conversation history to Ollama
    response = ollama.chat(
        model="qwen3:1.7b",
        messages=messages
    )

    # 6. Extract assistant response
    assistant_reply = response["message"]["content"]

    print("\nAssistant:", assistant_reply)

    # 7. Add assistant response to history
    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

# 8. Display conversation statistics
print("\nTotal messages stored:", len(messages))
