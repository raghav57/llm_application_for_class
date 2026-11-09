# Verify first step configuration settings

# from src.config.settings import (
#     APP_NAME,
#     OLLAMA_HOST,
#     MODEL,
#     MAX_HISTORY_MESSAGES,
#     SUMMARY_TRIGGER_MESSAGES,
#     KEEP_RECENT_MESSAGES,
#     TEMPERATURE
# )

# print("=" * 45)
# print(APP_NAME)
# print("=" * 45)

# print("Ollama Host:", OLLAMA_HOST)
# print("Model:", MODEL)
# print("Max History Messages:", MAX_HISTORY_MESSAGES)
# print("Summary Trigger:", SUMMARY_TRIGGER_MESSAGES)
# print("Keep Recent Messages:", KEEP_RECENT_MESSAGES)
# print("Temperature:", TEMPERATURE)

# print("\nConfiguration Types")
# print("MODEL:", type(MODEL).__name__)
# print("MAX_HISTORY_MESSAGES:", type(MAX_HISTORY_MESSAGES).__name__)
# print("TEMPERATURE:", type(TEMPERATURE).__name__)

# Verify system prompt step

# from pathlib import Path

# # Locate the system prompt file
# PROJECT_ROOT = Path(__file__).resolve().parent

# PROMPT_PATH = PROJECT_ROOT / "prompts" / "system_prompt.txt"

# # Read the system prompt
# with open(PROMPT_PATH, "r", encoding="utf-8") as file:
#     SYSTEM_PROMPT = file.read()

# print("=" * 50)
# print("VALUE INVESTING COPILOT")
# print("=" * 50)

# print("\nSYSTEM PROMPT LOADED SUCCESSFULLY")
# print("-" * 50)

# print(SYSTEM_PROMPT)

# print("-" * 50)
# print("Prompt characters:", len(SYSTEM_PROMPT))

#Verify pydantic schemas

# from src.schemas.stock_analysis import (
#     StockAnalysis,
#     FinancialHealth,
#     ValuationAssessment
# )

# from src.schemas.conversation import (
#     ConversationMessage,
#     ConversationState
# )


# # ----------------------------------
# # TEST 1: STOCK ANALYSIS SCHEMA
# # ----------------------------------

# financial_health = FinancialHealth(
#     profitability="Consistent profitability",
#     debt_position="Moderate debt",
#     cash_flow="Positive operating cash flow",
#     revenue_growth="Steady revenue growth"
# )

# valuation = ValuationAssessment(
#     intrinsic_value_estimate=1500.0,
#     market_price=1200.0,
#     margin_of_safety=20.0,
#     valuation_commentary="Illustrative valuation assumptions"
# )

# stock = StockAnalysis(
#     company_name="Example Technologies",
#     ticker="EXAMPLE",
#     business_overview="A fictional technology company",
#     financial_health=financial_health,
#     valuation=valuation,
#     strengths=["Strong profitability", "Positive cash flow"],
#     risks=["Competitive pressure"],
#     overall_assessment="Promising characteristics, subject to verification",
#     assessment_category="potential_value",
#     data_limitations=["Illustrative data only"]
# )

# print("\nSTOCK ANALYSIS")
# print(stock.model_dump_json(indent=2))


# # ----------------------------------
# # TEST 2: CONVERSATION SCHEMA
# # ----------------------------------

# message1 = ConversationMessage(
#     role="user",
#     content="Analyse Example Technologies"
# )

# message2 = ConversationMessage(
#     role="assistant",
#     content="Please provide verified financial data."
# )

# conversation = ConversationState(
#     messages=[message1, message2],
#     summary="The user is evaluating a fictional technology company."
# )

# print("\nCONVERSATION STATE")
# print(conversation.model_dump_json(indent=2))


# print("\nBoth schemas validated successfully!")


# Verify Ollama and LLM generation

# from src.llm.ollama_client import OllamaClient


# # Initialise Ollama client
# llm = OllamaClient()


# messages = [
#     {
#         "role": "system",
#         "content": "You are a helpful AI assistant."
#     },
#     {
#         "role": "user",
#         "content": "Explain margin of safety in value investing in three sentences."
#     }
# ]


