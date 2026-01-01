"""
Todo In-Memory Console App
Unit tests for task operations

This module tests the TaskOperations class functionality.
"""

from src.models import Task
from src.storage import TaskStorage
from src.tasks import TaskOperations


def test_task_operations_initialization():
    """Test initializing TaskOperations with a storage instance."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    assert task_ops.storage == storage
    print("OK TaskOperations initialization test passed")


def test_add_task_operation():
    """Test adding a task through TaskOperations."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    task = task_ops.add_task("Test Title", "Test Description")

    assert task is not None
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed is False
    print("OK Add task operation test passed")


def test_add_task_with_empty_title():
    """Test adding a task with an empty title."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    result = task_ops.add_task("", "Test Description")

    assert result is None
    print("OK Add task with empty title test passed")


def test_add_task_with_whitespace_only_title():
    """Test adding a task with a whitespace-only title."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    result = task_ops.add_task("   ", "Test Description")

    assert result is None
    print("OK Add task with whitespace-only title test passed")


def test_list_tasks():
    """Test listing all tasks."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    task_ops.add_task("Title 1", "Description 1")
    task_ops.add_task("Title 2", "Description 2")

    tasks = task_ops.list_tasks()

    assert len(tasks) == 2
    titles = [task.title for task in tasks]
    assert "Title 1" in titles
    assert "Title 2" in titles
    print("OK List tasks test passed")


def test_update_task_operation():
    """Test updating a task through TaskOperations."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    original_task = task_ops.add_task("Original Title", "Original Description")

    success = task_ops.update_task(original_task.id, "Updated Title", "Updated Description")

    assert success is True

    updated_task = task_ops.get_task(original_task.id)
    assert updated_task.title == "Updated Title"
    assert updated_task.description == "Updated Description"
    print("OK Update task operation test passed")


def test_update_task_with_none_values():
    """Test updating a task with None values (should not update)."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    original_task = task_ops.add_task("Original Title", "Original Description")

    success = task_ops.update_task(original_task.id, None, None)

    assert success is True  # Update should succeed but not change anything

    same_task = task_ops.get_task(original_task.id)
    assert same_task.title == "Original Title"
    assert same_task.description == "Original Description"
    print("OK Update task with None values test passed")


def test_update_nonexistent_task():
    """Test updating a task that doesn't exist."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    success = task_ops.update_task(999, "New Title", "New Description")

    assert success is False
    print("OK Update nonexistent task test passed")


def test_delete_task_operation():
    """Test deleting a task through TaskOperations."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    task = task_ops.add_task("Test Title", "Test Description")

    success = task_ops.delete_task(task.id)

    assert success is True
    assert task_ops.get_task(task.id) is None
    assert len(task_ops.list_tasks()) == 0
    print("OK Delete task operation test passed")


def test_delete_nonexistent_task():
    """Test deleting a task that doesn't exist."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    success = task_ops.delete_task(999)

    assert success is False
    print("OK Delete nonexistent task test passed")


def test_mark_task_complete():
    """Test marking a task as complete."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    task = task_ops.add_task("Test Title", "Test Description")
    assert task.completed is False

    success = task_ops.mark_task_complete(task.id, True)

    assert success is True

    completed_task = task_ops.get_task(task.id)
    assert completed_task.completed is True
    print("OK Mark task complete test passed")


def test_mark_task_incomplete():
    """Test marking a task as incomplete."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    task = task_ops.add_task("Test Title", "Test Description")
    # First mark as complete
    task_ops.mark_task_complete(task.id, True)
    assert task.completed is True

    success = task_ops.mark_task_complete(task.id, False)

    assert success is True

    incomplete_task = task_ops.get_task(task.id)
    assert incomplete_task.completed is False
    print("OK Mark task incomplete test passed")


def test_get_task():
    """Test getting a specific task."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    original_task = task_ops.add_task("Test Title", "Test Description")

    retrieved_task = task_ops.get_task(original_task.id)

    assert retrieved_task is not None
    assert retrieved_task.id == original_task.id
    assert retrieved_task.title == original_task.title
    assert retrieved_task.description == original_task.description
    assert retrieved_task.completed == original_task.completed
    print("OK Get task test passed")


def test_get_nonexistent_task():
    """Test getting a task that doesn't exist."""
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    retrieved_task = task_ops.get_task(999)

    assert retrieved_task is None
    print("OK Get nonexistent task test passed")


if __name__ == "__main__":
    test_task_operations_initialization()
    test_add_task_operation()
    test_add_task_with_empty_title()
    test_add_task_with_whitespace_only_title()
    test_list_tasks()
    test_update_task_operation()
    test_update_task_with_none_values()
    test_update_nonexistent_task()
    test_delete_task_operation()
    test_delete_nonexistent_task()
    test_mark_task_complete()
    test_mark_task_incomplete()
    test_get_task()
    test_get_nonexistent_task()
    print("All TaskOperations tests passed!")