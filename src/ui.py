"""
Todo In-Memory Console App
UI module

This module handles console input/output and menu display.
"""

from typing import List
from .models import Task


def display_menu() -> None:
    """Display the main menu options to the user."""
    print("\n" + "="*40)
    print("TODO APPLICATION - MAIN MENU")
    print("="*40)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Search Tasks")
    print("7. Filter Tasks")
    print("8. Sort Tasks")
    print("9. Exit")
    print("-"*40)


def get_user_choice() -> str:
    """
    Get the user's menu choice.

    Returns:
        The user's choice as a string
    """
    return input("Enter your choice (1-9): ").strip()


def display_tasks(tasks: List[Task]) -> None:
    """
    Display all tasks in a formatted way.

    Args:
        tasks: List of tasks to display
    """
    if not tasks:
        print("\nNo tasks found.")
        return

    print(f"\n{'ID':<3} {'Status':<8} {'Priority':<8} {'Tags':<15} {'Title':<20} {'Description'}")
    print("-" * 80)

    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        title = task.title[:17] + "..." if len(task.title) > 20 else task.title
        description = task.description[:30] + "..." if len(task.description) > 30 else task.description

        # Ensure task.tags is a list before processing
        task_tags = task.tags if isinstance(task.tags, list) else []

        # Create tags string representation
        if task_tags:
            if len(task_tags) > 2:
                tags_str = ",".join(str(tag) for tag in task_tags[:2]) + "..."
            else:
                tags_str = ",".join(str(tag) for tag in task_tags)
        else:
            tags_str = "None"

        print(f"{task.id:<3} {status:<8} {task.priority:<8} {tags_str:<15} {title:<20} {description}")


def get_task_input(is_update: bool = False) -> tuple:
    """
    Get task details from user input.

    Args:
        is_update: Whether this is for an update operation (makes fields optional)

    Returns:
        A tuple containing (title, description, priority, tags) entered by the user
    """
    if is_update:
        print("Leave blank to keep current value")
        title = input("Enter new title (or press Enter to keep current): ").strip()
        title = title if title else None
        description = input("Enter new description (or press Enter to keep current): ").strip()
        description = description if description else None
    else:
        title = input("Enter task title: ").strip()
        description = input("Enter task description: ").strip()

    # Get priority
    if not is_update or (is_update and input("Update priority? (y/n): ").strip().lower() == 'y'):
        while True:
            priority = input("Enter priority (high/medium/low) [default: medium]: ").strip().lower()
            if priority in ["", "high", "medium", "low"]:
                if priority == "":
                    priority = "medium"
                break
            else:
                print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    else:
        priority = None

    # Get tags
    if not is_update or (is_update and input("Update tags? (y/n): ").strip().lower() == 'y'):
        tags_input = input("Enter tags separated by commas (e.g., work,urgent): ").strip()
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        else:
            tags = []
    else:
        tags = None

    return title, description, priority, tags


def get_task_id(prompt: str = "Enter task ID: ") -> int:
    """
    Get a task ID from user input with validation.

    Args:
        prompt: The prompt to display to the user

    Returns:
        The task ID as an integer
    """
    while True:
        try:
            task_id = int(input(prompt).strip())
            if task_id > 0:
                return task_id
            else:
                print("Task ID must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def display_message(message: str) -> None:
    """
    Display a message to the user.

    Args:
        message: The message to display
    """
    print(f"\n{message}")


def get_completion_status() -> bool:
    """
    Get the completion status from user input.

    Returns:
        True if the task should be marked as complete, False if incomplete
    """
    while True:
        status = input("Mark as complete (c) or incomplete (i)? ").strip().lower()
        if status in ['c', 'complete']:
            return True
        elif status in ['i', 'incomplete']:
            return False
        else:
            print("Please enter 'c' for complete or 'i' for incomplete.")


def get_search_keyword() -> str:
    """
    Get the search keyword from user input.

    Returns:
        The keyword to search for
    """
    return input("Enter keyword to search: ").strip()


def get_filter_criteria() -> tuple:
    """
    Get filter criteria from user input.

    Returns:
        A tuple containing (status, priority, tags) for filtering
    """
    print("Leave blank to skip filtering by that criterion")

    # Get status filter
    status_input = input("Filter by status (complete/incomplete) or press Enter to skip: ").strip().lower()
    if status_input == "complete":
        status = True
    elif status_input == "incomplete":
        status = False
    elif status_input == "":
        status = None
    else:
        print("Invalid status. Skipping status filter.")
        status = None

    # Get priority filter
    priority = input("Filter by priority (high/medium/low) or press Enter to skip: ").strip().lower()
    if priority not in ["high", "medium", "low", ""]:
        print("Invalid priority. Skipping priority filter.")
        priority = None
    elif priority == "":
        priority = None

    # Get tags filter
    tags_input = input("Filter by tags (comma-separated) or press Enter to skip: ").strip()
    if tags_input:
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
    else:
        tags = None

    return status, priority, tags


def get_sort_criteria() -> str:
    """
    Get sort criteria from user input.

    Returns:
        The criteria to sort by
    """
    print("Sort by:")
    print("1. Priority")
    print("2. Title")
    print("3. Due date (not implemented yet)")

    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            return "priority"
        elif choice == "2":
            return "title"
        elif choice == "3":
            return "due_date"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")