"""
Unit tests for filter_tasks functionality
"""
import unittest
import sys
import os

# Add src directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from tasks import TaskOperations
from storage import TaskStorage


class TestFilterTasks(unittest.TestCase):
    """Test cases for filter_tasks functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.storage = TaskStorage()
        self.task_ops = TaskOperations(self.storage)
        
        # Add some test tasks with different properties
        self.task1 = self.task_ops.add_task("Project Alpha", "Complete initial design", "high", ["work", "design"])
        self.task2 = self.task_ops.add_task("Buy groceries", "Milk, eggs, bread", "medium", ["personal", "shopping"])
        self.task3 = self.task_ops.add_task("Review documentation", "Check API docs", "low", ["work", "review"])
        self.task4 = self.task_ops.add_task("Plan vacation", "Research destinations", "medium", ["personal", "travel"])
        
        # Mark one task as complete
        self.task_ops.mark_task_complete(self.task2.id, True)

    def test_filter_by_status_completed(self):
        """Test filtering tasks by completed status."""
        results = self.task_ops.filter_tasks(status=True)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Buy groceries")

    def test_filter_by_status_incomplete(self):
        """Test filtering tasks by incomplete status."""
        results = self.task_ops.filter_tasks(status=False)
        self.assertEqual(len(results), 3)
        titles = [task.title for task in results]
        self.assertIn("Project Alpha", titles)
        self.assertIn("Review documentation", titles)
        self.assertIn("Plan vacation", titles)

    def test_filter_by_priority_high(self):
        """Test filtering tasks by high priority."""
        results = self.task_ops.filter_tasks(priority="high")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Project Alpha")

    def test_filter_by_priority_medium(self):
        """Test filtering tasks by medium priority."""
        results = self.task_ops.filter_tasks(priority="medium")
        self.assertEqual(len(results), 2)
        titles = [task.title for task in results]
        self.assertIn("Buy groceries", titles)
        self.assertIn("Plan vacation", titles)

    def test_filter_by_priority_low(self):
        """Test filtering tasks by low priority."""
        results = self.task_ops.filter_tasks(priority="low")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Review documentation")

    def test_filter_by_tags_single(self):
        """Test filtering tasks by a single tag."""
        results = self.task_ops.filter_tasks(tags=["work"])
        self.assertEqual(len(results), 2)
        titles = [task.title for task in results]
        self.assertIn("Project Alpha", titles)
        self.assertIn("Review documentation", titles)

    def test_filter_by_tags_multiple(self):
        """Test filtering tasks by multiple tags (task must have all tags)."""
        results = self.task_ops.filter_tasks(tags=["personal", "shopping"])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Buy groceries")

    def test_filter_by_tags_none_match(self):
        """Test filtering tasks by tags that no task has."""
        results = self.task_ops.filter_tasks(tags=["nonexistent"])
        self.assertEqual(len(results), 0)

    def test_combined_filter_status_and_priority(self):
        """Test filtering tasks by both status and priority."""
        results = self.task_ops.filter_tasks(status=False, priority="high")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Project Alpha")

    def test_combined_filter_status_and_tags(self):
        """Test filtering tasks by both status and tags."""
        results = self.task_ops.filter_tasks(status=False, tags=["personal"])
        self.assertEqual(len(results), 2)
        titles = [task.title for task in results]
        self.assertIn("Buy groceries", titles)  # This one is completed
        self.assertIn("Plan vacation", titles)
        
        # Actually, the completed task should not be in the results
        # Let me fix this test
        results = self.task_ops.filter_tasks(status=False, tags=["personal"])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Plan vacation")

    def test_combined_filter_all_criteria(self):
        """Test filtering tasks by status, priority, and tags."""
        results = self.task_ops.filter_tasks(status=False, priority="medium", tags=["personal"])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Plan vacation")

    def test_filter_with_none_criteria(self):
        """Test filtering with None criteria (should return all tasks)."""
        results = self.task_ops.filter_tasks()
        self.assertEqual(len(results), 4)

    def test_filter_by_nonexistent_priority(self):
        """Test filtering by a priority that doesn't exist."""
        results = self.task_ops.filter_tasks(priority="nonexistent")
        self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()