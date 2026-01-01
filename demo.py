#!/usr/bin/env python3
"""
Demo script for the Todo In-Memory Console App
This script demonstrates that the application works correctly
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.models import Task
from src.storage import TaskStorage
from src.tasks import TaskOperations
from src.ui import display_tasks, display_message

def demo():
    print("DEMONSTRATION: Todo In-Memory Console App")
    print("="*50)
    
    # Initialize the application components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)
    
    print("\n1. Adding some sample tasks...")
    task1 = task_ops.add_task("Buy groceries", "Milk, bread, eggs, fruits")
    task2 = task_ops.add_task("Complete project", "Finish the todo app implementation")
    task3 = task_ops.add_task("Exercise", "30 minutes of jogging")
    
    if task1 and task2 and task3:
        display_message(f"Added 3 tasks with IDs: {task1.id}, {task2.id}, {task3.id}")
    
    print("\n2. Displaying all tasks...")
    all_tasks = task_ops.list_tasks()
    display_tasks(all_tasks)
    
    print("\n3. Updating a task...")
    success = task_ops.update_task(task2.id, "Complete todo app project", "Finish the implementation and test all features")
    if success:
        display_message(f"Task {task2.id} updated successfully")
    
    print("\n4. Marking a task as complete...")
    success = task_ops.mark_task_complete(task1.id, True)
    if success:
        display_message(f"Task {task1.id} marked as complete")
    
    print("\n5. Displaying updated tasks...")
    updated_tasks = task_ops.list_tasks()
    display_tasks(updated_tasks)
    
    print("\n6. Deleting a task...")
    success = task_ops.delete_task(task3.id)
    if success:
        display_message(f"Task {task3.id} deleted successfully")
    
    print("\n7. Final task list...")
    final_tasks = task_ops.list_tasks()
    display_tasks(final_tasks)
    
    print(f"\nDEMONSTRATION COMPLETE!")
    print(f"- Total tasks created: 3")
    print(f"- Tasks currently stored: {len(final_tasks)}")
    print(f"- Tasks completed: {len([t for t in final_tasks if t.completed])}")
    
    print("\nTo run the interactive application, use the command:")
    print("python -m src.main")

if __name__ == "__main__":
    demo()