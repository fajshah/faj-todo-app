---
id: 1
title: Create Project Constitution
stage: constitution
date_iso: 2025-01-01
surface: agent
model: Qwen Code
feature: none
branch: main
user: user
command: /sp.constitution
labels:
  - constitution
  - setup
  - todo-app
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests: []
outcome: Created comprehensive constitution for Todo In-Memory Console App
evaluation: Constitution includes all required principles and constraints
---

# Prompt History Record: Create Project Constitution

## Intent
Create a comprehensive constitution.md file for a Todo In-Memory Console App project that follows spec-driven development principles and agentic development processes.

## Original Prompt
```
As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution You are an expert Spec Architect using Spec-Kit Plus for spec-driven development of a simple Python project.

Generate a complete and professional constitution.md file for the following project.

Project Name: Todo In-Memory Console App (Phase I - Basic Level)

Project Description:
A command-line todo application that stores tasks entirely in memory (no persistence to files or databases). It must implement exactly the 5 basic features:
- Add a new task with title and description
- List/view all tasks with status indicators (e.g., [ ] Incomplete, [x] Complete) and unique IDs
- Update an existing task's title or description by ID
- Delete a task by ID
- Mark a task as complete or incomplete by ID

The application should be interactive (menu-driven or command-based loop) and run in the console.

Technology Constraints:
- Python 3.13+
- Managed with UV
- No external dependencies beyond the Python standard library
- In-memory storage only (use a list of dictionaries or a simple class)

Development Principles (Non-Negotiable - These MUST be in the constitution):
- Strictly spec-driven development using Spec-Kit Plus workflow
- No manual coding by humans; all code generated via agentic process (Qwen Code or similar)
- Follow clean code principles: meaningful names, small functions, separation of concerns
- Use type hints everywhere
- Proper Python project structure: /src folder with __init__.py, main module, separate modules if needed (e.g., task model, storage, ui)
- Code must be readable, maintainable, and extensible for future phases
- Include basic error handling (e.g., invalid ID, empty title)
- Use simple text-based UI with clear prompts and status messages
- Tasks should have: id (auto-increment), title, description, completed (bool)

Additional Rules:
- All specifications, plans, and history must be preserved in the specs history folder
- The agent must never deviate from the approved spec and plan
- Prioritize simplicity and correctness over advanced features
- Use modern Python idioms (f-strings, match-case if appropriate, dataclasses if helpful)
- The main entry point should be runnable via `python -m src.main` or similar

Output ONLY the full content of constitution.md in Markdown format.

Start with # Project Constitution

Then sections like:
- Project Overview
- Non-Negotiable Principles
- Technology Stack
- Code Quality Standards
- Workflow Constraints
- etc.

Make it comprehensive but concise (around 600-800 words).
```

## Response Summary
Successfully created a comprehensive constitution.md file for the Todo In-Memory Console App project. The constitution includes all required principles and constraints, with sections for core principles, technology stack, code quality standards, development workflow constraints, feature requirements, task model specifications, user interface requirements, error handling standards, testing requirements, and documentation standards. The constitution enforces spec-driven development, agentic development processes, type safety, clean code standards, and proper project structure.