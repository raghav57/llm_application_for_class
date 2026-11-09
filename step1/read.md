# Session 11 – Step 1: Direct LLM API Integration

## Project Overview

This project demonstrates how to connect a Python application to a locally running Large Language Model (LLM) using Ollama.

We will use Qwen3 1.7B as our primary language model.

## Learning Objectives

- Connect Python to Ollama.
- Send prompts to a locally hosted LLM.
- Receive and display generated responses.
- Understand basic LLM API integration.

## Technology Stack

- Python
- Ollama
- Qwen3 1.7B
- VS Code

## Project Structure

```text
step1/
├── src/
│   └── main.py
├── README.md
└── requirements.txt
```

## Prerequisites

1. Python installed.
2. Ollama installed and running.
3. Qwen3 1.7B downloaded locally.
4. Ollama Python library installed.

## How to Run

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Verify the Ollama model:

```bash
ollama list
```

Run the application from the project root:

```bash
python src/main.py
```

## Expected Outcome

The Python application sends a prompt to Qwen3 1.7B through Ollama and displays the generated response in the terminal.

## Session

Session 11 – LLM Application Engineering & Pydantic

Step 1 – Direct LLM API Integration
