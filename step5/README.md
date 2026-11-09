# Step 5 – Nested Pydantic Schemas

**Session 11: LLM Application Engineering & Pydantic**

**Project:** Value Investing Copilot  
**Technology:** Python 3.13, Pydantic, Ollama

---

## 1. Objective

The objective of this step is to understand how to design and implement nested Pydantic models for representing complex application data.

Instead of maintaining a single large data structure, we divide a stock analysis into smaller, reusable models and combine them into one comprehensive `StockAnalysis` model.

By the end of this step, we can represent company information, financial metrics, valuation, risks, investment recommendations and historical financial data using nested Python objects.

## 2. Folder Structure

```text
step5/
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

### 5.1 Understanding Nested Schemas

- Why complex applications require structured data models.
- Limitations of maintaining all fields in a single model.
- Introduction to nested Pydantic models.

### 5.2 Creating Independent Pydantic Models

Created individual models for different components of stock analysis:

- `CompanyInfo`
- `FinancialMetrics`
- `ValuationAnalysis`
- `RiskAnalysis`
- `InvestmentVerdict`

### 5.3 Embedding One Model Inside Another

Learned how one Pydantic model can be used as a field inside another model.

### 5.4 Creating a Complete StockAnalysis Model

Combined the individual models into a comprehensive `StockAnalysis` model.

### 5.5 Creating Nested Objects

Created individual Python objects and passed them into the parent `StockAnalysis` model.

### 5.6 Validating Nested Data

Explored how Pydantic validates nested dictionaries and objects against their respective models.

### 5.7 Handling Errors Inside Nested Models

Tested invalid values within nested objects and observed how Pydantic reports validation errors, including the nested field path.

### 5.8 Working with Lists of Nested Models

Introduced historical financial records using:

```python
historical_financials: list[FinancialMetrics] = []
```

This allows a stock analysis to contain multiple financial records.

### 5.9 Serializing Nested Models

Learned how to convert nested Pydantic objects into:

- Python dictionaries using `model_dump()`
- JSON strings using `model_dump_json()`
- Pydantic objects again using `model_validate_json()`

### 5.10 Final Schema Integration and Testing

Integrated all models into the final Value Investing Copilot schema and tested the complete structure.

## 4. Final Schema Architecture

```text
StockAnalysis
│
├── company: CompanyInfo
│   ├── company_name
│   ├── ticker
│   ├── sector
│   └── industry
│
├── financials: FinancialMetrics
│   ├── revenue
│   ├── net_profit
│   ├── total_debt
│   ├── operating_cash_flow
│   └── return_on_equity
│
├── valuation: ValuationAnalysis
│   ├── pe_ratio
│   ├── pb_ratio
│   ├── intrinsic_value
│   ├── margin_of_safety
│   └── valuation_assessment
│
├── risks: RiskAnalysis
│   ├── financial_risks
│   ├── business_risks
│   ├── governance_risks
│   └── risk_assessment
│
├── verdict: InvestmentVerdict
│   ├── recommendation
│   ├── investment_thesis
│   ├── confidence_score
│   └── investment_horizon
│
└── historical_financials: list[FinancialMetrics]
```

## 5. Pydantic Validation Rules

The implementation includes examples of field-level constraints:

| Field                     | Validation                    |
| ------------------------- | ----------------------------- |
| Revenue                   | Greater than zero             |
| Total debt                | Greater than or equal to zero |
| Ticker                    | Between 1 and 10 characters   |
| Confidence score          | Between 0 and 100             |
| Optional valuation fields | Can contain `None`            |

These constraints demonstrate how Pydantic enforces data requirements during model creation and validation.

## 6. Serialization and Deserialization

The following methods were implemented:

| Method                  | Purpose                                            |
| ----------------------- | -------------------------------------------------- |
| `model_dump()`          | Converts a Pydantic model into a Python dictionary |
| `model_dump_json()`     | Converts a Pydantic model into a JSON string       |
| `model_validate_json()` | Validates JSON and reconstructs a Pydantic object  |

This allows structured application data to be transferred, stored and reconstructed.

## 7. Installation

The project dependencies are:

```text
ollama
pydantic
```

Install them using:

```powershell
pip install -r requirements.txt
```

## 8. Running the Application

Navigate to the Step 5 project directory:

```powershell
cd D:\genai-course\session_11_steps\step5
```

Run the application from the project root:

```powershell
python -m src.main
```

## 9. Expected Outcome

The final application successfully demonstrates:

1. Creation of independent Pydantic models.
2. Composition of multiple models into a nested schema.
3. Validation of nested dictionaries and Python objects.
4. Detection of invalid nested field values.
5. Management of lists containing nested model objects.
6. Serialization into dictionaries and JSON.
7. Reconstruction of nested Pydantic objects from JSON.
8. Successful validation of the final `StockAnalysis` object.

Example final output:

```text
FINAL VALUE INVESTING COPILOT SCHEMA

Company: Infosys Limited
Ticker: INFY
Revenue: 160000.0
Net Profit: 26000.0
Valuation: Reasonably valued
Risk: Moderate risk
Recommendation: Buy
Historical Financial Records: 3

FINAL SCHEMA VALIDATION:
Valid: True
```

## 10. Key Learning

Nested Pydantic schemas provide a way to represent complex application data through smaller, reusable and independently validated models.

In the Value Investing Copilot, the `StockAnalysis` model acts as the central data structure that brings together company information, financial performance, valuation, risk analysis and investment recommendations.

**Next Step: Step 6 – Structured Output**

We will connect the existing Pydantic schema to the LLM and learn how to generate structured JSON responses that conform to the expected `StockAnalysis` structure.
