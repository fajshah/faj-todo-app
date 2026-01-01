"""
Todo In-Memory Console App
Tasks module

This module implements the business logic for task operations.
"""

from typing import List, Optional
from .models import Task
from .storage import TaskStorage


class TaskOperations:
    """
    Implements the business logic for task operations.
    """

    def __init__(self, storage: TaskStorage):
        """
        Initialize the task operations with a storage instance.

        Args:
            storage: The TaskStorage instance to use
        """
        self.storage = storage

    def add_task(self, title: str, description: str, priority: str = "medium", tags: List[str] = None) -> Optional[Task]:
        """
        Add a new task with validation.

        Args:
            title: The title of the task
            description: The description of the task
            priority: Priority level (high, medium, low)
            tags: List of tags for the task

        Returns:
            The newly created Task object, or None if validation fails
        """
        if not title.strip():
            return None

        # Validate priority
        if priority not in ["high", "medium", "low"]:
            return None

        # Initialize tags as empty list if None provided
        if tags is None:
            tags = []

        try:
            return self.storage.add_task(title, description, priority, tags)
        except Exception as e:
            print(f"Error adding task: {e}")
            return None

    def list_tasks(self) -> List[Task]:
        """
        List all tasks.

        Returns:
            A list of all Task objects
        """
        return self.storage.get_all_tasks()

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None, priority: Optional[str] = None,
                   tags: Optional[List[str]] = None) -> bool:
        """
        Update a task with validation.

        Args:
            task_id: The ID of the task to update
            title: New title (if provided)
            description: New description (if provided)
            priority: New priority (if provided)
            tags: New tags (if provided)

        Returns:
            True if the task was updated, False otherwise
        """
        # Validate priority if provided
        if priority is not None and priority not in ["high", "medium", "low"]:
            return False

        # Prepare update values
        update_title = title if title is not None and title.strip() else None
        update_desc = description if description is not None and description.strip() else None
        update_priority = priority if priority is not None else None
        update_tags = tags if tags is not None else None

        return self.storage.update_task(task_id, update_title, update_desc, update_priority, update_tags)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False otherwise
        """
        return self.storage.delete_task(task_id)

    def mark_task_complete(self, task_id: int, completed: bool) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id: The ID of the task to update
            completed: Whether the task should be marked as complete

        Returns:
            True if the task was updated, False otherwise
        """
        return self.storage.update_task(task_id, completed=completed)

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self.storage.get_task(task_id)

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description.

        Args:
            keyword: The keyword to search for

        Returns:
            A list of tasks containing the keyword
        """
        if not keyword.strip():
            return []

        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self.storage.get_all_tasks():
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, status: Optional[bool] = None, priority: Optional[str] = None,
                     tags: Optional[List[str]] = None) -> List[Task]:
        """
        Filter tasks by status, priority, and/or tags.

        Args:
            status: Filter by completion status (True for complete, False for incomplete)
            priority: Filter by priority level
            tags: Filter by tags (task must have all specified tags)

        Returns:
            A list of tasks matching the filter criteria
        """
        filtered_tasks = []

        for task in self.storage.get_all_tasks():
            # Check status filter
            if status is not None and task.completed != status:
                continue

            # Check priority filter
            if priority is not None and task.priority != priority:
                continue

            # Check tags filter
            if tags is not None:
                if not all(tag in task.tags for tag in tags):
                    continue

            filtered_tasks.append(task)

        return filtered_tasks

    def sort_tasks(self, tasks: List[Task], criteria: str) -> List[Task]:
        """
        Sort tasks by specified criteria.

        Args:
            tasks: List of tasks to sort
            criteria: Sorting criteria ('priority', 'title', 'due_date')

        Returns:
            A new list of sorted tasks
        """
        if criteria == "priority":
            # Sort by priority: high, medium, low
            priority_order = {"high": 0, "medium": 1, "low": 2}
            return sorted(tasks, key=lambda task: priority_order[task.priority])
        elif criteria == "title":
            # Sort alphabetically by title
            return sorted(tasks, key=lambda task: task.title.lower())
        elif criteria == "due_date":
            # For now, we don't have due dates, so just return as is
            # In a future implementation, this would sort by due date
            return tasks
        else:
            # Invalid criteria, return original list
            return tasks