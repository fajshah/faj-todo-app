# API Contract: Todo App – Intermediate Level Features

## Overview
This document defines the API contracts for the intermediate level features of the Todo application. Since this is a console application, these represent the method signatures and expected behaviors within the application.

## Task Model Extensions

### Task Creation with Priority and Tags
- **Method**: `add_task(title: str, description: str, priority: str = "medium", tags: List[str] = []) -> int`
- **Purpose**: Add a new task with priority and tags
- **Input**: 
  - title: Non-empty string
  - description: String (can be empty)
  - priority: One of ["high", "medium", "low"], defaults to "medium"
  - tags: List of strings, defaults to empty list
- **Output**: Task ID (positive integer)
- **Errors**: ValueError if title is empty or priority is invalid

### Task Update with Priority and Tags
- **Method**: `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None, priority: Optional[str] = None, tags: Optional[List[str]] = None) -> bool`
- **Purpose**: Update an existing task's properties including priority and tags
- **Input**: 
  - task_id: Existing task ID
  - title: New title (optional)
  - description: New description (optional)
  - priority: New priority level (optional)
  - tags: New list of tags (optional)
- **Output**: True if successful, False if task not found
- **Errors**: ValueError if priority is invalid

## Search Functionality

### Search Tasks by Keyword
- **Method**: `search_tasks(keyword: str) -> List[Task]`
- **Purpose**: Find tasks containing the keyword in title or description
- **Input**: keyword - non-empty string to search for
- **Output**: List of matching Task objects
- **Errors**: ValueError if keyword is empty

## Filter Functionality

### Filter Tasks by Criteria
- **Method**: `filter_tasks(status: Optional[bool] = None, priority: Optional[str] = None, tags: Optional[List[str]] = None) -> List[Task]`
- **Purpose**: Filter tasks based on multiple criteria
- **Input**:
  - status: Optional boolean (True for completed, False for incomplete)
  - priority: Optional priority level to filter by
  - tags: Optional list of tags to filter by (tasks must have all specified tags)
- **Output**: List of Task objects matching all specified criteria
- **Errors**: ValueError if priority is invalid

## Sort Functionality

### Sort Tasks by Criteria
- **Method**: `sort_tasks(tasks: List[Task], criteria: str) -> List[Task]`
- **Purpose**: Sort tasks according to specified criteria
- **Input**:
  - tasks: List of Task objects to sort
  - criteria: One of ["priority", "title", "due_date"]
- **Output**: New list of Task objects in sorted order
- **Errors**: ValueError if criteria is invalid

## Combined Operations

### Search, Filter, and Sort
- **Method**: `search_filter_sort(keyword: Optional[str] = None, status: Optional[bool] = None, priority: Optional[str] = None, tags: Optional[List[str]] = None, sort_by: Optional[str] = None) -> List[Task]`
- **Purpose**: Perform combined search, filter, and sort operations
- **Input**: All parameters from search, filter, and sort operations
- **Output**: List of Task objects matching criteria, sorted as requested
- **Errors**: ValueError if any parameter is invalid