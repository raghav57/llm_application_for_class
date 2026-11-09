# Session 11 – Step 14: Configuration Management

**Duration:** 10 minutes  
**Phase:** LLM Application Engineering & Pydantic  
**Project:** Value Investing Copilot

## 1. Learning Objective

Understand how to separate application configuration from application logic using environment variables and `.env` files.

By the end of this step, you will be able to:

- Understand why hardcoded configuration is undesirable.
- Store configuration outside Python source code.
- Load environment variables using `python-dotenv`.
- Read configuration using Python's `os.getenv()`.
- Convert environment variables into appropriate Python data types.
- Define default values when configuration is missing.
- Demonstrate that application behaviour can be configured without changing Python code.

## 2. Project Structure

Create the following structure inside the `step14` folder:

```text
step14/
│
├── .env
├── requirements.txt
│
└── src/
    ├── __init__.py
    ├── config.py
    └── main.py
```

The purpose of each file:

| File               | Responsibility                         |
| ------------------ | -------------------------------------- |
| `.env`             | Stores application configuration       |
| `requirements.txt` | Lists Python dependencies              |
| `config.py`        | Loads and exposes configuration        |
| `main.py`          | Demonstrates application configuration |

## 3. Step 14.1 – Understanding Configuration Management

**Problem: Hardcoded configuration**

Consider the following Python code:

```python
MODEL = "qwen3:1.7b"
KEEP_RECENT_MESSAGES = 4
SUMMARY_TRIGGER_MESSAGES = 6
```

These values are embedded directly in the application.

If we want to change the model or conversation settings, we must modify the Python code.

**Solution: External configuration**

Move these values outside the application and load them when the application starts.

This separates configuration from application logic.

## 4. Step 14.2 – Environment Variables and `.env`

### Install the required package

Run:

```powershell
python -m pip install python-dotenv
```

### Create `requirements.txt`

```text
ollama
pydantic
python-dotenv
```

### Create `.env`

```env
MODEL=qwen3:1.7b
KEEP_RECENT_MESSAGES=4
SUMMARY_TRIGGER_MESSAGES=6
```

**Important concepts:**

- Environment variables store configuration outside Python code.
- `python-dotenv` loads values from the `.env` file.
- `os.getenv()` reads environment variables.
- Environment variable values are read as strings.
- Numeric configuration values must be converted into integers.

## 5. Step 14.3 – Implement Configuration Using Python

### Create `src/config.py`

```python
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
```

### Understanding the implementation

| Code            | Purpose                           |
| --------------- | --------------------------------- |
| `load_dotenv()` | Loads values from `.env`          |
| `os.getenv()`   | Reads an environment variable     |
| `"qwen3:1.7b"`  | Default model if MODEL is missing |
| `int()`         | Converts a string into an integer |

The application can now access configuration through a separate Python module.

### Create `src/main.py`

```python
# SESSION 11 - STEP 14 CONFIGURATION MANAGEMENT

from src.config import (
    MODEL,
    KEEP_RECENT_MESSAGES,
    SUMMARY_TRIGGER_MESSAGES
)

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
```

## 6. Step 14.4 – Testing Configuration Management

Run the application from the `step14` directory:

```powershell
python -m src.main
```

### Test 1 – Load the default configuration

Keep the original `.env` file:

```env
MODEL=qwen3:1.7b
KEEP_RECENT_MESSAGES=4
SUMMARY_TRIGGER_MESSAGES=6
```

Expected output:

```text
LLM Model: qwen3:1.7b
Recent Messages Window: 4
Summary Trigger: 6

MODEL: str
KEEP_RECENT_MESSAGES: int
SUMMARY_TRIGGER_MESSAGES: int
```

**What this demonstrates:** The application successfully loads configuration and converts numeric values into integers.

### Test 2 – Change configuration without modifying Python code

Modify `.env`:

```env
MODEL=qwen3:8b
KEEP_RECENT_MESSAGES=8
SUMMARY_TRIGGER_MESSAGES=12
```

Run the application again:

```powershell
python -m src.main
```

Expected output:

```text
LLM Model: qwen3:8b
Recent Messages Window: 8
Summary Trigger: 12
```

**What this demonstrates:** Configuration can be changed without modifying `main.py` or `config.py`.

Note: This is only a configuration demonstration. The application does not load or execute the Qwen3 8B model.

### Test 3 – Test default fallback values

Remove the `MODEL` entry from `.env`.

The file should now contain:

```env
KEEP_RECENT_MESSAGES=5
SUMMARY_TRIGGER_MESSAGES=10
```

Run the application again:

```powershell
python -m src.main
```

Expected output:

```text
LLM Model: qwen3:1.7b
Recent Messages Window: 5
Summary Trigger: 10
```

**What this demonstrates:** When an environment variable is missing, `os.getenv()` uses the default value defined in `config.py`.

### Restore the original configuration

After testing, restore `.env`:

```env
MODEL=qwen3:1.7b
KEEP_RECENT_MESSAGES=4
SUMMARY_TRIGGER_MESSAGES=6
```

## 7. Key Takeaways

1. Configuration should be separated from application logic.
2. Environment variables make applications easier to configure across environments.
3. `.env` files provide a convenient local development approach.
4. `os.getenv()` supports default values.
5. Environment variables are strings and may need type conversion.
6. Configuration changes should not require changes to application code.

**Security note:** Do not commit `.env` files containing secrets to source control. Add `.env` to `.gitignore`. For production deployments, use securely managed environment variables or a secrets manager.

## 8. What We Have Built

A small, modular configuration layer:

```text
.env
  │
  ▼
python-dotenv
  │
  ▼
config.py
  │
  ▼
main.py
  │
  ▼
Application Configuration
```

This step deliberately focuses on configuration management rather than rebuilding the complete Value Investing Copilot.

In Step 15 – Application Integration, we will bring the components developed throughout Session 11 together into a more complete application.

---

**Step 14 Complete: Configuration Management**

The application now reads configuration independently of its Python business logic.
