# from pydantic import ValidationError

# from src.schemas.stock_schema import StockAnalysis

# # Deliberately create invalid JSON data
# invalid_stock_json = """
# {
#     "company": {
#         "company_name": "Infosys Limited",
#         "ticker": "INFY"
#     },
#     "financials": {
#         "revenue": -5000
#     }
# }
# """


# try:
#     stock_analysis = StockAnalysis.model_validate_json(invalid_stock_json)

#     print("Validation successful!")

# except ValidationError as error:

#     print("VALIDATION FAILED:\n")

#     for issue in error.errors():
#         field = ".".join(str(part) for part in issue["loc"])
#         message = issue["msg"]

#         print(f"Field: {field}")
#         print(f"Error: {message}")
#         print("-" * 40)


import ollama
from pydantic import ValidationError

from src.schemas.stock_schema import StockAnalysis


# Initial response from the LLM (deliberately invalid for demonstration)
invalid_stock_json = """
{
    "company": {
        "company_name": "Infosys Limited",
        "ticker": "INFY"
    },
    "financials": {
        "revenue": -5000
    }
}
"""

# Generate JSON schema from Pydantic
stock_schema = StockAnalysis.model_json_schema()

try:

    # First validation attempt
    stock_analysis = StockAnalysis.model_validate_json(invalid_stock_json)

    print("Initial response is valid!")

except ValidationError as error:

    print("Initial validation failed.")
    print("Requesting LLM to correct the response...\n")

    # Convert validation errors into feedback
    error_feedback = str(error)

    # Ask the LLM to correct the original JSON
    retry_response = ollama.chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a JSON correction assistant. "
                    "Correct the supplied JSON so it satisfies "
                    "the required Pydantic schema. "
                    "Do not invent financial facts. "
                    "Return only the corrected JSON."
                )
            },
            {
                "role": "user",
                "content": f"""
                Correct this JSON:

                {invalid_stock_json}

                Validation errors:

                {error_feedback}

                Return a complete JSON object matching the schema.
                """
            }
        ],
        format=stock_schema
    )

    corrected_json = retry_response["message"]["content"]

    # Validate the corrected response
    try:
        stock_analysis = StockAnalysis.model_validate_json(corrected_json)

        print("RETRY SUCCESSFUL!")
        print("Corrected response passed Pydantic validation.")

        print(stock_analysis)
        print("\nCOMPANY:", stock_analysis.company.company_name)
        print("TICKER:", stock_analysis.company.ticker)
        print("RECOMMENDATION:", stock_analysis.verdict.recommendation)
        print("FULL VERDICT:", stock_analysis.verdict)

    except ValidationError as retry_error:

        print("Retry also failed.")
        print(retry_error)
