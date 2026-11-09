
# -----------------------------------------
# SESSION 11 - STEP 14
# CONFIGURATION MANAGEMENT
# -----------------------------------------

# Import configuration from config.py
from src.config import (
    MODEL,
    KEEP_RECENT_MESSAGES,
    SUMMARY_TRIGGER_MESSAGES
)

# -----------------------------------------
# DISPLAY APPLICATION CONFIGURATION
# -----------------------------------------

print("=" * 45)
print("VALUE INVESTING COPILOT")
print("CONFIGURATION MANAGEMENT")
print("=" * 45)

print("\nAPPLICATION CONFIGURATION")
print("-" * 45)

print("LLM Model:", MODEL)

print("Recent Messages Window:", KEEP_RECENT_MESSAGES)

print("Summary Trigger:", SUMMARY_TRIGGER_MESSAGES)

print("-" * 45)

print("\nConfiguration loaded successfully!")

# -----------------------------------------
# SIMPLE CONFIGURATION TEST
# -----------------------------------------

print("\nCONFIGURATION TYPES")

print("MODEL:", type(MODEL).__name__)

print(
    "KEEP_RECENT_MESSAGES:",
    type(KEEP_RECENT_MESSAGES).__name__
)

print(
    "SUMMARY_TRIGGER_MESSAGES:",
    type(SUMMARY_TRIGGER_MESSAGES).__name__
)

print("\nApplication ready.")
