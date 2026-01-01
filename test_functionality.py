"""
Todo In-Memory Console App
Basic functionality test
"""

import sys
import os
# Add src to the Python path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.models import Task
from src.storage import TaskStorage
from src.tasks import TaskOperations


def test_basic_functionality():
    """Test the basic functionality of the todo app."""
    print("Testing basic functionality of Todo In-Memory Console App...")

    # Initialize components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    # Test 1: Add tasks
    print("\n1. Testing task creation...")
    task1 = task_ops.add_task("Buy groceries", "Milk, bread, eggs")
    task2 = task_ops.add_task("Walk the dog", "Take Fido to the park")

    if task1 and task2:
        print(f"OK Tasks created successfully - IDs: {task1.id}, {task2.id}")
    else:
        print("FAIL Failed to create tasks")
        return False

    # Test 2: List tasks
    print("\n2. Testing task listing...")
    tasks = task_ops.list_tasks()
    if len(tasks) == 2:
        print(f"OK Found {len(tasks)} tasks as expected")
        for task in tasks:
            status = "Complete" if task.completed else "Incomplete"
            print(f"  - ID: {task.id}, Title: {task.title}, Status: {status}")
    else:
        print(f"FAIL Expected 2 tasks, found {len(tasks)}")
        return False

    # Test 3: Update a task
    print("\n3. Testing task update...")
    update_success = task_ops.update_task(task1.id, "Buy groceries updated", "Milk, bread, eggs, fruits")
    if update_success:
        updated_task = task_ops.get_task(task1.id)
        if updated_task and updated_task.title == "Buy groceries updated":
            print(f"OK Task {task1.id} updated successfully")
        else:
            print("FAIL Task update failed - title not changed correctly")
            return False
    else:
        print("FAIL Failed to update task")
        return False

    # Test 4: Mark task as complete
    print("\n4. Testing task completion...")
    complete_success = task_ops.mark_task_complete(task1.id, True)
    if complete_success:
        completed_task = task_ops.get_task(task1.id)
        if completed_task and completed_task.completed:
            print(f"OK Task {task1.id} marked as complete successfully")
        else:
            print("FAIL Task completion failed - status not changed")
            return False
    else:
        print("FAIL Failed to mark task as complete")
        return False

    # Test 5: Delete a task
    print("\n5. Testing task deletion...")
    delete_success = task_ops.delete_task(task2.id)
    if delete_success:
        remaining_tasks = task_ops.list_tasks()
        if len(remaining_tasks) == 1 and remaining_tasks[0].id == task1.id:
            print(f"OK Task {task2.id} deleted successfully")
            print(f"  Remaining task count: {len(remaining_tasks)}")
        else:
            print("FAIL Task deletion failed - incorrect remaining task count")
            return False
    else:
        print("FAIL Failed to delete task")
        return False

    print("\nOK All tests passed! The basic functionality is working correctly.")
    return True


if __name__ == "__main__":
    success = test_basic_functionality()
    if success:
        print("\nSUCCESS Todo In-Memory Console App is functioning as expected!")
    else:
        print("\nFAILURE Some tests failed. Please check the implementation.")
        sys.exit(1)