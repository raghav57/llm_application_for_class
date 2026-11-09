# Session 11 – Step 3: Application Architecture and Separation

## 1. Project Overview

In this exercise, we transform a single-file LLM application into a modular Python application.

We separate the application into independent components, each responsible for a specific task.

Our project is a basic Value Investing Copilot powered by Qwen3 1.7B through Ollama.

## 2. Learning Objectives

- Understand Separation of Concerns.
- Organise Python applications into modules.
- Separate LLM communication from application logic.
- Maintain system prompts independently.
- Understand the purpose of data schemas.
- Connect different Python modules using imports.
- Build a modular LLM application.

## 3. Technology Stack

- Python
- Ollama
- Qwen3 1.7B
- VS Code

## 4. Project Structure

```text
step3/
│
├── src/
│   │
│   ├── llm/
│   │   └── ollama_client.py
│   │
│   ├── prompts/
│   │   └── system_prompt.py
│   │
│   ├── schemas/
│   │   └── stock_schema.py
│   │
│   ├── services/
│   │   └── investment_service.py
│   │
│   └── main.py
│
├── README.md
│
└── requirements.txt
```

## 5. Component Responsibilities

| Component             | Responsibility                                                 |
| --------------------- | -------------------------------------------------------------- |
| ollama_client.py      | Communicates with Ollama and retrieves model responses         |
| system_prompt.py      | Stores the system instructions for the Value Investing Copilot |
| stock_schema.py       | Describes the expected stock analysis structure                |
| investment_service.py | Coordinates the LLM client, prompts and application workflow   |
| main.py               | Entry point for executing the application                      |

## 6. Application Workflow

The application follows this sequence:

1. The user enters a question through main.py.
2. The InvestmentService receives the question.
3. The service combines the system prompt and user message.
4. The OllamaClient sends the request to Ollama.
5. Qwen3 1.7B generates a response.
6. The response is returned to the service.
7. main.py displays the response.

## 7. Installation

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

Ensure Ollama is running and Qwen3 1.7B is available locally.

## 8. Running the Application

Open the terminal in the project root directory.

Execute:

```bash
python -m src.main
```

Enter a question when prompted.

Example:

```text
What is value investing and why is margin of safety important?
```

## 9. Key Engineering Concepts

### Separation of Concerns

Each component has a clearly defined responsibility.

### Modularity

Different application components are maintained in separate Python files.

### Reusability

The Ollama client can be reused by other application services without rewriting the communication logic.

### Maintainability

Changes to prompts, model communication or application logic can be made independently.

## 10. Important Note About Schemas

The stock_schema.py file currently contains a basic Python dictionary describing the expected stock analysis fields.

It does not yet enforce validation.

We will introduce Pydantic models and data validation in the upcoming exercises.

## 11. Learning Outcome

We have transformed a single-file LLM script into a modular Python application.

The application now separates model communication, prompts, data structure definitions and application logic.

**Next: Step 4 – Pydantic Fundamentals: Building Data Models Using BaseModel, Types and Field.**
