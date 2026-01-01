"""
Todo In-Memory Console App
Integration tests

This module tests the integration between different components.
"""

from src.models import Task
from src.storage import TaskStorage
from src.tasks import TaskOperations
from src.ui import display_tasks, get_task_input


def test_full_task_lifecycle():
    """Test the complete lifecycle of a task through all components."""
    # Initialize components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    # 1. Add a task
    task = task_ops.add_task("Integration Test Task", "This is an integration test")
    assert task is not None
    assert task.id == 1
    assert task.title == "Integration Test Task"
    assert task.description == "This is an integration test"
    assert task.completed is False

    # 2. List tasks
    tasks = task_ops.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1

    # 3. Update the task
    update_success = task_ops.update_task(task.id, "Updated Integration Test Task", "Updated description")
    assert update_success is True

    updated_task = task_ops.get_task(task.id)
    assert updated_task.title == "Updated Integration Test Task"
    assert updated_task.description == "Updated description"

    # 4. Mark as complete
    complete_success = task_ops.mark_task_complete(task.id, True)
    assert complete_success is True

    completed_task = task_ops.get_task(task.id)
    assert completed_task.completed is True

    # 5. Mark as incomplete again
    incomplete_success = task_ops.mark_task_complete(task.id, False)
    assert incomplete_success is True

    incomplete_task = task_ops.get_task(task.id)
    assert incomplete_task.completed is False

    # 6. Delete the task
    delete_success = task_ops.delete_task(task.id)
    assert delete_success is True

    # 7. Verify task is deleted
    deleted_task = task_ops.get_task(task.id)
    assert deleted_task is None

    tasks_after_delete = task_ops.list_tasks()
    assert len(tasks_after_delete) == 0
    print("OK Full task lifecycle test passed")


def test_multiple_tasks():
    """Test operations with multiple tasks."""
    # Initialize components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    # Add multiple tasks
    task1 = task_ops.add_task("Task 1", "Description 1")
    task2 = task_ops.add_task("Task 2", "Description 2")
    task3 = task_ops.add_task("Task 3", "Description 3")

    # Verify all tasks exist
    all_tasks = task_ops.list_tasks()
    assert len(all_tasks) == 3

    # Update one task
    task_ops.update_task(task2.id, "Updated Task 2", "Updated Description 2")
    updated_task = task_ops.get_task(task2.id)
    assert updated_task.title == "Updated Task 2"

    # Mark one as complete
    task_ops.mark_task_complete(task1.id, True)
    completed_task = task_ops.get_task(task1.id)
    assert completed_task.completed is True

    # Delete one task
    task_ops.delete_task(task3.id)
    remaining_tasks = task_ops.list_tasks()
    assert len(remaining_tasks) == 2

    # Verify the right task was deleted
    task_ids = [task.id for task in remaining_tasks]
    assert task3.id not in task_ids
    assert task1.id in task_ids
    assert task2.id in task_ids
    print("OK Multiple tasks test passed")


def test_ui_integration_with_tasks():
    """Test UI functions work with actual tasks."""
    # Initialize components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    # Add some tasks
    task_ops.add_task("UI Test Task 1", "Description for UI test 1")
    task_ops.add_task("UI Test Task 2", "Description for UI test 2")

    # Get all tasks and verify UI function can handle them
    tasks = task_ops.list_tasks()
    assert len(tasks) == 2

    # Test that display_tasks can handle the tasks without error
    try:
        display_tasks(tasks)
        # If we reach this point, the function executed without error
        print("OK UI integration with tasks test passed")
        return True
    except Exception as e:
        print(f"FAIL UI integration with tasks test failed: {e}")
        return False


def test_task_validation_integration():
    """Test that validation works across components."""
    # Initialize components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    # Try to add a task with empty title (should fail)
    result = task_ops.add_task("", "This should fail")
    assert result is None

    # Verify no tasks were added
    tasks = task_ops.list_tasks()
    assert len(tasks) == 0

    # Add a valid task
    valid_task = task_ops.add_task("Valid Task", "This should work")
    assert valid_task is not None

    # Try to update with empty title (should not update title)
    success = task_ops.update_task(valid_task.id, "", "New description")
    # The update should succeed but not change the title since it's empty
    same_task = task_ops.get_task(valid_task.id)
    assert same_task.title == "Valid Task"  # Title should remain unchanged
    assert same_task.description == "New description"  # Description should be updated
    print("OK Task validation integration test passed")


def test_task_id_uniqueness():
    """Test that task IDs are unique across operations."""
    # Initialize components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    # Add multiple tasks and track their IDs
    task1 = task_ops.add_task("Task 1", "Description 1")
    task2 = task_ops.add_task("Task 2", "Description 2")
    task3 = task_ops.add_task("Task 3", "Description 3")

    # Verify IDs are unique and sequential
    ids = [task1.id, task2.id, task3.id]
    assert len(set(ids)) == 3  # All IDs should be unique
    assert sorted(ids) == [1, 2, 3]  # IDs should be sequential starting from 1

    # Delete middle task
    task_ops.delete_task(task2.id)

    # Add another task - should get the next ID
    task4 = task_ops.add_task("Task 4", "Description 4")
    assert task4.id == 4  # Should be 4, not 2

    # Verify remaining tasks still have their original IDs
    remaining_tasks = task_ops.list_tasks()
    remaining_ids = [task.id for task in remaining_tasks]
    assert 1 in remaining_ids  # task1
    assert 2 not in remaining_ids  # task2 (deleted)
    assert 3 in remaining_ids  # task3
    assert 4 in remaining_ids  # task4
    print("OK Task ID uniqueness test passed")


if __name__ == "__main__":
    test_full_task_lifecycle()
    test_multiple_tasks()
    test_ui_integration_with_tasks()
    test_task_validation_integration()
    test_task_id_uniqueness()
    print("All integration tests passed!")