# Session 11 – Step 10: Conversation State Management

## Objective

Understand how to maintain conversation history in an LLM application so that the assistant can respond to follow-up questions using previous conversational context.

The practical implementation extends the Value Investing Copilot using Python, Ollama and Qwen3 1.7B.

## Folder Structure

```text
step10/
├── src/
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── company_schema.py
│   │   ├── financial_schema.py
│   │   ├── valuation_schema.py
│   │   ├── risk_schema.py
│   │   ├── verdict_schema.py
│   │   └── stock_schema.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Topics Covered

| Substep   | Topic                               |   Duration |
| --------- | ----------------------------------- | ---------: |
| 10.1      | Stateless vs Stateful Conversations |      3 min |
| 10.2      | Maintaining Conversation History    |      7 min |
| 10.3      | Multi-turn Conversation Testing     |      5 min |
| **Total** |                                     | **15 min** |

## 10.1 – Stateless vs Stateful Conversations

### Stateless Conversations

In a stateless interaction, every API request is treated independently.

Example:

- User: Analyse Infosys.
- Assistant: Infosys has strong fundamentals.
- User: What about its debt?
- Assistant: Which company are you referring to?

The second request does not contain the previous conversation.

### Stateful Conversations

In a stateful interaction, the application maintains previous messages and sends the relevant conversation history with each new request.

Example:

- User: Analyse Infosys.
- Assistant: Infosys has strong fundamentals.
- User: What about its debt?
- Assistant: Infosys has a relatively manageable debt position...

The assistant can interpret follow-up questions using previous context.

## 10.2 – Maintaining Conversation History

Python maintains the conversation using a list called `messages`.

### Initialize conversation history

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful value investing assistant."
    }
]
```

### Append the user message

```python
messages.append({
    "role": "user",
    "content": user_input
})
```

### Send conversation history to Ollama

```python
response = ollama.chat(
    model="qwen3:1.7b",
    messages=messages
)
```

### Capture the assistant response

```python
assistant_reply = response["message"]["content"]
```

### Append the assistant response

```python
messages.append({
    "role": "assistant",
    "content": assistant_reply
})
```

Both user and assistant messages are retained in the conversation history.

## 10.3 – Multi-turn Conversation Testing

The application implements a continuous conversation loop using Python's `while` statement.

```python
while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() == "/quit":
        print("Conversation ended.")
        break

    if not user_input:
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

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
```

### Test Conversation

Run the application:

```powershell
python -m src.main
```

Try the following conversation:

1. Analyse Infosys as a potential value investment.
2. What about its debt?
3. What are its major risks?
4. Would you consider it a value investment?
5. Type `/quit` to exit.

Observe how the assistant uses previous messages to understand follow-up questions.

## How Conversation State Works

1. Initialize an empty conversation history with a system instruction.
2. Append the user's message.
3. Send the complete message history to Ollama.
4. Receive the assistant response.
5. Append the assistant response to the history.
6. Repeat until the user exits.

## Important Engineering Concept

**The LLM does not automatically remember previous API calls.**

The Python application maintains conversation history and provides that history with each subsequent request.

The conversation state in this implementation exists in application memory. It is not persisted across application restarts.

## Scope and Limitations

This implementation uses a simple Python list to demonstrate conversation state.

It does not yet implement:

- Persistent conversation storage.
- Multiple independent user sessions.
- Token-based context management.
- Sliding window conversation history.
- Conversation summarisation.

These concepts are addressed in subsequent steps.

## Final Learning Outcome

Students build a continuous conversational LLM application that maintains context across multiple user interactions.

## Technologies Used

- Python 3.13
- Ollama
- Qwen3 1.7B

## Final Takeaway

**Conversation state transforms independent LLM requests into contextual multi-turn interactions.**

The application, not the model alone, is responsible for maintaining and supplying conversation history.
