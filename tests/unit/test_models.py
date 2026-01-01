"""
Unit tests for Task model with priority and tags functionality
"""
import unittest
import sys
import os

# Add src directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from models import Task


class TestTaskModel(unittest.TestCase):
    """Test cases for the Task model with priority and tags."""

    def test_task_creation_with_defaults(self):
        """Test creating a task with default priority and empty tags."""
        task = Task(id=1, title="Test Task", description="Test Description")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, False)
        self.assertEqual(task.priority, "medium")  # Default priority
        self.assertEqual(task.tags, [])  # Default empty list

    def test_task_creation_with_priority_and_tags(self):
        """Test creating a task with specific priority and tags."""
        tags = ["work", "urgent"]
        task = Task(
            id=1,
            title="Test Task",
            description="Test Description",
            completed=False,
            priority="high",
            tags=tags
        )
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, False)
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, tags)

    def test_task_creation_with_none_tags(self):
        """Test that None tags are converted to empty list."""
        task = Task(
            id=1,
            title="Test Task",
            description="Test Description",
            completed=False,
            priority="low",
            tags=None
        )
        
        self.assertEqual(task.tags, [])  # Should be converted to empty list

    def test_task_modification(self):
        """Test modifying task properties after creation."""
        task = Task(id=1, title="Test Task", description="Test Description")
        
        # Modify properties
        task.title = "Updated Title"
        task.description = "Updated Description"
        task.completed = True
        task.priority = "high"
        task.tags = ["updated", "tags"]
        
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Updated Description")
        self.assertEqual(task.completed, True)
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["updated", "tags"])


if __name__ == '__main__':
    unittest.main()