# # --------------------------------
# # TEST 1: COMPLETE RESPONSE
# # --------------------------------

# print("\nTEST 1: COMPLETE RESPONSE")
# print("=" * 50)

# response = llm.generate(messages)

# print(response)


# # --------------------------------
# # TEST 2: STREAMING RESPONSE
# # --------------------------------

# print("\n\nTEST 2: STREAMING RESPONSE")
# print("=" * 50)

# for chunk in llm.generate_stream(messages):

#     print(chunk, end="", flush=True)

# print("\n")

# Verify response validator

# from src.services.response_validator import ResponseValidator


# validator = ResponseValidator()


# # --------------------------------
# # TEST 1: VALID RESPONSE
# # --------------------------------

# valid_response = """
# {
#     "company_name": "Example Technologies",
#     "ticker": "EXAMPLE",
#     "business_overview": "A fictional technology company",
#     "financial_health": {
#         "profitability": "Consistent profitability",
#         "debt_position": "Moderate debt",
#         "cash_flow": "Positive operating cash flow",
#         "revenue_growth": "Steady revenue growth"
#     },
#     "valuation": {
#         "intrinsic_value_estimate": 1500.0,
#         "market_price": 1200.0,
#         "margin_of_safety": 20.0,
#         "valuation_commentary": "Illustrative valuation assumptions"
#     },
#     "strengths": [
#         "Strong profitability",
#         "Positive cash flow"
#     ],
#     "risks": [
#         "Competitive pressure"
#     ],
#     "overall_assessment": "Promising characteristics, subject to verification",
#     "assessment_category": "potential_value",
#     "data_limitations": [
#         "Illustrative data only"
#     ]
# }
# """

# print("\nTEST 1: VALID RESPONSE")
# print("=" * 50)

# try:
#     result = validator.validate_stock_analysis(valid_response)

#     print("Validation successful!")
#     print(result.model_dump_json(indent=2))

# except ValueError as error:
#     print("Validation failed:", error)


# # --------------------------------
# # TEST 2: INVALID RESPONSE
# # --------------------------------

# invalid_response = """
# {
#     "company_name": "Example Technologies",
#     "business_overview": "A fictional technology company",
#     "assessment_category": "guaranteed_multibagger"
# }
# """

# print("\nTEST 2: INVALID RESPONSE")
# print("=" * 50)

# try:
#     result = validator.validate_stock_analysis(invalid_response)

#     print("Validation successful!")

# except ValueError as error:
#     print("Validation failed as expected!")
#     print(error)


# # --------------------------------
# # TEST 3: INVALID JSON
# # --------------------------------

# malformed_response = """
# {
#     "company_name": "Example Technologies",
#     "assessment_category": "potential_value"
# """

# print("\nTEST 3: MALFORMED JSON")
# print("=" * 50)

# try:
#     result = validator.validate_stock_analysis(malformed_response)

#     print("Validation successful!")

# except ValueError as error:
#     print("JSON parsing failed as expected!")
#     print(error)

# Verify Conversation Management
# from pathlib import Path

# from src.llm.ollama_client import OllamaClient
# from src.services.conversation_manager import ConversationManager


# # --------------------------------
# # LOAD SYSTEM PROMPT
# # --------------------------------

# PROJECT_ROOT = Path(__file__).resolve().parent

# PROMPT_PATH = PROJECT_ROOT / "prompts" / "system_prompt.txt"

# with open(PROMPT_PATH, "r", encoding="utf-8") as file:
#     SYSTEM_PROMPT = file.read()


# # --------------------------------
# # INITIALISE COMPONENTS
# # --------------------------------

# llm = OllamaClient()

# conversation = ConversationManager(
#     system_prompt=SYSTEM_PROMPT,
#     llm_client=llm
# )


# # --------------------------------
# # INTERACTIVE CONVERSATION
# # --------------------------------

# print("\nVALUE INVESTING COPILOT")
# print("Type 'quit' to exit.")
# print("=" * 50)

# while True:

#     user_input = input("\nYou: ")

