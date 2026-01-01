"""
Todo In-Memory Console App
Data models module

This module defines the data structures used in the application.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Task:
    """
    Represents a single todo task.

    Attributes:
        id: Unique identifier for the task
        title: Brief title of the task
        description: Detailed description of the task
        completed: Boolean indicating if the task is completed
        priority: Priority level of the task (high, medium, low)
        tags: List of tags associated with the task
    """
    id: int
    title: str
    description: str
    completed: bool = False
    priority: str = "medium"  # Default priority is medium
    tags: List[str] = None  # Initialize as empty list if None provided

    def __post_init__(self):
        """Initialize tags as an empty list if not provided."""
        if self.tags is None:
            self.tags = []