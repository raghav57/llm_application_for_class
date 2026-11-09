
import ollama

# -----------------------------------------
# STEP 13.2 - CONFIGURATION
# -----------------------------------------

MODEL = "qwen3:1.7b"

KEEP_RECENT_MESSAGES = 4
SUMMARY_TRIGGER_MESSAGES = 6

SYSTEM_PROMPT = """
You are a helpful value investing assistant.
Help users understand companies, financial metrics,
business quality and investment risks.
"""

# -----------------------------------------
# CONVERSATION STATE
# -----------------------------------------

conversation_summary = ""

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("VALUE INVESTING COPILOT")
print("-" * 40)
print("Ask me anything about value investing.")
print("Type /quit to exit.\n")


while True:

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
        # STEP 13.2.1 - PREPARE LLM CONTEXT
        # -----------------------------------------

        request_messages = [messages[0]]

        if conversation_summary:
            request_messages.append({
                "role": "system",
                "content": (
                    "Summary of earlier conversation:\n"
                    + conversation_summary
                )
            })

        request_messages.extend(messages[1:])

        # -----------------------------------------
        # STEP 13.2.2 - GENERATE RESPONSE
        # -----------------------------------------

        response = ollama.chat(
            model=MODEL,
            messages=request_messages
        )

        assistant_reply = response["message"]["content"]

        print("\nAssistant:", assistant_reply)

        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

        # -----------------------------------------
        # STEP 13.2.3 - TOKEN COUNTING
        # -----------------------------------------

        print("\nTOKEN USAGE")
        print("Input tokens:", response["prompt_eval_count"])
        print("Generated tokens:", response["eval_count"])

        # -----------------------------------------
        # STEP 13.2.4 - CHECK SUMMARISATION TRIGGER
        # -----------------------------------------

        if len(messages) - 1 > SUMMARY_TRIGGER_MESSAGES:

            print("\nGenerating conversation summary...")

            # Select older messages for summarisation
            older_messages = messages[1:-KEEP_RECENT_MESSAGES]

            conversation_text = "\n".join(
                message["role"] + ": " + message["content"]
                for message in older_messages
            )

            # Include the previous summary to preserve
            # important information across summarisation cycles
            summarisation_prompt = f"""
You are a conversation summarisation assistant.

Existing conversation summary:
{conversation_summary if conversation_summary else "No previous summary."}

New conversation messages:
{conversation_text}

Create an updated, concise summary.

Preserve important facts, user preferences,
investment horizon, companies discussed,
financial figures and unresolved questions.

Do not invent information.
Clearly distinguish user-provided facts from assumptions.
"""

            summary_response = ollama.chat(
                model=MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You create accurate conversation summaries."
                    },
                    {
                        "role": "user",
                        "content": summarisation_prompt
                    }
                ]
            )

            conversation_summary = (
                summary_response["message"]["content"]
            )

            # -----------------------------------------
            # STEP 13.2.5 - UPDATE CONVERSATION HISTORY
            # -----------------------------------------

            messages = (
                [messages[0]]
                + messages[-KEEP_RECENT_MESSAGES:]
            )

            print("\nUPDATED CONVERSATION SUMMARY")
            print(conversation_summary)

            print("\nOlder messages summarised and removed.")

        # -----------------------------------------
        # OBSERVE ACTIVE CONTEXT
        # -----------------------------------------

        print("\nACTIVE CONVERSATION")
        print("Summary available:", bool(conversation_summary))
        print("Recent messages retained:", len(messages) - 1)

    except ollama.ResponseError as error:
        print("\nOLLAMA API ERROR:")
        print(error)

    except Exception as error:
        print("\nCONNECTION OR UNEXPECTED ERROR:")
        print(error)


print("\nConversation ended.")