#     if user_input.lower() == "quit":
#         break

#     # Add user message
#     conversation.add_message(
#         "user",
#         user_input
#     )

#     # Generate response using conversation context
#     messages = conversation.get_messages()

#     print("\nCopilot: ", end="", flush=True)

#     response_chunks = []

#     for chunk in llm.generate_stream(messages):

#         print(chunk, end="", flush=True)
#         response_chunks.append(chunk)

#     assistant_response = "".join(response_chunks)

#     # Add assistant response
#     conversation.add_message(
#         "assistant",
#         assistant_response
#     )

#     # Display context information
#     print("\n\n--- Conversation Status ---")

#     print(
#         "Messages retained:",
#         len(conversation.state.messages) - 1
#     )

#     if conversation.get_summary():

#         print("Summary generated: Yes")

#     else:

#         print("Summary generated: No")

# print("\nConversation ended.")

# Verify Token Counter
# from src.utils.token_counter import TokenCounter


# # Initialise token counter
# counter = TokenCounter()


# # --------------------------------
# # Simulate first LLM request
# # --------------------------------

# counter.record_usage(
#     input_tokens=250,
#     output_tokens=120
# )


# # --------------------------------
# # Simulate second LLM request
# # --------------------------------

# counter.record_usage(
#     input_tokens=380,
#     output_tokens=150
# )


# # --------------------------------
# # Simulate third LLM request
# # --------------------------------

# counter.record_usage(
#     input_tokens=420,
#     output_tokens=180
# )


# # --------------------------------
# # Display cumulative usage
# # --------------------------------

# counter.display_usage()

# Final Code 

from pathlib import Path
from unittest import result

from src.config.settings import APP_NAME
from src.llm.ollama_client import OllamaClient

from src.services.conversation_manager import ConversationManager
from src.services.response_validator import ResponseValidator

from src.utils.token_counter import TokenCounter

from src.services.scope_guard import ScopeGuard



# ==========================================
# 1. LOAD SYSTEM PROMPT
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent

PROMPT_PATH = PROJECT_ROOT / "prompts" / "system_prompt.txt"

with open(PROMPT_PATH, "r", encoding="utf-8") as file:
    SYSTEM_PROMPT = file.read()


# ==========================================
# 2. INITIALISE APPLICATION COMPONENTS
# ==========================================

llm = OllamaClient()

# Initialise token counter first
token_counter = TokenCounter()

# Pass token counter to Scope Guard
scope_guard = ScopeGuard(llm, token_counter)

conversation = ConversationManager(
    system_prompt=SYSTEM_PROMPT,
    llm_client=llm
)

validator = ResponseValidator()





# ==========================================
# 3. APPLICATION COMMANDS
# ==========================================

def display_help():


    print("\nAVAILABLE COMMANDS")
    print("-" * 45)
    print("/help       - Display available commands")
    print("/summary    - Display conversation summary")
    print("/clear      - Clear conversation history")
    print("/quit       - Exit the application")
    print("/analyze    - Generate structured stock analysis")
    print("-" * 45)




def clear_conversation():

    global conversation

    conversation = ConversationManager(
        system_prompt=SYSTEM_PROMPT,
        llm_client=llm
    )

    print("\nConversation history cleared.")



# ==========================================
# 4. DISPLAY TOKEN USAGE
# ==========================================

def display_token_usage():

    token_counter.display_usage()


# ==========================================
# 5. STREAM NORMAL LLM RESPONSE
# ==========================================


def stream_response(messages):

    print("\nCopilot: ", end="", flush=True)

    response_chunks = []

    stream = iter(
        llm.generate_stream_with_usage(messages)
    )

    try:

        while True:

            try:
                chunk = next(stream)

                print(chunk, end="", flush=True)
                response_chunks.append(chunk)

            except StopIteration as result:

                usage = result.value
                break

        print("\n")

        response_text = "".join(response_chunks)

        token_counter.record_usage(
            input_tokens=usage["input_tokens"],
            output_tokens=usage["output_tokens"]
        )

        return response_text

    except Exception:

        print("\n\n[Response interrupted due to a generation error.]")
        raise

