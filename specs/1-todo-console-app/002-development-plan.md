# Plan: Todo In-Memory Console App - Phase I Development Plan

## Overview

This document outlines the development plan for the Todo In-Memory Console App (Phase I - Basic Level). The application is a command-line todo application that stores tasks entirely in memory with support for 5 basic operations. This plan follows the Spec-Kit Plus methodology and adheres to the project constitution.

## Architecture Sketch

The application will follow a modular architecture with clear separation of concerns:

```
Main Application (main.py)
    ↓
User Interface Layer (ui.py)
    ↓
Business Logic Layer (tasks.py)
    ↓
Data Storage Layer (storage.py)
    ↓
Data Models (models.py)
```

- **models.py**: Contains the Task dataclass definition
- **storage.py**: Handles in-memory storage with auto-incrementing IDs
- **ui.py**: Manages console input/output and menu display
- **tasks.py**: Implements the business logic for task operations
- **main.py**: Orchestrates the application flow and main loop

## Project Structure

```
src/
├── __init__.py
├── models.py          # Task dataclass definition
├── storage.py         # In-memory storage implementation
├── tasks.py           # Task business logic
├── ui.py              # User interface components
└── main.py            # Main application entry point

tests/
├── __init__.py
├── test_models.py     # Unit tests for Task model
├── test_storage.py    # Unit tests for storage operations
├── test_tasks.py      # Unit tests for task operations
├── test_ui.py         # Unit tests for UI components
└── test_integration.py # Integration tests

pyproject.toml         # Project dependencies and metadata
uv.lock               # UV lock file
```

## Key Decisions

### 1. Data Model: Dataclass vs Dictionary vs Custom Class
- **Options Considered**:
  - Dictionary: Simple but lacks type safety and validation
  - Custom Class: More control but more code to maintain
  - Dataclass: Type safety, less boilerplate, clean syntax
- **Chosen Option**: Dataclass
- **Tradeoffs/Reasons**: Dataclasses provide type hints, automatic generation of special methods (init, repr), and clean syntax while maintaining readability and maintainability.

### 2. Storage Approach: List vs Dictionary vs Custom Class
- **Options Considered**:
  - Simple list: Easy to implement but requires searching for IDs
  - Dictionary with ID as key: Fast lookups but requires manual ID management
  - Custom class with list and ID counter: Encapsulates storage logic
- **Chosen Option**: Custom class with list and auto-increment ID counter
- **Tradeoffs/Reasons**: Provides encapsulation of storage logic, automatic ID management, and maintains simplicity.

### 3. UI Loop Style: Menu-driven vs Command-based vs Hybrid
- **Options Considered**:
  - Menu-driven: Numbered options, user-friendly
  - Command-based: Text commands, more flexible
  - Hybrid: Both approaches available
- **Chosen Option**: Menu-driven with numbered options
- **Tradeoffs/Reasons**: More intuitive for console applications, easier to implement, matches user expectations for this type of application.

### 4. Error Handling: Exceptions vs Return Codes vs Result Types
- **Options Considered**:
  - Exceptions: Standard Python approach, clear error propagation
  - Return codes: More explicit, requires checking
  - Result types: Functional approach, explicit success/failure
- **Chosen Option**: Exceptions for error conditions
- **Tradeoffs/Reasons**: Follows Python conventions, clear error propagation, easier to implement for this simple application.

## Implementation Phases

### Phase 1: Project Setup and Task Model
- Set up project structure with proper Python packaging
- Create the Task dataclass with id, title, description, and completed fields
- Implement basic type hints and docstrings
- Write unit tests for the Task model

### Phase 2: In-Memory Storage Implementation
- Create a TaskStorage class to manage the in-memory list
- Implement methods for adding, retrieving, updating, and deleting tasks
- Add auto-incrementing ID functionality
- Write unit tests for storage operations

### Phase 3: Console UI Components
- Create functions for displaying the main menu
- Implement functions for getting user input
- Create functions for displaying tasks in a formatted way
- Write unit tests for UI components

### Phase 4: Core Operations Implementation
- Implement functions for adding tasks with validation
- Implement functions for listing all tasks
- Implement functions for updating task details
- Implement functions for deleting tasks
- Implement functions for marking tasks as complete/incomplete
- Write unit tests for each operation

### Phase 5: Main Application Loop and Integration
- Create the main application loop with menu options
- Integrate all components together
- Implement error handling for user inputs
- Add graceful exit functionality

### Phase 6: Polish, Error Handling, and Final Testing
- Add comprehensive error handling
- Implement input validation
- Conduct integration testing
- Perform user acceptance testing
- Refine UI messages and formatting

