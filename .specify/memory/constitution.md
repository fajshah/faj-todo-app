<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles: All principles (content update)
Added sections: None
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ reviewed
- README.md ✅ updated
Follow-up TODOs: None
-->

# Todo In-Memory Console App Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All development must follow the Spec-Kit Plus workflow: Specification → Plan → Tasks → Implementation. No code is written without an approved specification. All changes must be traced back to specific requirements in the spec. This ensures predictability, quality, and maintainability.

### II. Agentic Development Process
All code must be generated through agentic processes (Qwen Code or similar AI assistants). Manual coding by humans is strictly prohibited. This ensures consistency, adherence to standards, and documentation of the development process in prompt history records.

### III. Clean Code Standards
Code must follow clean code principles: meaningful variable and function names, small functions (ideally under 20 lines), clear separation of concerns, and well-organized modules. Code should be self-documenting with clear intent expressed through naming and structure.

### IV. Type Safety (NON-NEGOTIABLE)
All Python code must use type hints for every function signature, variable declaration, and class attribute. This ensures early error detection, better documentation, and improved IDE support. No exceptions are allowed.

### V. Proper Project Structure
The project must follow proper Python structure: `/src` folder with `__init__.py`, separate modules for different concerns (task model, storage, UI), and clear main entry point. This ensures maintainability and extensibility for future phases.

### VI. In-Memory Storage Only
The application must store all data in memory only, with no persistence to files or databases. This simplifies the implementation for Phase I while maintaining a clean architecture that can be extended in future phases.

## Technology Stack
- Python 3.13+ as the primary language
- UV as the package manager
- Python standard library only (no external dependencies)
- Console-based interactive interface
- Type hints for all code elements

## Code Quality Standards
- All functions must be small and focused (under 20 lines when possible)
- Meaningful names for all variables, functions, and classes
- Proper error handling for all user inputs and edge cases
- Comprehensive type hints throughout the codebase
- Clear separation between business logic and UI concerns
- Follow PEP 8 style guidelines
- Include docstrings for all public functions and classes

## Development Workflow Constraints
- All specifications, plans, and history must be preserved in the specs history folder
- The agent must never deviate from the approved spec and plan
- All development must be documented through Prompt History Records (PHRs)
- Prioritize simplicity and correctness over advanced features
- Use modern Python idioms (f-strings, match-case statements, dataclasses where appropriate)
- Main entry point should be runnable via `python -m src.main`

## Feature Requirements
The application must implement exactly these 5 basic features:
- Add a new task with title and description
- List/view all tasks with status indicators ([ ] Incomplete, [x] Complete) and unique IDs
- Update an existing task's title or description by ID
- Delete a task by ID
- Mark a task as complete or incomplete by ID

## Task Model Specifications
- Each task must have: id (auto-increment), title, description, completed (boolean)
- Tasks must be stored in memory using a list of dictionaries or a simple class structure
- IDs must be unique and auto-incremented
- Proper validation for all user inputs (e.g., non-empty titles)

## User Interface Requirements
- Simple text-based UI with clear prompts and status messages
- Interactive menu-driven or command-based loop
- Clear feedback for all user actions
- Proper error messages for invalid inputs or operations
- Console-based interface running in terminal

## Error Handling Standards
- Validate all user inputs (e.g., check for empty titles, invalid IDs)
- Handle edge cases gracefully (e.g., attempting to update/delete non-existent tasks)
- Provide clear, user-friendly error messages
- Never crash the application due to user input errors
- Log errors appropriately for debugging when needed

## Testing Requirements
- Unit tests for all business logic functions
- Integration tests for the main application flow
- Test error handling scenarios
- All tests must pass before any code is considered complete
- Follow TDD principles where possible

## Documentation Standards
- All public functions and classes must have docstrings
- Complex logic must be explained with inline comments
- Specifications must be comprehensive and clear
- All architectural decisions must be documented in ADRs

## Governance
This constitution supersedes all other development practices for this project. Any amendments to this constitution require explicit approval and must be documented with a clear rationale. All pull requests and code reviews must verify compliance with these principles. The development process must be traceable through the Spec-Kit Plus workflow (Specification → Plan → Tasks → Implementation).

**Version**: 1.1.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01