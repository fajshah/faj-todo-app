"""
Unit tests for sort_tasks functionality
"""
import unittest
import sys
import os

# Add src directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from tasks import TaskOperations
from storage import TaskStorage
from models import Task


class TestSortTasks(unittest.TestCase):
    """Test cases for sort_tasks functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.storage = TaskStorage()
        self.task_ops = TaskOperations(self.storage)
        
        # Add some test tasks with different properties
        self.task1 = self.task_ops.add_task("Task C", "Description C", "low", ["tag1"])
        self.task2 = self.task_ops.add_task("Task A", "Description A", "high", ["tag2"])
        self.task3 = self.task_ops.add_task("Task B", "Description B", "medium", ["tag3"])
        self.task4 = self.task_ops.add_task("Task D", "Description D", "high", ["tag4"])

    def test_sort_by_priority(self):
        """Test sorting tasks by priority (high, medium, low)."""
        all_tasks = self.task_ops.list_tasks()
        sorted_tasks = self.task_ops.sort_tasks(all_tasks, "priority")
        
        # Check that high priority tasks come first
        self.assertEqual(sorted_tasks[0].priority, "high")
        self.assertEqual(sorted_tasks[1].priority, "high")
        self.assertEqual(sorted_tasks[2].priority, "medium")
        self.assertEqual(sorted_tasks[3].priority, "low")
        
        # Check that high priority tasks are at the beginning
        for i in range(2):
            self.assertEqual(sorted_tasks[i].priority, "high")
        self.assertEqual(sorted_tasks[2].priority, "medium")
        self.assertEqual(sorted_tasks[3].priority, "low")

    def test_sort_by_title(self):
        """Test sorting tasks alphabetically by title."""
        all_tasks = self.task_ops.list_tasks()
        sorted_tasks = self.task_ops.sort_tasks(all_tasks, "title")
        
        titles = [task.title for task in sorted_tasks]
        expected_order = ["Task A", "Task B", "Task C", "Task D"]
        self.assertEqual(titles, expected_order)

    def test_sort_by_due_date(self):
        """Test sorting tasks by due date (placeholder implementation)."""
        all_tasks = self.task_ops.list_tasks()
        sorted_tasks = self.task_ops.sort_tasks(all_tasks, "due_date")
        
        # For now, due_date sorting returns the same list
        # This is a placeholder until due dates are implemented
        self.assertEqual(len(sorted_tasks), len(all_tasks))

    def test_sort_with_invalid_criteria(self):
        """Test sorting with invalid criteria (should return original list)."""
        all_tasks = self.task_ops.list_tasks()
        sorted_tasks = self.task_ops.sort_tasks(all_tasks, "invalid_criteria")
        
        # Should return the same list when criteria is invalid
        self.assertEqual(len(sorted_tasks), len(all_tasks))

    def test_sort_empty_list(self):
        """Test sorting an empty list of tasks."""
        empty_list = []
        sorted_tasks = self.task_ops.sort_tasks(empty_list, "priority")
        
        self.assertEqual(sorted_tasks, [])

    def test_sort_single_task(self):
        """Test sorting a list with a single task."""
        single_task_list = [self.task1]
        sorted_tasks = self.task_ops.sort_tasks(single_task_list, "priority")
        
        self.assertEqual(len(sorted_tasks), 1)
        self.assertEqual(sorted_tasks[0].id, self.task1.id)

    def test_sort_already_sorted(self):
        """Test sorting a list that is already sorted."""
        # Create a new storage to have control over the order
        storage = TaskStorage()
        task_ops = TaskOperations(storage)
        
        # Add tasks in order that should remain the same when sorted by title
        task_a = task_ops.add_task("A Task", "Description", "medium")
        task_b = task_ops.add_task("B Task", "Description", "medium")
        task_c = task_ops.add_task("C Task", "Description", "medium")
        
        all_tasks = task_ops.list_tasks()
        sorted_tasks = task_ops.sort_tasks(all_tasks, "title")
        
        # The order should remain the same
        self.assertEqual(sorted_tasks[0].title, "A Task")
        self.assertEqual(sorted_tasks[1].title, "B Task")
        self.assertEqual(sorted_tasks[2].title, "C Task")


if __name__ == '__main__':
    unittest.main()