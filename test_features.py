"""
Simple test to verify the new features work correctly
"""
import sys
import os

# Add src directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import using absolute imports
import importlib.util

# Load storage module
spec_storage = importlib.util.spec_from_file_location("storage", "./src/storage.py")
storage_module = importlib.util.module_from_spec(spec_storage)
spec_storage.loader.exec_module(storage_module)
TaskStorage = storage_module.TaskStorage

# Load tasks module
spec_tasks = importlib.util.spec_from_file_location("tasks", "./src/tasks.py")
tasks_module = importlib.util.module_from_spec(spec_tasks)
spec_tasks.loader.exec_module(tasks_module)
TaskOperations = tasks_module.TaskOperations


def test_new_features():
    """Test that all new features work correctly."""
    print("Testing new features...")

    # Initialize components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)

    # Test 1: Add task with priority and tags
    print("\n1. Testing task creation with priority and tags...")
    task1 = task_ops.add_task("Test Task", "Test Description", "high", ["work", "urgent"])
    if task1:
        print(f"✓ Created task with ID {task1.id}, priority '{task1.priority}', tags {task1.tags}")
    else:
        print("✗ Failed to create task with priority and tags")
        return False

    # Test 2: Add another task with different priority and tags
    task2 = task_ops.add_task("Another Task", "Another Description", "low", ["personal"])
    if task2:
        print(f"✓ Created task with ID {task2.id}, priority '{task2.priority}', tags {task2.tags}")
    else:
        print("✗ Failed to create second task")
        return False

    # Test 3: Search functionality
    print("\n2. Testing search functionality...")
    results = task_ops.search_tasks("Test")
    if len(results) == 1 and results[0].title == "Test Task":
        print("✓ Search functionality works correctly")
    else:
        print("✗ Search functionality failed")
        return False

    # Test 4: Filter functionality
    print("\n3. Testing filter functionality...")
    high_priority_tasks = task_ops.filter_tasks(priority="high")
    if len(high_priority_tasks) == 1 and high_priority_tasks[0].priority == "high":
        print("✓ Filter by priority works correctly")
    else:
        print("✗ Filter by priority failed")
        return False

    work_tag_tasks = task_ops.filter_tasks(tags=["work"])
    if len(work_tag_tasks) == 1 and "work" in work_tag_tasks[0].tags:
        print("✓ Filter by tags works correctly")
    else:
        print("✗ Filter by tags failed")
        return False

    # Test 5: Sort functionality
    print("\n4. Testing sort functionality...")
    all_tasks = task_ops.list_tasks()
    sorted_tasks = task_ops.sort_tasks(all_tasks, "priority")

    if len(sorted_tasks) == 2:
        # High priority should come first
        if sorted_tasks[0].priority == "high" and sorted_tasks[1].priority == "low":
            print("✓ Sort by priority works correctly")
        else:
            print("✗ Sort by priority failed")
            return False
    else:
        print("✗ Sort functionality failed")
        return False

    # Test 6: Update task with new priority and tags
    print("\n5. Testing update functionality with priority and tags...")
    success = task_ops.update_task(task1.id, title="Updated Test Task", priority="medium", tags=["work", "updated"])
    if success:
        updated_task = task_ops.get_task(task1.id)
        if (updated_task.title == "Updated Test Task" and
            updated_task.priority == "medium" and
            "updated" in updated_task.tags):
            print("✓ Update with priority and tags works correctly")
        else:
            print("✗ Update with priority and tags failed")
            return False
    else:
        print("✗ Update operation failed")
        return False

    print("\n✓ All tests passed! New features are working correctly.")
    return True


if __name__ == "__main__":
    success = test_new_features()
    if success:
        print("\n🎉 All new features implemented successfully!")
    else:
        print("\n❌ Some tests failed.")