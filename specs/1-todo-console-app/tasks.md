# Tasks: Todo In-Memory Console App - Phase I

## Feature Overview

This document outlines the actionable, dependency-ordered tasks for implementing the Todo In-Memory Console App (Phase I - Basic Level). The application is a command-line todo application that stores tasks entirely in memory with support for 5 basic operations.

## Dependencies

- User Story 2 (Update and Delete Tasks) depends on User Story 1 (Add and View Tasks) being partially complete (at least the ability to add tasks)
- User Story 3 (Mark Tasks Complete/Incomplete) depends on User Story 1 (Add and View Tasks) being partially complete (at least the ability to add tasks)

## Parallel Execution Examples

- Task creation and UI display can be developed in parallel after the foundational Task model is established
- Storage implementation can proceed in parallel with UI component development
- Each user story's operations can be tested independently once the foundational components are in place

## Implementation Strategy

- MVP: Implement User Story 1 (Add and View Tasks) completely to deliver basic value
- Incremental delivery: Add each subsequent user story in priority order
- Each phase delivers independently testable functionality

## Phase 1: Setup

### Goal
Set up the basic project structure and foundational components.

### Tasks
- [X] T001 Create project structure with src/ and tests/ directories
- [X] T002 Create Task dataclass with type hints in src/models.py
- [X] T003 Add __init__.py files to make directories into packages
- [X] T004 Create pyproject.toml with project metadata
- [X] T005 [P] Write unit tests for Task model in tests/test_models.py

## Phase 2: Foundational Components

### Goal
Implement the core data storage and business logic components that will be used by all user stories.

### Tasks
- [X] T006 Create TaskStorage class with in-memory list in src/storage.py
- [X] T007 Implement add_task method with auto-incrementing ID in src/storage.py
- [X] T008 Implement get_task method by ID in src/storage.py
- [X] T009 Implement get_all_tasks method in src/storage.py
- [X] T010 Implement update_task method in src/storage.py
- [X] T011 Implement delete_task method in src/storage.py
- [X] T012 [P] Write unit tests for all storage methods in tests/test_storage.py
- [X] T013 Create TaskOperations class in src/tasks.py
- [X] T014 Implement add_task operation with validation in src/tasks.py
- [X] T015 Implement list_tasks operation in src/tasks.py
- [X] T016 [P] Write unit tests for task operations in tests/test_tasks.py

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1)

### Goal
Enable users to add tasks with a title and description and view all their tasks.

### Independent Test Criteria
Can be fully tested by adding multiple tasks and viewing them. Delivers the basic value of task tracking.

### Tasks
- [X] T017 [US1] Create display_menu function in src/ui.py
- [X] T018 [US1] Create get_user_choice function in src/ui.py
- [X] T019 [US1] Create display_tasks function with proper formatting in src/ui.py
- [X] T020 [P] [US1] Write unit tests for UI components in tests/test_ui.py
- [X] T021 [US1] Implement add_task operation with validation in src/tasks.py
- [X] T022 [US1] Implement list_tasks operation in src/tasks.py
- [X] T023 [US1] Create get_task_input function in src/ui.py
- [X] T024 [US1] Integrate add task functionality in main application loop in src/main.py
- [X] T025 [US1] Integrate view tasks functionality in main application loop in src/main.py
- [X] T026 [US1] Test acceptance scenario 1: Add and view tasks

## Phase 4: User Story 2 - Update and Delete Tasks (Priority: P2)

### Goal
Enable users to update or delete their tasks so that they can modify or remove tasks that are no longer relevant.

### Independent Test Criteria
Can be tested by adding tasks, updating their details, and deleting some of them.

### Tasks
- [X] T027 [US2] Implement update_task operation with validation in src/tasks.py
- [X] T028 [US2] Implement delete_task operation with validation in src/tasks.py
- [X] T029 [US2] Create get_task_id function in src/ui.py
- [X] T030 [US2] Integrate update task functionality in main application loop in src/main.py
- [X] T031 [US2] Integrate delete task functionality in main application loop in src/main.py
- [X] T032 [US2] Test acceptance scenario 2: Update and delete tasks

## Phase 5: User Story 3 - Mark Tasks Complete/Incomplete (Priority: P3)

### Goal
Enable users to mark tasks as complete or incomplete so that they can track their progress.

### Independent Test Criteria
Can be tested by marking tasks as complete/incomplete and verifying the status updates.

### Tasks
- [X] T033 [US3] Implement mark_task_complete operation in src/tasks.py
- [X] T034 [US3] Create get_completion_status function in src/ui.py
- [X] T035 [US3] Integrate mark complete/incomplete functionality in main application loop in src/main.py
- [X] T036 [US3] Test acceptance scenario 3: Mark tasks complete/incomplete

## Phase 6: Error Handling and Edge Cases

### Goal
Implement comprehensive error handling and address edge cases identified in the specification.

### Tasks
- [X] T037 [P] Add error handling for invalid task IDs in src/tasks.py
- [X] T038 [P] Add validation for empty titles when adding/updating tasks in src/tasks.py
- [X] T039 [P] Handle case when trying to mark a task as complete when no tasks exist in src/tasks.py
- [X] T040 [P] Handle very long descriptions that might affect display in src/ui.py
- [X] T041 [P] Add comprehensive error messages for all operations in src/ui.py
- [X] T042 [P] Test acceptance scenario 4: Error handling

## Phase 7: Polish & Cross-Cutting Concerns

### Goal
Finalize the application with proper integration, testing, and documentation.

### Tasks
- [X] T043 Create main application loop with menu options in src/main.py
- [X] T044 Integrate all components together in src/main.py
- [X] T045 Implement error handling in main loop in src/main.py
- [X] T046 Add graceful exit functionality in src/main.py
- [X] T047 Test complete application flow
- [X] T048 Conduct integration testing
- [X] T049 Perform user acceptance testing
- [X] T050 Refine UI messages and formatting
- [X] T051 Write integration tests in tests/test_integration.py
- [X] T052 Update README.md with usage instructions