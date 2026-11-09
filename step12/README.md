# Session 11 – Step 12: Sliding Window Context Management

## 1. Objective

In this step, we learn how to manage conversation history in an LLM application using a sliding window.

In Step 10, we implemented conversation state management to maintain chat history.

In Step 11, we measured token consumption using Ollama response metadata.

In Step 12, we introduce a mechanism to control how much conversation history is retained and sent to the LLM.

**Core idea:** Instead of retaining the entire conversation indefinitely, maintain a limited window of recent messages.

## 2. Learning Outcomes

By the end of this step, students should be able to:

- Explain why conversation history grows over time.
- Understand the concept of a sliding window.
- Implement message-count-based history management in Python.
- Preserve system instructions while removing older messages.
- Observe how the active conversation history changes.
- Understand the trade-off between bounded context and loss of historical information.

## 3. Key Concepts

### 3.1 The Context Growth Problem

In a stateful LLM application, every new request can include previous conversation messages.

As conversations become longer:

- Input token consumption increases.
- More historical context is processed.
- Requests may eventually exceed the model's context window.
- Application latency and inference costs may increase.

### 3.2 What Is a Sliding Window?

A sliding window retains only a fixed number of recent conversation messages.

For example, with a window size of four:

- The latest four conversational messages are retained.
- Older messages are removed from the active history.
- The system instruction is preserved separately.

The window moves forward as new messages arrive.

### 3.3 Message Count vs Token Count

This implementation uses a message-count-based window.

It does not guarantee a fixed token budget because individual messages can have very different lengths.

A token-budget-based window is a possible future improvement.

## 4. Implementation

### Project Structure

```text
step12/
│
├── src/
│   ├── schemas/
│   └── main.py
│
├── README.md
└── requirements.txt
```

### Configuration

```python
MAX_HISTORY_MESSAGES = 4
```

This sets the maximum number of conversational messages retained after each assistant response.

### Core Sliding Window Logic

```python
if len(messages) > MAX_HISTORY_MESSAGES + 1:
    messages = [messages[0]] + messages[-MAX_HISTORY_MESSAGES:]
```

Explanation:

- `messages[0]` preserves the system instruction.
- `messages[-MAX_HISTORY_MESSAGES:]` selects the latest four conversational messages.
- Older conversational messages are removed.

The trimming happens after the assistant response is appended.

Consequently, the current request can temporarily include the previous four messages plus the new user message. After the assistant responds, the history is trimmed back to four conversational messages.

## 5. Execution

Activate the Python virtual environment, if applicable, and run the application from the `step12` directory:

```powershell
python -m src.main
```

The application uses:

- Python
- Ollama Python library
- Ollama local server
- Qwen3 1.7B model

Type `/quit` to exit the application.

## 6. Test Prompts – Sliding Window Demonstration

Run the following prompts sequentially in the same conversation.

Do not restart the application between prompts.

### Test 1 – Initial Context

```text
Analyse Infosys as a potential value investment.
```

### Test 2 – Follow-up

```text
What are the three most important financial metrics to evaluate Infosys?
```

### Test 3 – Deeper Analysis

```text
Explain how its operating margin affects its long-term valuation.
```

### Test 4 – Follow-up

```text
What risks should an investor consider before investing in Infosys?
```

### Test 5 – Change of Subject

```text
Now analyse TCS as a potential value investment.
```

### Test 6 – Comparison

```text
Compare TCS and Infosys in terms of business quality.
```

### Test 7 – Competitive Advantage

```text
Which of these two companies appears to have stronger competitive advantages?
```

### Test 8 – Historical Context Test

```text
Going back to our original Infosys analysis, what were the key risks we discussed?
```

### What to Observe

- Only four conversational messages should remain after each completed response.
- The system instruction should always be preserved.
- Older messages should disappear as new exchanges enter.
- Input token counts should reflect the context sent for each request.
- The model may still produce plausible answers about Infosys using its general knowledge.

**Important:** This sequence demonstrates history management, but it does not conclusively prove that the model has forgotten Infosys. The model already has general knowledge about Infosys.

## 7. Stronger Experiment – Testing Actual Context Loss

To demonstrate context loss more convincingly, introduce fictional information that exists only in the conversation.

Run these prompts sequentially.

### Prompt 1 – Introduce Unique Information

```text
For this experiment, remember that our fictional company Orion has revenue of ₹850 crore and operating margin of 23%.
```

### Prompt 2 – Introduce an Unrelated Topic

```text
Now analyse TCS as a value investment.
```

### Prompt 3 – Ask About the Original Information

```text
What was the revenue and operating margin of Orion that I mentioned earlier?
```

Continue with additional unrelated exchanges if necessary so that the original Orion message falls outside the four-message window.

### Expected Observation

The model should no longer have access to the original Orion message once it has been removed from the active history.

It may fail to retrieve the figures or generate an incorrect answer.

This demonstrates an important distinction:

**A plausible answer does not necessarily mean the model remembers the original conversation.**

## 8. Understanding the Trade-off

| Advantage                                    | Limitation                                     |
| -------------------------------------------- | ---------------------------------------------- |
| Controls conversation history size           | Older information is discarded                 |
| Reduces historical context sent to the model | Long-term conversational continuity is reduced |
| Simple to implement                          | Message count does not equal token count       |
| Helps manage context-window consumption      | Important information may be lost              |

## 9. Key Takeaways

Three capabilities work together in an LLM application:

| Capability                    | Purpose                               |
| ----------------------------- | ------------------------------------- |
| Conversation State Management | Maintains conversation history        |
| Token Counting                | Measures context consumption          |
| Sliding Window                | Controls how much history is retained |

Sliding window management is a practical technique for controlling context growth, but it is not a complete memory solution.

**This limitation motivates the next step: Conversation Summarisation.**

## 10. Next Step

**Step 13 – Conversation Summarisation**

We will explore how to preserve important information from older conversation turns in a compact summary, rather than simply discarding all older messages.
