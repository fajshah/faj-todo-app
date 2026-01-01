"""
Integration tests for the Todo App – Intermediate Level Features
"""
import unittest
import sys
import os

# Add src directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from tasks import TaskOperations
from storage import TaskStorage


class TestIntegration(unittest.TestCase):
    """Integration tests for combined functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.storage = TaskStorage()
        self.task_ops = TaskOperations(self.storage)

    def test_full_workflow_add_search_filter_sort(self):
        """Test the full workflow: add tasks, search, filter, and sort."""
        # Add multiple tasks with different properties
        task1 = self.task_ops.add_task("Project Alpha", "Complete initial design", "high", ["work", "design"])
        task2 = self.task_ops.add_task("Buy groceries", "Milk, eggs, bread", "medium", ["personal", "shopping"])
        task3 = self.task_ops.add_task("Review documentation", "Check API docs", "low", ["work", "review"])
        task4 = self.task_ops.add_task("Plan vacation", "Research destinations", "medium", ["personal", "travel"])
        
        # Mark one task as complete
        self.task_ops.mark_task_complete(task2.id, True)

        # Test search functionality
        search_results = self.task_ops.search_tasks("Project")
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0].title, "Project Alpha")

        # Test filter functionality
        completed_tasks = self.task_ops.filter_tasks(status=True)
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].title, "Buy groceries")

        high_priority_tasks = self.task_ops.filter_tasks(priority="high")
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0].title, "Project Alpha")

        work_tasks = self.task_ops.filter_tasks(tags=["work"])
        self.assertEqual(len(work_tasks), 2)

        # Test combined filter
        work_and_high = self.task_ops.filter_tasks(status=False, priority="high", tags=["work"])
        self.assertEqual(len(work_and_high), 1)
        self.assertEqual(work_and_high[0].title, "Project Alpha")

        # Test sort functionality
        all_tasks = self.task_ops.list_tasks()
        sorted_by_priority = self.task_ops.sort_tasks(all_tasks, "priority")
        
        # High priority should come first
        self.assertEqual(sorted_by_priority[0].priority, "high")
        self.assertEqual(sorted_by_priority[1].priority, "medium")
        self.assertEqual(sorted_by_priority[2].priority, "medium")
        self.assertEqual(sorted_by_priority[3].priority, "low")

        # Test update functionality
        updated = self.task_ops.update_task(task3.id, title="Updated documentation review", priority="high")
        self.assertTrue(updated)
        
        updated_task = self.task_ops.get_task(task3.id)
        self.assertEqual(updated_task.title, "Updated documentation review")
        self.assertEqual(updated_task.priority, "high")

        # Verify the updated priority affects sorting
        all_tasks_after_update = self.task_ops.list_tasks()
        sorted_after_update = self.task_ops.sort_tasks(all_tasks_after_update, "priority")
        
        # Now there should be 2 high priority tasks at the beginning
        high_priority_count = sum(1 for task in sorted_after_update if task.priority == "high")
        self.assertEqual(high_priority_count, 2)

    def test_search_filter_sort_combined_workflow(self):
        """Test combined search, filter, and sort operations."""
        # Add tasks
        self.task_ops.add_task("Urgent work task", "Complete report", "high", ["work", "urgent"])
        self.task_ops.add_task("Personal chore", "Clean house", "medium", ["personal"])
        self.task_ops.add_task("Less urgent work", "Check emails", "low", ["work"])
        self.task_ops.add_task("Very urgent work", "Fix critical bug", "high", ["work", "urgent"])

        # Search for work-related tasks
        search_results = self.task_ops.search_tasks("work")
        self.assertEqual(len(search_results), 3)

        # Filter the search results by high priority
        high_priority_work = self.task_ops.filter_tasks(status=None, priority="high", tags=["work"])
        self.assertEqual(len(high_priority_work), 2)

        # Sort the filtered results by title
        sorted_results = self.task_ops.sort_tasks(high_priority_work, "title")
        titles = [task.title for task in sorted_results]
        self.assertEqual(titles, ["Urgent work task", "Very urgent work task"])

    def test_task_lifecycle_operations(self):
        """Test the complete lifecycle of a task through all operations."""
        # Add a task
        new_task = self.task_ops.add_task("Test task", "Test description", "medium", ["test", "important"])
        self.assertIsNotNone(new_task)
        self.assertEqual(new_task.title, "Test task")
        self.assertEqual(new_task.priority, "medium")
        self.assertIn("test", new_task.tags)

        # Update the task
        updated = self.task_ops.update_task(new_task.id, title="Updated test task", priority="high", tags=["updated", "critical"])
        self.assertTrue(updated)

        # Verify update
        updated_task = self.task_ops.get_task(new_task.id)
        self.assertEqual(updated_task.title, "Updated test task")
        self.assertEqual(updated_task.priority, "high")
        self.assertIn("updated", updated_task.tags)

        # Search for the updated task
        search_results = self.task_ops.search_tasks("Updated")
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0].id, updated_task.id)

        # Filter by the new priority
        high_priority_tasks = self.task_ops.filter_tasks(priority="high")
        high_task_ids = [task.id for task in high_priority_tasks]
        self.assertIn(updated_task.id, high_task_ids)

        # Sort by priority and verify the task is in the right position
        all_tasks = self.task_ops.list_tasks()
        sorted_tasks = self.task_ops.sort_tasks(all_tasks, "priority")
        
        # The updated task should be among the high priority tasks (at the beginning)
        high_priority_task_count = sum(1 for task in sorted_tasks if task.priority == "high")
        high_priority_tasks_list = [task for task in sorted_tasks if task.priority == "high"]
        self.assertIn(updated_task.id, [task.id for task in high_priority_tasks_list])

        # Mark as complete
        marked = self.task_ops.mark_task_complete(updated_task.id, True)
        self.assertTrue(marked)

        # Verify completion status
        completed_task = self.task_ops.get_task(updated_task.id)
        self.assertTrue(completed_task.completed)

        # Filter by completion status
        completed_tasks = self.task_ops.filter_tasks(status=True)
        completed_task_ids = [task.id for task in completed_tasks]
        self.assertIn(updated_task.id, completed_task_ids)

        # Delete the task
        deleted = self.task_ops.delete_task(updated_task.id)
        self.assertTrue(deleted)

        # Verify deletion
        deleted_task = self.task_ops.get_task(updated_task.id)
        self.assertIsNone(deleted_task)

        # Ensure it's not in search results anymore
        search_after_deletion = self.task_ops.search_tasks("Updated")
        self.assertEqual(len(search_after_deletion), 0)


if __name__ == '__main__':
    unittest.main()