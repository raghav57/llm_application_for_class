# Session 11: LLM Application Engineering & Pydantic

### Building a Value Investing Copilot with Python, Ollama and Qwen

An end-to-end hands-on project demonstrating how to transform a locally hosted Large Language Model (LLM) into a structured, conversational and more reliable AI application.

This project is part of a practical AI Engineering course focused on building real-world applications rather than simply interacting with language models.

---

## 1. Project Overview

Large Language Models can generate impressive responses, but building a dependable AI application requires much more than connecting to an LLM.

This project develops a **Value Investing Copilot** using Python, Ollama and Qwen3. It demonstrates how application engineering components work together to manage conversations, validate structured responses, control application scope and handle model interactions.

The application is designed to help users explore value investing concepts and analyse companies through structured financial assessments.

## 2. Technology Stack

| Technology    | Purpose                       |
| ------------- | ----------------------------- |
| Python 3.13   | Application development       |
| Ollama        | Local LLM runtime             |
| Qwen3 1.7B    | Language model                |
| Pydantic      | Data modelling and validation |
| python-dotenv | Configuration management      |
| JSON Mode     | Structured LLM responses      |
| VS Code       | Development environment       |

## 3. Key Capabilities

### LLM Integration

- Connect Python applications to locally hosted LLMs.
- Manage system and user message roles.
- Generate responses using Ollama and Qwen3.

### Application Architecture

- Separate LLM clients, prompts, schemas, services and utilities.
- Organise application logic into reusable components.

### Structured Output and Validation

- Define data structures using Pydantic.
- Validate LLM-generated JSON responses.
- Handle malformed or invalid structured responses.

### Conversation Management

- Maintain conversational state.
- Track conversation history.
- Implement sliding-window context management.
- Summarise older conversations while retaining recent messages.

### Streaming and Token Accounting

- Stream model responses.
- Track input and output token usage.
- Monitor cumulative application usage.

### Scope Guard

- Classify incoming requests as in-scope or out-of-scope.
- Keep the application focused on value investing and financial analysis.

### Reliability Improvements

- Handle Ollama connectivity failures.
- Protect conversation state from unsuccessful operations.
- Validate structured stock analysis.
- Manage application configuration through environment variables.

---

## 4. Project Structure

The repository is organised into individual learning steps.

```text
session_11_steps/
│
├── .gitignore
├── README.md
│
├── step1/
├── step2/
├── step3/
├── ...
├── step14/
│
└── step15/
    ├── .env.example
    ├── requirements.txt
    │
    └── src/
        ├── main.py
        │
        ├── config/
        │   └── settings.py
        │
        ├── llm/
        │   └── ollama_client.py
        │
        ├── prompts/
        │   └── system_prompt.txt
        │
        ├── schemas/
        │   ├── conversation.py
        │   └── stock_analysis.py
        │
        ├── services/
        │   ├── conversation_manager.py
        │   └── response_validator.py
        │
        └── utils/
            └── token_counter.py
```

The individual step folders contain the progressive learning exercises. Step 15 contains the integrated application.

---

## 5. Getting Started

### Prerequisites

Install the following:

- Python 3.13
- Git
- Ollama
- Visual Studio Code (recommended)

### Step 1: Clone the repository

```bash
git clone https://github.com/raghav57/llm_application_for_class.git
```

Navigate to the project:

```bash
cd llm_application_for_class
```

### Step 2: Download the LLM

Install Ollama and download the Qwen3 model:

```bash
ollama pull qwen3:1.7b
```

Ensure Ollama is running before starting the application.

### Step 3: Navigate to the integrated application

```bash
cd step15
```

### Step 4: Create a virtual environment

```powershell
py -3.13 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure environment variables

Create your local `.env` file using the provided template:

```powershell
Copy-Item .env.example .env
```

Review the configuration if required.

### Step 7: Run the application

From the `step15` directory:

```bash
python -m src.main
```

The application checks the Ollama connection before starting.

---

## 6. Application Commands

Once the application starts, the following commands are available:

| Command              | Description                          |
| -------------------- | ------------------------------------ |
| `/help`              | Display available commands           |
| `/analyze <company>` | Generate structured company analysis |
| `/summary`           | Display conversation summary         |
| `/clear`             | Clear conversation history           |
| `/quit`              | Exit the application                 |

You can also ask general questions related to value investing and financial fundamentals.

---

## 7. Example Usage

```text
Value Investing Copilot

> Explain free cash flow.

> Why is free cash flow important when evaluating a company?

> What is the difference between intrinsic value and market price?

> /analyze TCS
```

The stock analysis produces a structured response containing:

- Company overview
- Financial health
- Valuation assessment
- Strengths
- Risks
- Overall assessment
- Data limitations

---

## 8. Important Design Considerations

This project demonstrates an important distinction:

**A valid LLM response is not necessarily a factually correct response.**

Pydantic validates the structure and types of generated information. It does not independently verify financial facts.

The application does not currently integrate a live financial data provider. Therefore, generated company assessments may have incomplete information or limitations.

Always verify financial information against reliable sources before making investment decisions.

This application is an educational engineering project, not financial advice.

---

## 9. Learning Outcomes

By completing this project, learners gain practical experience in:

1. Integrating locally hosted LLMs with Python.
2. Designing modular LLM applications.
3. Building structured data models using Pydantic.
4. Managing JSON responses and validation.
5. Implementing conversational memory.
6. Managing context windows and conversation summaries.
7. Streaming LLM responses.
8. Tracking token consumption.
9. Building application-level scope controls.
10. Improving the reliability of LLM-powered applications.

---

## 10. Project Philosophy

Building an LLM application is not simply about choosing a powerful model.

It requires thoughtful engineering around the model:

- Structured inputs and outputs.
- Application architecture.
- Context management.
- Validation.
- Error handling.
- Reliability.
- Responsible use of generated information.

**Reliable AI = Model Intelligence + Application Engineering**

---

_Part of a hands-on AI Engineering learning journey. Built using Python, Ollama, Qwen3 and Pydantic._
