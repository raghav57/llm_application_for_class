# Session 11 – Step 11: Token Counting

## Objective

Understand how LLMs process text as tokens, how conversation history consumes tokens, and how to inspect token usage in an LLM application.

The practical implementation extends the Value Investing Copilot using Python, Ollama and Qwen3 1.7B.

## Folder Structure

```text
step11/
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

| Substep   | Topic                                   |  Duration |
| --------- | --------------------------------------- | --------: |
| 11.1      | Understanding Tokens and Token Counting |     3 min |
| 11.2      | Count Tokens in Conversation History    |     3 min |
| 11.3      | Observe Context Growth                  |     2 min |
| **Total** |                                         | **8 min** |

## 11.1 – Understanding Tokens

Tokens are the units of text processed by an LLM.

Important concepts:

- Tokens are not necessarily equivalent to words.
- A word can consist of one or multiple tokens.
- Punctuation and spaces also influence tokenization.
- The model processes tokenized input rather than ordinary words.
- Conversation history consumes context-window capacity.

## 11.2 – Count Tokens Using Ollama

Ollama provides token usage metadata as part of its response.

Two important fields are:

| Field               | Description                       |
| ------------------- | --------------------------------- |
| `prompt_eval_count` | Number of input tokens processed  |
| `eval_count`        | Number of output tokens generated |

### Implementation

```python
response = ollama.chat(
    model="qwen3:1.7b",
    messages=messages
)

prompt_tokens = response["prompt_eval_count"]
generated_tokens = response["eval_count"]

print("Input tokens:", prompt_tokens)
print("Generated tokens:", generated_tokens)
print("Total tokens:", prompt_tokens + generated_tokens)
```

### Understanding the Results

- Input tokens represent the prompt and conversation history processed for that request.
- Generated tokens represent the assistant's output.
- Total tokens represent the combined input and output token usage for that request.

Ollama provides these counts after the generation request completes.

No additional tokenizer library or Hugging Face dependency is required.

## 11.3 – Observe Context Growth

Run the continuous conversation application and ask:

1. Analyse Infosys.
2. What about its debt?
3. What are its major risks?

Observe the input token count after each response.

As conversation history grows, the input token count generally increases because previous messages are included in subsequent requests.

### Important Observation

Token counts shown by Ollama are per-request measurements, not cumulative conversation totals.

Each new request processes the conversation history supplied to it again.

## Why Token Counting Matters

Token counting helps developers:

- Understand input and output token consumption.
- Monitor context-window usage.
- Estimate API usage and costs in hosted environments.
- Identify growing conversation histories.
- Understand potential inference latency and resource requirements.
- Decide when context management strategies are necessary.

Actual cost and resource consumption depend on the model, infrastructure and provider.

## Important Engineering Distinction

**Token Counting ≠ Context Management**

Token counting measures token usage.

Context management controls how much conversation history is retained and sent to the model.

## Connection to Subsequent Steps

| Step | Topic                             | Purpose                             |
| ---- | --------------------------------- | ----------------------------------- |
| 10   | Conversation State Management     | Maintain conversation history       |
| 11   | Token Counting                    | Measure token consumption           |
| 12   | Sliding Window Context Management | Retain recent conversation history  |
| 13   | Conversation Summarisation        | Compress older conversation context |

## Final Learning Outcome

Students understand token usage in LLM applications and learn how to inspect input and output token counts using Ollama response metadata.

## Technologies Used

- Python 3.13
- Ollama
- Qwen3 1.7B

## Final Takeaway

**You cannot manage context intelligently without understanding how much context your application is consuming.**
