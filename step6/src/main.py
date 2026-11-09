import ollama
from src.schemas.stock_schema import StockAnalysis

# Generate JSON Schema
stock_schema = StockAnalysis.model_json_schema()

# Display the schema
print("\nGENERATED JSON SCHEMA:\n")
print(stock_schema)

# -----------------------------------------
# STEP 6.3 - Structured Output with Ollama
# -----------------------------------------

prompt = """
You are a value investing analyst.

Analyse Infosys Limited using the financial information provided.

Generate a complete stock analysis including:
- Company information
- Financial metrics
- Valuation analysis
- Financial, business and governance risks
- Investment verdict
- Historical financial information

Use only the supplied financial data.
Do not invent financial figures.
Return the response in the required JSON structure.
"""

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

# print("\nSTRUCTURED LLM RESPONSE:\n")
# print(response["message"]["content"])


# -----------------------------------------
# STEP 6.4 - Convert JSON to Pydantic Object
# -----------------------------------------

stock_json = response["message"]["content"]

stock_analysis = StockAnalysis.model_validate_json(stock_json)

print("\nPYDANTIC STOCK ANALYSIS OBJECT:\n")
print(stock_analysis)

print("\nCOMPANY NAME:", stock_analysis.company.company_name)
print("TICKER:", stock_analysis.company.ticker)
print("RECOMMENDATION:", stock_analysis.verdict.recommendation)

print("\nOBJECT TYPE:")
print(type(stock_analysis))
