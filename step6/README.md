# Step 6 – Structured Output

**Session 11:** LLM Application Engineering & Pydantic

**Project:** Value Investing Copilot

**Technologies:** Python 3.13, Ollama, Qwen3 1.7B, Pydantic

## 1. Objective

The objective of this step is to generate structured JSON responses from an LLM and convert them into Python objects using Pydantic.

We use the existing `StockAnalysis` Pydantic model developed in Step 5 to define the expected output structure.

## 2. Folder Structure

```text
step6/
│
├── src/
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── company_schema.py
│   │   ├── financial_schema.py
│   │   ├── valuation_schema.py
│   │   ├── risk_schema.py
│   │   ├── verdict_schema.py
│   │   └── stock_schema.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

## 3. Concepts Covered

### 6.1 Understanding Structured Output

- Difference between free-text and structured JSON responses.
- Why structured output is useful in LLM applications.

### 6.2 Generating JSON Schema

- Generate JSON Schema from an existing Pydantic model.
- Understand how nested models and validation constraints are represented.

```python
stock_schema = StockAnalysis.model_json_schema()
```

### 6.3 Structured Generation with Ollama

- Use Ollama's `chat()` interface.
- Pass the generated JSON Schema through the `format` parameter.
- Generate structured JSON using Qwen3 1.7B.

```python
response = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    format=stock_schema
)
```

### 6.4 Converting JSON into Pydantic Objects

- Extract the JSON response from Ollama.
- Convert the JSON string into a nested Pydantic object.

```python
stock_json = response["message"]["content"]

stock_analysis = StockAnalysis.model_validate_json(stock_json)
```

## 4. Execution

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run from the Step 6 project root:

```powershell
python -m src.main
```

## 5. Expected Outcome

The application successfully:

1. Generates a JSON Schema from `StockAnalysis`.
2. Passes the schema to Ollama.
3. Receives structured JSON from Qwen3.
4. Converts the JSON response into a Pydantic object.
5. Accesses individual nested fields.

Example:

```text
COMPANY NAME: Infosys Limited
TICKER: INFY
RECOMMENDATION: Buy

OBJECT TYPE:
<class 'src.schemas.stock_schema.StockAnalysis'>
```

## 6. Important Learning

Structured output controls the format of an LLM response, but it does not guarantee factual accuracy.

A response can follow the correct JSON structure while still containing incorrect or fabricated information.

**Key Takeaway:** Pydantic JSON Schema provides a structured contract that guides LLM output generation and makes the response easier to integrate into Python applications.

**Next Step: Step 7 – Validation and Automatic Retries**
