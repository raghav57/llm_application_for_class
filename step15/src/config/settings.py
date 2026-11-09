import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Application configuration
APP_NAME = os.getenv(
    "APP_NAME",
    "Value Investing Copilot"
)

# Ollama configuration
OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434"
)

MODEL = os.getenv(
    "MODEL",
    "qwen3:1.7b"
)

# Conversation configuration
MAX_HISTORY_MESSAGES = int(
    os.getenv("MAX_HISTORY_MESSAGES", "4")
)

SUMMARY_TRIGGER_MESSAGES = int(
    os.getenv("SUMMARY_TRIGGER_MESSAGES", "6")
)

KEEP_RECENT_MESSAGES = int(
    os.getenv("KEEP_RECENT_MESSAGES", "4")
)

# Generation configuration
TEMPERATURE = float(
    os.getenv("TEMPERATURE", "0.3")
)