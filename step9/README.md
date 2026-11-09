# Session 11 – Step 9: Streaming

## Objective

Understand how LLM applications progressively receive and display generated responses using streaming.

The practical implementation uses Python, Ollama and Qwen3 1.7B to compare non-streaming and streaming responses in our Value Investing Copilot.

## Folder Structure

```text
step9/
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

| Substep   | Topic                              |   Duration |
| --------- | ---------------------------------- | ---------: |
| 9.1       | Understanding Streaming            |      3 min |
| 9.2       | Implement Streaming with Ollama    |      8 min |
| 9.3       | Compare Streaming vs Non-Streaming |      4 min |
| **Total** |                                    | **15 min** |

## 9.1 – Understanding Streaming

In non-streaming generation, the application receives the complete response after the model finishes generating it.

In streaming generation, the application receives the response incrementally in smaller chunks.

### Non-Streaming Workflow

1. User submits a prompt.
2. Model generates the complete response.
3. Python receives the completed response.
4. Application displays the answer.

### Streaming Workflow

1. User submits a prompt.
2. Model starts generating.
3. Ollama delivers incremental response chunks.
4. Python consumes and displays each chunk.
5. Generation continues until completion.

Streaming improves the time at which users first see output, even when total generation time remains similar.

## 9.2 – Implement Streaming with Ollama

### Non-Streaming Implementation

```python
import ollama

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

print(response["message"]["content"])
```

### Streaming Implementation

```python
import ollama

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

for chunk in response:
    content = chunk["message"]["content"]

    print(content, end="", flush=True)

print("\n\nGeneration completed.")
```

### Important Code Concepts

| Code                          | Purpose                                |
| ----------------------------- | -------------------------------------- |
| `stream=True`                 | Requests incremental response delivery |
| `for chunk in response`       | Iterates through incoming chunks       |
| `chunk["message"]["content"]` | Extracts generated text                |
| `end=""`                      | Prevents a newline after every chunk   |
| `flush=True`                  | Immediately displays buffered output   |

**Important:** Chunks are incremental pieces of generated text. They are not necessarily individual tokens.

## 9.3 – Streaming vs Non-Streaming

Execute both implementations using the same prompt.

Observe:

- When the first output becomes visible.
- How the response is delivered.
- Whether the user waits for the complete response.
- How incremental output changes the interaction experience.

## Why Streaming Matters Beyond User Friendliness

Streaming provides several important engineering benefits.

### 1. Reduced Time to First Output

The application can display the first generated content without waiting for the entire response.

This reduces perceived latency.

### 2. Incremental Processing

Applications can process incoming chunks progressively instead of waiting for the complete response.

Potential applications include:

- Incremental text rendering.
- Progressive report generation.
- Processing generated content as it arrives.
- Building downstream processing pipelines.

### 3. Early Cancellation

Streaming applications can support stopping generation when the user no longer needs the response.

When cancellation is propagated to the model-serving layer, unnecessary generation and compute consumption can be reduced.

### 4. Better Resource Management

An application can process chunks incrementally rather than always buffering the entire response before doing anything with it.

This can reduce application-side buffering and support more efficient handling of long responses.

Actual memory and compute savings depend on implementation.

### 5. Real-Time Application Integration

Streaming supports applications that need to display or process output progressively, including:

- Conversational AI assistants.
- AI coding assistants.
- Enterprise report generation.
- Voice AI applications.
- Agentic AI interfaces.

### 6. Progressive Communication in Agentic Systems

Agentic applications can communicate intermediate updates while longer operations are running.

For example, a Value Investing Copilot could progressively report:

- Company information retrieved.
- Financial analysis underway.
- Risk assessment completed.
- Investment analysis being generated.

Note that agent progress events and LLM token streaming are separate mechanisms, although they can be combined.

## Important Engineering Considerations

Streaming introduces additional responsibilities:

- Handling incomplete responses.
- Detecting completion.
- Handling errors during generation.
- Supporting cancellation.
- Accumulating chunks when the complete response is required.

For example, if the application needs to validate a complete JSON response using Pydantic, it can accumulate the chunks and validate the completed JSON after generation.

Streaming does not replace structured output or Pydantic validation.

## Streaming Does Not Automatically Mean Faster Generation

Streaming improves time to first output and perceived responsiveness.

It does not necessarily reduce:

- Total model inference time.
- Total number of generated tokens.
- Compute consumption.
- End-to-end execution time.

These depend on the model, infrastructure and application implementation.

## Final Learning Outcome

Students understand how to implement streaming with Ollama, consume incremental response chunks, and explain why streaming is an important capability in modern LLM applications.

## Technologies Used

- Python 3.13
- Ollama
- Qwen3 1.7B

## Final Takeaway

**Streaming transforms LLM response delivery from a single completed output into a progressive interaction.**

Its value extends beyond user experience to incremental processing, cancellation, resource management and real-time application integration.
