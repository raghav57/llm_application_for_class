
import ollama

# -----------------------------------------
# STEP 12.1 - SLIDING WINDOW CONFIGURATION
# -----------------------------------------

MAX_HISTORY_MESSAGES = 4

print("VALUE INVESTING COPILOT")
print("-" * 40)
print("Ask me anything about value investing.")
print("Type /quit to exit.\n")

# Preserve the system instruction throughout the conversation
messages = [
    {
        "role": "system",
        "content": "You are a helpful value investing assistant."
    }
]

while True:

    # -----------------------------------------
    # STEP 10 - CONVERSATION STATE MANAGEMENT
    # -----------------------------------------

    user_input = input("\nYou: ").strip()

    if user_input.lower() == "/quit":
        print("\nConversation ended.")
        break

    if not user_input:
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        # -----------------------------------------
        # STEP 9 - LLM RESPONSE
        # -----------------------------------------

        print("\nMESSAGES SENT TO LLM:", len(messages))
        
        response = ollama.chat(
            model="qwen3:1.7b",
            messages=messages
        )

        assistant_reply = response["message"]["content"]

        print("\nAssistant:", assistant_reply)

        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

        # -----------------------------------------
        # STEP 11 - TOKEN COUNTING
        # -----------------------------------------

        prompt_tokens = response["prompt_eval_count"]
        generated_tokens = response["eval_count"]

        print("\nTOKEN USAGE")
        print("Input tokens:", prompt_tokens)
        print("Generated tokens:", generated_tokens)
        print("Total tokens:", prompt_tokens + generated_tokens)

        # -----------------------------------------
        # STEP 12.2 - SLIDING WINDOW MANAGEMENT
        # -----------------------------------------

        if len(messages) > MAX_HISTORY_MESSAGES + 1:
            messages = [messages[0]] + messages[-MAX_HISTORY_MESSAGES:]

        # -----------------------------------------
        # STEP 12.3 - OBSERVE ACTIVE HISTORY
        # -----------------------------------------

        print("\nACTIVE CONVERSATION HISTORY")
        print("Messages retained:", len(messages) - 1)

        for message in messages[1:]:
            print(
                message["role"],
                ":",
                message["content"][:80]
            )

    except ollama.ResponseError as error:
        print("\nOLLAMA API ERROR:")
        print(error)

    except Exception as error:
        print("\nCONNECTION OR UNEXPECTED ERROR:")
        print(error)

print("\nTotal messages retained:", len(messages))
