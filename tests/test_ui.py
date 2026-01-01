"""
Todo In-Memory Console App
Unit tests for UI components

This module tests the UI functions.
"""

from src.ui import (
    display_menu, display_tasks,
    get_task_input, get_task_id, display_message, get_completion_status
)
from src.models import Task


def test_display_menu():
    """Test that the menu displays correctly."""
    # This test checks that the function runs without error
    try:
        display_menu()
        # If we reach this point, the function executed without error
        print("OK Display menu test passed")
        return True
    except Exception as e:
        print(f"FAIL Display menu test failed: {e}")
        return False


def test_display_tasks():
    """Test displaying tasks."""
    tasks = [
        Task(id=1, title="Task 1", description="Description 1", completed=False),
        Task(id=2, title="Task 2", description="Description 2", completed=True)
    ]

    # This test checks that the function runs without error
    try:
        display_tasks(tasks)
        # If we reach this point, the function executed without error
        print("OK Display tasks test passed")
        return True
    except Exception as e:
        print(f"FAIL Display tasks test failed: {e}")
        return False


def test_display_tasks_empty():
    """Test displaying empty task list."""
    tasks = []

    # This test checks that the function runs without error
    try:
        display_tasks(tasks)
        # If we reach this point, the function executed without error
        print("OK Display tasks empty test passed")
        return True
    except Exception as e:
        print(f"FAIL Display tasks empty test failed: {e}")
        return False


def test_display_message():
    """Test displaying a message."""
    # This test checks that the function runs without error
    try:
        display_message("Test message")
        # If we reach this point, the function executed without error
        print("OK Display message test passed")
        return True
    except Exception as e:
        print(f"FAIL Display message test failed: {e}")
        return False


if __name__ == "__main__":
    all_passed = True
    all_passed &= test_display_menu()
    all_passed &= test_display_tasks()
    all_passed &= test_display_tasks_empty()
    all_passed &= test_display_message()

    if all_passed:
        print("All UI tests passed!")
    else:
        print("Some UI tests failed!")