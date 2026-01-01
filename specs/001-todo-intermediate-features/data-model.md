# Data Model: Todo App – Intermediate Level Features

## Task Entity

### Fields
- **id**: int (auto-increment, unique, required)
  - Purpose: Unique identifier for each task
  - Constraints: Positive integer, auto-generated
- **title**: str (required)
  - Purpose: Brief description of the task
  - Constraints: Non-empty string
- **description**: str (optional)
  - Purpose: Detailed information about the task
  - Constraints: Can be empty string
- **completed**: bool (required)
  - Purpose: Status of the task completion
  - Constraints: Boolean value, defaults to False
- **priority**: str (required)
  - Purpose: Importance level of the task
  - Constraints: Must be one of ["high", "medium", "low"], defaults to "medium"
- **tags**: List[str] (optional)
  - Purpose: Categories or labels for the task
  - Constraints: List of strings, can be empty

### Validation Rules
- Title must not be empty or contain only whitespace
- Priority must be one of the allowed values: "high", "medium", "low"
- Tags must be a list of non-empty strings
- ID must be unique within the system

### State Transitions
- completed: False → True (when marking task as complete)
- completed: True → False (when marking task as incomplete)
- priority: Can be updated to any valid value
- tags: Can be added, removed, or modified

## SearchQuery Entity

### Fields
- **keyword**: str (required)
  - Purpose: Text to search for in task titles and descriptions
  - Constraints: Non-empty string

## FilterCriteria Entity

### Fields
- **status**: Optional[bool] (optional)
  - Purpose: Filter by completion status
  - Constraints: Boolean value or None (for any status)
- **priority**: Optional[str] (optional)
  - Purpose: Filter by priority level
  - Constraints: One of ["high", "medium", "low"] or None (for any priority)
- **tags**: Optional[List[str]] (optional)
  - Purpose: Filter by tags
  - Constraints: List of tag strings or None (for any tags)

## SortCriteria Entity

### Fields
- **criteria**: str (required)
  - Purpose: Determines how tasks should be sorted
  - Constraints: Must be one of ["priority", "title", "due_date"]

## Relationships
- Each Task has zero or more tags
- SearchQuery, FilterCriteria, and SortCriteria are used as parameters for operations on Task collections