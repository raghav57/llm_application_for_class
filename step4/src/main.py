from src.schemas.stock_schema import StockAnalysis


stock = StockAnalysis(
    company_name="Tata Consultancy Services",
    # ticker=12345, For checking error#
    # ticker="",
    # ticker="ABCDEFGHIJK",
    ticker="TCS",
    business_overview="Provides IT services, consulting and business solutions.",
    financial_health="Strong balance sheet and consistent profitability.",
    # valuation="Trading at a reasonable valuation relative to earnings.",
    investment_risks="Competition, technology disruption and pricing pressure.",
    # investment_verdict="Potentially suitable for further investment research."
)

print("\nPython object:")
print(stock)

print("\nDictionary representation:")
print(stock.model_dump())

print(stock)

json_data = stock.model_dump_json()

reconstructed_stock = StockAnalysis.model_validate_json(json_data)

print("\nReconstructed Pydantic object:")
print(reconstructed_stock)


invalid_json = """
{
    "company_name": "Tata Consultancy Services",
    "ticker": 12345,
    "business_overview": "IT services",
    "financial_health": "Strong",
}
"""

try:
    invalid_stock = StockAnalysis.model_validate_json(invalid_json)
    print(invalid_stock)

except Exception as e:
    print("\nValidation failed:")
    print(e)