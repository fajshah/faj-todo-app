# Todo In-Memory Console App

A simple, interactive command-line Todo application that stores tasks in memory and supports the 5 basic operations plus advanced organization features.

## Features

- Add a new task with title and description
- List/view all tasks with status indicators ([ ] Incomplete, [x] Complete) and unique IDs
- Update an existing task's title or description by ID
- Delete a task by ID
- Mark a task as complete or incomplete by ID
- **NEW**: Assign priority levels (high, medium, low) to tasks
- **NEW**: Add tags to tasks for categorization
- **NEW**: Search tasks by keyword in title or description
- **NEW**: Filter tasks by status, priority, or tags
- **NEW**: Sort tasks by priority, title, or due date

## Requirements

- Python 3.13+
- UV package manager (optional, for dependency management)

## Project Structure

```
src/
├── __init__.py
├── models.py          # Task dataclass definition with priority and tags
├── storage.py         # In-memory storage implementation
├── tasks.py           # Task business logic with search, filter, sort
├── ui.py              # User interface components
└── main.py            # Main application entry point
```

## How to Run

To run the application, execute:

```bash
python -m src.main
```

## Architecture

The application follows a modular architecture with clear separation of concerns:

- **models.py**: Contains the Task dataclass definition with priority and tags
- **storage.py**: Handles in-memory storage with auto-incrementing IDs
- **ui.py**: Manages console input/output and menu display
- **tasks.py**: Implements the business logic for task operations including search, filter, and sort
- **main.py**: Orchestrates the application flow and main loop

## Design Decisions

- **Data Model**: Used a dataclass for the Task model to provide type hints, automatic generation of special methods, and clean syntax
- **Storage Approach**: Implemented a custom class with a list and auto-incrementing ID counter for encapsulation of storage logic
- **UI Style**: Implemented a menu-driven interface with numbered options for user-friendliness
- **Error Handling**: Used exceptions for error conditions following Python conventions
- **Extensibility**: Designed with extension points for priority, tags, search, filter, and sort functionality