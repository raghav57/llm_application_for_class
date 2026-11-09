# Session 11 – Step 13: Conversation Summarisation

## 1. Objective

Learn how to preserve important information from older conversations without retaining the entire conversation history.

In Step 12, we implemented a sliding window that removes older messages.

In this step, we introduce conversation summarisation.

**Core idea:** Convert older conversation messages into a compact summary and use that summary as context for future LLM requests.

## 2. Learning Outcomes

By the end of this step, students should be able to:

- Explain why conversation summarisation is useful.
- Generate summaries using an LLM.
- Maintain and update a conversation summary.
- Combine a summary with recent conversation messages.
- Preserve important information across multiple exchanges.
- Understand the limitations of summarisation-based memory.

## 3. Architecture

The application maintains two separate components:

1. **Conversation Summary:** A compact representation of important older information.
2. **Recent Messages:** The latest conversational exchanges.

When the conversation exceeds a configured threshold:

1. Older messages are selected.
2. The existing summary and older messages are sent to Qwen.
3. Qwen generates an updated summary.
4. Older messages are removed from active history.
5. Recent messages are retained.

Future LLM requests receive:

```text
System Instruction
       +
Conversation Summary
       +
Recent Messages
       +
New User Question
```

## 4. Configuration

```python
MODEL = "qwen3:1.7b"

KEEP_RECENT_MESSAGES = 4
SUMMARY_TRIGGER_MESSAGES = 6
```

- `KEEP_RECENT_MESSAGES`: Number of recent conversational messages retained.
- `SUMMARY_TRIGGER_MESSAGES`: Threshold that triggers summarisation.

The implementation uses a message-count-based trigger.

## 5. Important Implementation Logic

### 5.1 Maintain the Summary

```python
conversation_summary = ""
```

Stores the summary independently of recent conversation messages.

### 5.2 Trigger Summarisation

```python
if len(messages) - 1 > SUMMARY_TRIGGER_MESSAGES:
```

When the number of conversational messages exceeds six, summarisation begins.

### 5.3 Select Older Messages

```python
older_messages = messages[1:-KEEP_RECENT_MESSAGES]
```

Selects older conversational messages while excluding the system instruction and latest four messages.

### 5.4 Generate an Updated Summary

```python
conversation_summary = summary_response["message"]["content"]
```

Qwen generates an updated summary using:

- The previous conversation summary.
- Newly selected older messages.
- Instructions to preserve important information without inventing facts.

### 5.5 Preserve Recent Messages

```python
messages = (
    [messages[0]]
    + messages[-KEEP_RECENT_MESSAGES:]
)
```

Retains the system instruction and latest four conversational messages.

### 5.6 Use the Summary in Future Requests

```python
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
```

The summary is now included in subsequent LLM requests.

## 6. Execution

Run the application from the `step13` directory:

```powershell
python -m src.main
```

The implementation uses:

- Python
- Ollama Python library
- Ollama local server
- Qwen3 1.7B

Type `/quit` to exit.

## 7. Test Prompts – Generate and Maintain a Summary

Run these prompts sequentially in the same application session.

### Prompt 1 – Initial Analysis

```text
Analyse Infosys as a potential value investment.
```

### Prompt 2 – Investment Preferences

```text
My investment horizon is five years, and my risk appetite is moderate.
```

### Prompt 3 – Evaluation Criteria

```text
I am particularly concerned about operating margins and debt.
```

### Prompt 4 – Risk Analysis

```text
What are the biggest risks associated with Infosys?
```

### Prompt 5 – Change of Subject

```text
Compare Infosys with TCS.
```

### Prompt 6 – Competitive Advantage

```text
Which company has stronger competitive advantages?
```

### Prompt 7 – Investment Decision

```text
What should I monitor before making an investment decision?
```

### What to Observe

- Summarisation is triggered after the configured message threshold is exceeded.
- Qwen generates a compact summary.
- Older messages are removed from active history.
- The latest four conversational messages remain.
- The summary is maintained separately.

## 8. Test Prompts – Conversational Continuity

After the summary has been generated, run these prompts.

### Test 1 – Retrieve User Preferences

```text
What investment horizon and risk appetite did I previously mention?
```

### Test 2 – Retrieve Historical Concerns

```text
What were my main concerns regarding Infosys?
```

### Test 3 – Continue the Investment Analysis

```text
Considering my investment horizon and risk appetite, what factors should I prioritise before investing in Infosys?
```

### Test 4 – Introduce New Information

```text
I also prefer companies with consistent free cash flow generation. Include this in our investment preferences.
```

**Observation:** New information is not necessarily added to the summary immediately. It enters the summary when the next summarisation cycle processes the relevant older messages.

## 9. Understanding the Trade-offs

| Benefits                                  | Limitations                                 |
| ----------------------------------------- | ------------------------------------------- |
| Preserves selected historical information | Summaries can omit important details        |
| Reduces the need to retain every message  | Summarisation itself consumes tokens        |
| Supports conversational continuity        | Summary quality depends on the LLM          |
| Maintains a compact representation        | Errors can propagate across summary updates |

Important: Summarisation is not lossless. The LLM may omit facts, misunderstand information or introduce inaccuracies.

## 10. Engineering Concepts Demonstrated

| Concept                   | Purpose                                   |
| ------------------------- | ----------------------------------------- |
| Conversation State        | Maintains recent messages                 |
| Summarisation             | Compresses older messages                 |
| Incremental Summarisation | Updates an existing summary               |
| Context Assembly          | Combines summary and recent messages      |
| Conversational Continuity | Preserves selected historical information |

## 11. Implementation Limitations

This is an in-memory implementation.

- Conversation history is not saved to disk.
- The summary disappears when the application exits.
- The summary is not independently validated against the original conversation.
- The summarisation request has its own token consumption.
- A message-count threshold does not guarantee a fixed token budget.

These are deliberate simplifications for this training exercise.

## 12. Key Takeaway

**Sliding Window:** Keep recent messages and discard older ones.

**Conversation Summarisation:** Compress important older information and carry it forward.

We have now moved from basic conversation history management towards a more sophisticated memory mechanism for LLM applications.

## 13. Next Step

**Step 14 – Configuration Management**

We will explore how to manage application settings and configuration separately from application logic.
