"""
Todo In-Memory Console App
Storage module

This module handles in-memory storage of tasks with auto-incrementing IDs.
"""

from typing import List, Optional
from .models import Task


class TaskStorage:
    """
    Manages in-memory storage of tasks with auto-incrementing IDs.
    """

    def __init__(self):
        """Initialize the storage with an empty list of tasks and ID counter."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str, priority: str = "medium", tags: List[str] = None) -> Task:
        """
        Add a new task with the given title, description, priority, and tags.

        Args:
            title: The title of the task
            description: The description of the task
            priority: Priority level (high, medium, low)
            tags: List of tags for the task

        Returns:
            The newly created Task object
        """
        if tags is None:
            tags = []

        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            completed=False,
            priority=priority,
            tags=tags
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks.

        Returns:
            A list of all Task objects
        """
        return self._tasks.copy()

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None,
                   completed: Optional[bool] = None,
                   priority: Optional[str] = None,
                   tags: Optional[List[str]] = None) -> bool:
        """
        Update a task with the given ID.

        Args:
            task_id: The ID of the task to update
            title: New title (if provided)
            description: New description (if provided)
            completed: New completion status (if provided)
            priority: New priority (if provided)
            tags: New tags (if provided)

        Returns:
            True if the task was updated, False if not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed
        if priority is not None:
            task.priority = priority
        if tags is not None:
            task.tags = tags

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True