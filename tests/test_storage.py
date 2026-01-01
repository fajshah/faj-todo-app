"""
Todo In-Memory Console App
Unit tests for storage operations

This module tests the TaskStorage class functionality.
"""

from src.models import Task
from src.storage import TaskStorage


def test_task_storage_initialization():
    """Test initializing an empty TaskStorage."""
    storage = TaskStorage()

    assert len(storage.get_all_tasks()) == 0
    assert storage._next_id == 1
    print("OK TaskStorage initialization test passed")


def test_add_task():
    """Test adding a task to storage."""
    storage = TaskStorage()
    task = storage.add_task("Test Title", "Test Description")

    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed is False

    # Verify the task is in the storage
    tasks = storage.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1
    print("OK Add task test passed")


def test_get_task_by_id():
    """Test retrieving a task by its ID."""
    storage = TaskStorage()
    added_task = storage.add_task("Test Title", "Test Description")

    retrieved_task = storage.get_task(added_task.id)

    assert retrieved_task is not None
    assert retrieved_task.id == added_task.id
    assert retrieved_task.title == added_task.title
    assert retrieved_task.description == added_task.description
    assert retrieved_task.completed == added_task.completed
    print("OK Get task by ID test passed")


def test_get_task_by_invalid_id():
    """Test retrieving a task with an invalid ID."""
    storage = TaskStorage()
    storage.add_task("Test Title", "Test Description")

    retrieved_task = storage.get_task(999)

    assert retrieved_task is None
    print("OK Get task by invalid ID test passed")


def test_get_all_tasks():
    """Test retrieving all tasks."""
    storage = TaskStorage()
    task1 = storage.add_task("Title 1", "Description 1")
    task2 = storage.add_task("Title 2", "Description 2")

    tasks = storage.get_all_tasks()

    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks
    print("OK Get all tasks test passed")


def test_update_task():
    """Test updating a task."""
    storage = TaskStorage()
    original_task = storage.add_task("Original Title", "Original Description")

    # Update title and description
    success = storage.update_task(
        original_task.id,
        title="Updated Title",
        description="Updated Description"
    )

    assert success is True

    updated_task = storage.get_task(original_task.id)
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    assert updated_task.completed == original_task.completed  # Should remain unchanged
    print("OK Update task test passed")


def test_update_task_status():
    """Test updating a task's completion status."""
    storage = TaskStorage()
    task = storage.add_task("Test Title", "Test Description")

    # Update completion status
    success = storage.update_task(task.id, completed=True)

    assert success is True

    updated_task = storage.get_task(task.id)
    assert updated_task.completed is True
    assert updated_task.title == task.title  # Should remain unchanged
    assert updated_task.description == task.description  # Should remain unchanged
    print("OK Update task status test passed")


def test_update_nonexistent_task():
    """Test updating a task that doesn't exist."""
    storage = TaskStorage()

    success = storage.update_task(999, title="New Title")

    assert success is False
    print("OK Update nonexistent task test passed")


def test_delete_task():
    """Test deleting a task."""
    storage = TaskStorage()
    task = storage.add_task("Test Title", "Test Description")

    success = storage.delete_task(task.id)

    assert success is True
    assert storage.get_task(task.id) is None
    assert len(storage.get_all_tasks()) == 0
    print("OK Delete task test passed")


def test_delete_nonexistent_task():
    """Test deleting a task that doesn't exist."""
    storage = TaskStorage()

    success = storage.delete_task(999)

    assert success is False
    print("OK Delete nonexistent task test passed")


def test_auto_increment_id():
    """Test that IDs are auto-incremented."""
    storage = TaskStorage()
    task1 = storage.add_task("Title 1", "Description 1")
    task2 = storage.add_task("Title 2", "Description 2")
    task3 = storage.add_task("Title 3", "Description 3")

    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3
    print("OK Auto increment ID test passed")


if __name__ == "__main__":
    test_task_storage_initialization()
    test_add_task()
    test_get_task_by_id()
    test_get_task_by_invalid_id()
    test_get_all_tasks()
    test_update_task()
    test_update_task_status()
    test_update_nonexistent_task()
    test_delete_task()
    test_delete_nonexistent_task()
    test_auto_increment_id()
    print("All TaskStorage tests passed!")