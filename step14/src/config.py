
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read application configuration
MODEL = os.getenv("MODEL", "qwen3:1.7b")

KEEP_RECENT_MESSAGES = int(
    os.getenv("KEEP_RECENT_MESSAGES", "4")
)

SUMMARY_TRIGGER_MESSAGES = int(
    os.getenv("SUMMARY_TRIGGER_MESSAGES", "6")
)