# ==========================================
# 6. STRUCTURED STOCK ANALYSIS
# ==========================================

# def analyse_stock(user_input):

#     messages = conversation.get_messages()

#     analysis_instruction = f"""
# Analyse the company using the Value Investing Copilot system instructions.

# User's request:
# {user_input}

# Return only a valid JSON object matching the StockAnalysis schema.

# Required fields:
# - company_name
# - ticker
# - business_overview
# - financial_health
# - valuation
# - strengths
# - risks
# - overall_assessment
# - assessment_category
# - data_limitations

# For unavailable numerical values, use null.
# Do not invent financial figures.
# Use one of these assessment categories:
# potential_value, mixed_signals, potential_value_trap, insufficient_data.
# """

#     messages.append({
#         "role": "user",
#         "content": analysis_instruction
#     })

#     print("\nGenerating structured analysis...")

#     result = llm.generate_with_usage(
#         messages,
#         json_mode=True
#     )

#     token_counter.record_usage(
#         input_tokens=result["input_tokens"],
#         output_tokens=result["output_tokens"]
#     )

#     try:

#         validated_analysis = validator.validate_stock_analysis(
#             result["content"]
#         )

#         print("\nVALIDATED STOCK ANALYSIS")
#         print("=" * 50)

#         print(validated_analysis.model_dump_json(indent=2))

#         return validated_analysis.model_dump_json(indent=2)

#     except ValueError as error:

#         print("\nStructured response validation failed.")
#         print(error)

#         return (
#             "The generated analysis could not be validated. "
#             "Please try again or provide clearer financial data."
#         )

# Adding reliability to validate pydantic models and JSON responses

def analyse_stock(user_input):

    messages = conversation.get_messages()

    analysis_instruction = f"""
Analyse the company using the Value Investing Copilot system instructions.

User's request:
{user_input}

Return ONLY a valid JSON object matching the StockAnalysis Pydantic schema.

STRICT JSON STRUCTURE:

{{
    "company_name": "string",
    "ticker": "string or null",
    "business_overview": "string",

    "financial_health": {{
        "profitability": "string",
        "debt_position": "string",
        "cash_flow": "string",
        "revenue_growth": "string"
    }},

    "valuation": {{
        "intrinsic_value_estimate": "number or null",
        "market_price": "number or null",
        "margin_of_safety": "number or null",
        "valuation_commentary": "string"
    }},

    "strengths": ["string"],
    "risks": ["string"],
    "overall_assessment": "string",

    "assessment_category": "potential_value, mixed_signals, potential_value_trap, or insufficient_data",

    "data_limitations": ["string"]
}}

IMPORTANT RULES:

1. Use EXACTLY the field names shown above.
2. Do not rename, omit, or add fields.
3. financial_health and valuation MUST always be JSON objects.
4. Never use null for financial_health or valuation.
5. If information is unavailable, explain this in the relevant string fields.
6. Use null for unavailable numerical values.
7. strengths, risks and data_limitations MUST always be JSON arrays.
8. Do not invent financial figures.
9. Do not present unverified estimates as actual financial data.
10. Return valid JSON only. No Markdown or code fences.

Use one of these assessment categories:
potential_value, mixed_signals, potential_value_trap, insufficient_data.
"""

    # Prepare the complete analysis messages
    analysis_messages = messages + [
        {
            "role": "user",
            "content": analysis_instruction
        }
    ]

    print("\nGenerating structured analysis...")

    # First LLM request
    result = llm.generate_with_usage(
        analysis_messages,
        json_mode=True
    )

    # Record initial request token usage
    token_counter.record_usage(
        input_tokens=result["input_tokens"],
        output_tokens=result["output_tokens"]
    )

    print("\nRAW QWEN RESPONSE")
    print("=" * 50)
    print(result["content"])
    print("=" * 50)

    try:
        # Validate and automatically retry once if invalid
        validated_analysis = validator.validate_stock_analysis(
            result["content"])

        print("\nVALIDATED STOCK ANALYSIS")
        print("=" * 50)

        print(validated_analysis.model_dump_json(indent=2))

        return validated_analysis.model_dump_json(indent=2)

    except ValueError as error:

        print("\nStructured response validation failed.")
        print(error)

        return None



