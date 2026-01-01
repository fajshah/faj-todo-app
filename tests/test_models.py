"""
Todo In-Memory Console App
Unit tests for Task model

This module tests the Task dataclass functionality.
"""

from src.models import Task


def test_task_creation():
    """Test creating a Task instance."""
    task = Task(id=1, title="Test Task", description="Test Description")

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False  # Default value
    print("OK Task creation test passed")


def test_task_creation_with_completed_status():
    """Test creating a Task instance with completed status."""
    task = Task(id=1, title="Test Task", description="Test Description", completed=True)

    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is True
    print("OK Task creation with completed status test passed")


def test_task_repr():
    """Test the string representation of a Task."""
    task = Task(id=1, title="Test Task", description="Test Description")

    # Since dataclass automatically generates __repr__, we just verify it exists and is reasonable
    repr_str = repr(task)
    assert "Task" in repr_str
    assert "id=1" in repr_str
    assert "title='Test Task'" in repr_str
    print("OK Task repr test passed")


if __name__ == "__main__":
    test_task_creation()
    test_task_creation_with_completed_status()
    test_task_repr()
    print("All Task model tests passed!")