# Quickstart Guide: Todo App – Intermediate Level Features

## Overview
This guide will help you get started with the enhanced Todo app that includes priority levels, tags, search, filter, and sort functionality.

## Prerequisites
- Python 3.13+
- No external dependencies required (pure Python standard library)

## Running the Application
1. Navigate to the project root directory
2. Execute: `python -m src.main`
3. The console application will start with the main menu

## New Features

### 1. Task Priorities
- When adding or updating tasks, you can now assign a priority level: high, medium, or low
- High priority tasks are displayed first when sorted by priority
- Priority helps organize tasks by importance

### 2. Task Tags
- Assign one or more tags to tasks for categorization (e.g., work, personal, urgent)
- Tags can be added during task creation or updated later
- Use tags for filtering and organizing tasks

### 3. Search Tasks
- Use the search feature to find tasks by keyword in title or description
- Search is case-insensitive and finds partial matches
- Access search from the main menu

### 4. Filter Tasks
- Filter tasks by status (complete/incomplete), priority, or tags
- Combine multiple filters (e.g., show incomplete high-priority work tasks)
- Filtering helps focus on specific subsets of tasks

### 5. Sort Tasks
- Sort tasks by priority (high to low), title (alphabetically), or due date
- Sorting helps organize your task list according to your preference
- Access sorting from the view tasks menu

## Usage Examples

### Adding a Task with Priority and Tags
1. Select "Add Task" from the main menu
2. Enter the task title and description
3. Choose a priority level (high, medium, low)
4. Enter tags separated by commas (e.g., "work, urgent, project-x")

### Searching for Tasks
1. Select "Search Tasks" from the main menu
2. Enter a keyword to search in titles and descriptions
3. The matching tasks will be displayed

### Filtering Tasks
1. Select "Filter Tasks" from the main menu
2. Choose filter criteria (status, priority, tags)
3. The filtered tasks will be displayed

### Sorting Tasks
1. Select "View Tasks" from the main menu
2. Choose "Sort Tasks" option
3. Select the sorting criteria (priority, title, due date)
4. The tasks will be displayed in the sorted order

## Best Practices
- Use meaningful tags to categorize your tasks effectively
- Set appropriate priority levels to focus on important tasks
- Regularly search and filter to find specific tasks quickly
- Use sorting to organize your task list according to your workflow