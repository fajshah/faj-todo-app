"""
Unit tests for add_task and update_task functionality with priority and tags
"""
import unittest
import sys
import os

# Add src directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from models import Task
from tasks import TaskOperations
from storage import TaskStorage


class TestAddTask(unittest.TestCase):
    """Test cases for add_task functionality with priority and tags."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.storage = TaskStorage()
        self.task_ops = TaskOperations(self.storage)

    def test_add_task_with_defaults(self):
        """Test adding a task with default priority and empty tags."""
        task = self.task_ops.add_task("Test Title", "Test Description")

        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.priority, "medium")  # Default priority
        self.assertEqual(task.tags, [])  # Default empty list
        self.assertEqual(task.completed, False)

    def test_add_task_with_priority_and_tags(self):
        """Test adding a task with specific priority and tags."""
        tags = ["work", "urgent"]
        task = self.task_ops.add_task(
            "Test Title",
            "Test Description",
            priority="high",
            tags=tags
        )

        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, tags)
        self.assertEqual(task.completed, False)

    def test_add_task_with_none_tags(self):
        """Test adding a task with None tags (should become empty list)."""
        task = self.task_ops.add_task(
            "Test Title",
            "Test Description",
            priority="low",
            tags=None
        )

        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.priority, "low")
        self.assertEqual(task.tags, [])  # Should be converted to empty list

    def test_add_task_empty_title_fails(self):
        """Test that adding a task with empty title fails."""
        task = self.task_ops.add_task("", "Test Description")

        self.assertIsNone(task)

    def test_add_task_whitespace_title_fails(self):
        """Test that adding a task with whitespace-only title fails."""
        task = self.task_ops.add_task("   ", "Test Description")

        self.assertIsNone(task)

    def test_add_task_invalid_priority_fails(self):
        """Test that adding a task with invalid priority fails."""
        task = self.task_ops.add_task("Test Title", "Test Description", priority="invalid")

        self.assertIsNone(task)

    def test_add_task_empty_tags_list(self):
        """Test adding a task with empty tags list."""
        task = self.task_ops.add_task(
            "Test Title",
            "Test Description",
            priority="medium",
            tags=[]
        )

        self.assertIsNotNone(task)
        self.assertEqual(task.tags, [])


class TestUpdateTask(unittest.TestCase):
    """Test cases for update_task functionality with priority and tags."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.storage = TaskStorage()
        self.task_ops = TaskOperations(self.storage)
        # Add a task to update
        self.task = self.task_ops.add_task("Original Title", "Original Description")

    def test_update_task_title_and_description(self):
        """Test updating task title and description."""
        result = self.task_ops.update_task(
            self.task.id,
            title="Updated Title",
            description="Updated Description"
        )

        self.assertTrue(result)
        updated_task = self.task_ops.get_task(self.task.id)
        self.assertEqual(updated_task.title, "Updated Title")
        self.assertEqual(updated_task.description, "Updated Description")

    def test_update_task_priority(self):
        """Test updating task priority."""
        result = self.task_ops.update_task(
            self.task.id,
            priority="high"
        )

        self.assertTrue(result)
        updated_task = self.task_ops.get_task(self.task.id)
        self.assertEqual(updated_task.priority, "high")

    def test_update_task_tags(self):
        """Test updating task tags."""
        new_tags = ["updated", "tags"]
        result = self.task_ops.update_task(
            self.task.id,
            tags=new_tags
        )

        self.assertTrue(result)
        updated_task = self.task_ops.get_task(self.task.id)
        self.assertEqual(updated_task.tags, new_tags)

    def test_update_task_all_fields(self):
        """Test updating all task fields."""
        new_tags = ["all", "updated"]
        result = self.task_ops.update_task(
            self.task.id,
            title="All Updated Title",
            description="All Updated Description",
            priority="low",
            tags=new_tags
        )

        self.assertTrue(result)
        updated_task = self.task_ops.get_task(self.task.id)
        self.assertEqual(updated_task.title, "All Updated Title")
        self.assertEqual(updated_task.description, "All Updated Description")
        self.assertEqual(updated_task.priority, "low")
        self.assertEqual(updated_task.tags, new_tags)

    def test_update_task_invalid_priority_fails(self):
        """Test that updating with invalid priority fails."""
        result = self.task_ops.update_task(
            self.task.id,
            priority="invalid"
        )

        self.assertFalse(result)

    def test_update_task_nonexistent_task(self):
        """Test updating a non-existent task."""
        result = self.task_ops.update_task(
            999,  # Non-existent ID
            title="Should not work"
        )

        self.assertFalse(result)

    def test_update_task_with_none_values(self):
        """Test updating task with None values (should not change those fields)."""
        original_task = self.task_ops.get_task(self.task.id)
        original_priority = original_task.priority
        original_tags = original_task.tags[:]

        result = self.task_ops.update_task(
            self.task.id,
            title="Updated Title",
            priority=None,  # Should not change priority
            tags=None  # Should not change tags
        )

        self.assertTrue(result)
        updated_task = self.task_ops.get_task(self.task.id)
        self.assertEqual(updated_task.title, "Updated Title")
        self.assertEqual(updated_task.priority, original_priority)
        self.assertEqual(updated_task.tags, original_tags)


if __name__ == '__main__':
    unittest.main()