# ==========================================
# 7. MAIN APPLICATION LOOP
# ==========================================


def main():

    print("\n" + "=" * 50)
    print(APP_NAME.upper())
    print("=" * 50)

    # ----------------------------------
    # Step 16.1: Ollama startup health check
    # ----------------------------------

    is_ready, message = llm.check_connection()

    if not is_ready:

        print("\nAPPLICATION STARTUP FAILED")
        print(message)

        print(
            "\nPlease start Ollama and verify that "
            "the configured model is available."
        )

        return

    print(message)

    print("Powered by Ollama and Qwen")
    print("Type /help to see available commands.")
    print("Type /quit to exit.")

    while True:

        try:

            user_input = input("\nYou: ").strip()

            # ----------------------------------
            # Blank input handling
            # ----------------------------------

            if not user_input:

                print("Please enter a question.")
                continue

            command = user_input.lower()

            # ----------------------------------
            # Application commands
            # ----------------------------------

            if command == "/quit":

                print("\nThank you for using Value Investing Copilot.")
                break

            elif command == "/help":

                display_help()
                continue

            elif command == "/summary":

                summary = conversation.get_summary()

                if summary:

                    print("\nConversation Summary:")
                    print(summary)

                else:

                    print("\nNo conversation summary is available.")

                continue

            elif command == "/clear":

                clear_conversation()
                continue

            # ----------------------------------
            # Identify request type
            # ----------------------------------

            is_analyze_request = command.startswith("/analyze ")

            if command == "/analyze" or is_analyze_request:

                analysis_request = user_input[len("/analyze"):].strip()

                if not analysis_request:

                    print("Please provide a company or analysis request.")
                    continue

                scope_input = (
                f"Analyse the company {analysis_request} "
                    "for value investing and financial fundamentals.")

            else:

                scope_input = user_input

            # ----------------------------------
            # Step 16.4: Application Scope Validation
            # ----------------------------------

            try:

                classification = scope_guard.check(scope_input)

                if classification.category != "in_scope":

                    print(
                        "\nCopilot: I'm designed specifically for "
                        "value investing and company analysis. "
                        "Please ask me an investment-related question."
                    )

                    display_token_usage()

                    continue

            except Exception as error:

                print("\nScope validation failed.")
                print("Unable to process your request safely.")
                print(f"Details: {error}")

                continue

            # ----------------------------------
            # Structured Stock Analysis
            # ----------------------------------

            if is_analyze_request:

                try:

                    response = analyse_stock(analysis_request)

                    # Save conversation only if analysis succeeds
                    if response is None:

                        print(
                            "\nAnalysis was not saved "
                            "to conversation history."
                        )

                        display_token_usage()
                        continue

                    conversation.add_message(
                        "user",
                        analysis_request
                    )

                    conversation.add_message(
                        "assistant",
                        response
                    )

                    display_token_usage()
                    continue

                except Exception as error:

                    print("\nUnable to complete stock analysis.")
                    print(f"Details: {error}")

                    display_token_usage()
                    continue

            # ----------------------------------
            # Normal Conversation
            # ----------------------------------

            # Prepare messages without modifying stored history

            messages = conversation.get_messages() + [
                {
                    "role": "user",
                    "content": user_input
                }
            ]

            try:

                response = stream_response(messages)

                # Save messages only after successful generation

                conversation.add_message(
                    "user",
                    user_input
                )

                conversation.add_message(
                    "assistant",
                    response
                )

            except Exception as error:

                print("\nUnable to generate response.")
                print(f"Details: {error}")

            display_token_usage()

        except KeyboardInterrupt:

            print("\n\nApplication interrupted. Goodbye!")
            break

        except Exception as error:

            print("\nAn application error occurred:")
            print(error)

            print(
                "\nPlease check that Ollama is running "
                "and the configured model is available."
            )


# ==========================================
# APPLICATION ENTRY POINT
# ==========================================

if __name__ == "__main__":

    main()
