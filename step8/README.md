# Session 11 – Step 8: API and Network Error Handling

## Objective

Learn how to handle API errors and network connection failures in Python-based LLM applications.

The practical implementation extends the Value Investing Copilot using Python, Ollama and Qwen3 1.7B.

## Folder Structure

```text
step8/
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

| Substep   | Topic                          |   Duration |
| --------- | ------------------------------ | ---------: |
| 8.1       | Why API Error Handling Matters |      2 min |
| 8.2       | Connection Error Handling      |      4 min |
| 8.3       | Handling Unexpected API Errors |      4 min |
| **Total** |                                | **10 min** |

## 8.1 – Why Error Handling Matters

An LLM application depends on communication between the Python application, the Ollama API and the language model.

Communication can fail for several reasons:

- Ollama is not running.
- The requested model is unavailable.
- The API returns an error.
- An unexpected exception occurs.

Without appropriate exception handling, these failures can terminate application execution unexpectedly.

## 8.2 – Connection Error Handling

Python's `try-except` mechanism allows the application to handle connection failures gracefully.

Example:

```python
import ollama

try:
    response = ollama.chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": "Explain value investing."
            }
        ]
    )

    print(response["message"]["content"])

except Exception as error:
    print("CONNECTION OR UNEXPECTED ERROR:")
    print(error)
```

### Practical Test

1. Execute the application while Ollama is running.
2. Confirm that the LLM generates a response.
3. Exit Ollama completely from Windows.
4. Execute the application again.
5. Observe the connection error being caught by Python.

## 8.3 – Handling Unexpected API Errors

Ollama provides `ResponseError` for errors returned by the API.

Example:

```python
except ollama.ResponseError as error:
    print("OLLAMA API ERROR:")
    print(error)
```

A broader exception handler catches other unexpected errors:

```python
except Exception as error:
    print("CONNECTION OR UNEXPECTED ERROR:")
    print(error)
```

### Practical Test

1. Ensure Ollama is running.
2. Temporarily change the requested model to `qwen3:999b