## Task Breakdown

### Phase 1 Tasks:
- [ ] Create project structure with src/ and tests/ directories
- [ ] Create Task dataclass with type hints
- [ ] Add __init__.py files to make directories into packages
- [ ] Write unit tests for Task model
- [ ] Create pyproject.toml with project metadata

### Phase 2 Tasks:
- [ ] Create TaskStorage class with in-memory list
- [ ] Implement add_task method with auto-incrementing ID
- [ ] Implement get_task method by ID
- [ ] Implement get_all_tasks method
- [ ] Implement update_task method
- [ ] Implement delete_task method
- [ ] Write unit tests for all storage methods

### Phase 3 Tasks:
- [ ] Create display_menu function
- [ ] Create get_user_choice function
- [ ] Create display_tasks function with proper formatting
- [ ] Create input validation functions
- [ ] Write unit tests for UI components

### Phase 4 Tasks:
- [ ] Implement add_task operation with validation
- [ ] Implement list_tasks operation
- [ ] Implement update_task operation with validation
- [ ] Implement delete_task operation with validation
- [ ] Implement mark_task_complete operation
- [ ] Write unit tests for all operations

### Phase 5 Tasks:
- [ ] Create main application loop
- [ ] Integrate all components
- [ ] Implement error handling in main loop
- [ ] Add graceful exit functionality
- [ ] Test complete application flow

### Phase 6 Tasks:
- [ ] Add comprehensive error handling
- [ ] Implement additional input validation
- [ ] Conduct integration testing
- [ ] Perform user acceptance testing
- [ ] Refine UI messages and formatting

## Testing & Validation Strategy

### Unit Testing
- Each module will have corresponding test files
- Test all public methods and functions
- Test edge cases and error conditions
- Use pytest for test execution

### Integration Testing
- Test the interaction between different modules
- Validate the complete application flow
- Test error handling across module boundaries

### Acceptance Testing
- Validate against the success criteria from the specification
- Test all 5 core operations manually
- Verify performance requirements (operations complete in under 2 seconds)

## Acceptance Test Scenarios

### Scenario 1: Add and View Tasks
1. Start the application
2. Select "Add Task" option
3. Enter a title and description
4. Verify the task is added with a unique ID and shown as incomplete
5. Select "View Tasks" option
6. Verify all tasks are displayed with IDs, titles, descriptions, and completion status

### Scenario 2: Update and Delete Tasks
1. Add multiple tasks
2. Select "Update Task" option
3. Provide a valid ID and new details
4. Verify the task is updated
5. Select "Delete Task" option
6. Provide a valid ID
7. Verify the task is removed from the list

### Scenario 3: Mark Tasks Complete/Incomplete
1. Add a task
2. Select "Mark Complete" option
3. Provide the task ID
4. Verify the task's status changes to complete
5. Select "Mark Incomplete" option
6. Provide the task ID
7. Verify the task's status changes to incomplete

### Scenario 4: Error Handling
1. Try to update/delete/mark a task with an invalid ID
2. Verify appropriate error message is shown
3. Try to add a task with an empty title
4. Verify appropriate error message is shown
5. Try to mark a task as complete when there are no tasks
6. Verify appropriate error message is shown

## Risks & Mitigations

### Risk 1: Memory Usage with Large Numbers of Tasks
- **Risk**: Application performance degrades with many tasks in memory
- **Mitigation**: The specification limits to 100 tasks in memory, which is well within reasonable memory constraints

### Risk 2: Input Validation Issues
- **Risk**: Invalid inputs cause application crashes or unexpected behavior
- **Mitigation**: Implement comprehensive input validation and error handling for all user inputs

### Risk 3: ID Management Issues
- **Risk**: ID conflicts or gaps in the sequence
- **Mitigation**: Use a centralized storage class with auto-incrementing ID management

### Risk 4: User Experience Issues
- **Risk**: Confusing or non-intuitive menu system
- **Mitigation**: Design clear, simple menu options with consistent prompts and feedback

## Next Steps in Workflow

1. **Immediate Next Step**: Execute the task breakdown using `/sp.tasks` to convert this plan into specific, actionable tasks
2. **Follow-up Specifications**:
   - 003-model-spec.md: Detailed specification for the Task data model
   - 004-storage-spec.md: Detailed specification for the in-memory storage implementation
   - 005-ui-spec.md: Detailed specification for the user interface components
3. **Implementation Phase**: Begin with Phase 1 tasks to set up the project structure and Task model
4. **Quality Assurance**: Execute the testing strategy as implementation progresses
5. **Final Validation**: Perform acceptance testing against all success criteria before completion