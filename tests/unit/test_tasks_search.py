"""
Unit tests for search_tasks functionality
"""
import unittest
import sys
import os

# Add src directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from tasks import TaskOperations
from storage import TaskStorage


class TestSearchTasks(unittest.TestCase):
    """Test cases for search_tasks functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.storage = TaskStorage()
        self.task_ops = TaskOperations(self.storage)
        
        # Add some test tasks
        self.task1 = self.task_ops.add_task("Project Alpha", "Complete initial design", "high", ["work", "design"])
        self.task2 = self.task_ops.add_task("Buy groceries", "Milk, eggs, bread", "medium", ["personal", "shopping"])
        self.task3 = self.task_ops.add_task("Review documentation", "Check API docs", "low", ["work", "review"])
        self.task4 = self.task_ops.add_task("Plan vacation", "Research destinations", "medium", ["personal", "travel"])

    def test_search_by_title(self):
        """Test searching tasks by keyword in title."""
        results = self.task_ops.search_tasks("Project")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Project Alpha")

    def test_search_by_description(self):
        """Test searching tasks by keyword in description."""
        results = self.task_ops.search_tasks("groceries")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Buy groceries")

    def test_search_case_insensitive(self):
        """Test that search is case insensitive."""
        results = self.task_ops.search_tasks("PROJECT")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Project Alpha")

    def test_search_partial_match(self):
        """Test searching with partial keyword matches."""
        results = self.task_ops.search_tasks("doc")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Review documentation")

    def test_search_multiple_matches(self):
        """Test searching when multiple tasks match the keyword."""
        results = self.task_ops.search_tasks("work")
        self.assertEqual(len(results), 2)
        titles = [task.title for task in results]
        self.assertIn("Project Alpha", titles)
        self.assertIn("Review documentation", titles)

    def test_search_no_match(self):
        """Test searching when no tasks match the keyword."""
        results = self.task_ops.search_tasks("nonexistent")
        self.assertEqual(len(results), 0)

    def test_search_empty_keyword(self):
        """Test searching with empty keyword."""
        results = self.task_ops.search_tasks("")
        self.assertEqual(len(results), 0)

    def test_search_whitespace_keyword(self):
        """Test searching with whitespace-only keyword."""
        results = self.task_ops.search_tasks("   ")
        self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()