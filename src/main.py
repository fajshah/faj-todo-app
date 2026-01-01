"""
Todo In-Memory Console App
Main module

This module orchestrates the application flow and main loop.
"""

from .storage import TaskStorage
from .tasks import TaskOperations
from .ui import (
    display_menu, get_user_choice, display_tasks,
    get_task_input, get_task_id, display_message, get_completion_status,
    get_search_keyword, get_filter_criteria, get_sort_criteria
)


def main():
    """Main application entry point."""
    # Initialize components
    storage = TaskStorage()
    task_ops = TaskOperations(storage)
    print    ("ASSALAM-O-ALIKUM")
    print("Welcome to the Faj Todo In-Memory Console App!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            # Add Task
            title, description, priority, tags = get_task_input()
            result = task_ops.add_task(title, description, priority, tags)

            if result:
                display_message(f"Task '{result.title}' added successfully with ID {result.id}")
            else:
                display_message("Error: Task title cannot be empty or priority is invalid.")

        elif choice == '2':
            # View All Tasks
            tasks = task_ops.list_tasks()
            display_tasks(tasks)

        elif choice == '3':
            # Update Task
            if not task_ops.list_tasks():
                display_message("No tasks available to update.")
                continue

            task_id = get_task_id("Enter ID of task to update: ")
            task = task_ops.get_task(task_id)

            if not task:
                display_message(f"Task with ID {task_id} not found.")
                continue

            display_message(f"Current: Title='{task.title}', Description='{task.description}', Priority='{task.priority}', Tags={task.tags}")
            new_title, new_description, new_priority, new_tags = get_task_input(is_update=True)

            if task_ops.update_task(task_id, new_title, new_description, new_priority, new_tags):
                display_message(f"Task with ID {task_id} updated successfully.")
            else:
                display_message(f"Failed to update task with ID {task_id}.")

        elif choice == '4':
            # Delete Task
            if not task_ops.list_tasks():
                display_message("No tasks available to delete.")
                continue

            task_id = get_task_id("Enter ID of task to delete: ")

            if task_ops.delete_task(task_id):
                display_message(f"Task with ID {task_id} deleted successfully.")
            else:
                display_message(f"Task with ID {task_id} not found.")

        elif choice == '5':
            # Mark Task Complete/Incomplete
            if not task_ops.list_tasks():
                display_message("No tasks available to mark.")
                continue

            task_id = get_task_id("Enter ID of task to mark: ")
            task = task_ops.get_task(task_id)

            if not task:
                display_message(f"Task with ID {task_id} not found.")
                continue

            completed = get_completion_status()

            if task_ops.mark_task_complete(task_id, completed):
                status = "complete" if completed else "incomplete"
                display_message(f"Task with ID {task_id} marked as {status}.")
            else:
                display_message(f"Failed to update task with ID {task_id}.")

        elif choice == '6':
            # Search Tasks
            keyword = get_search_keyword()
            if keyword.strip():
                results = task_ops.search_tasks(keyword)
                if results:
                    print(f"\nSearch results for '{keyword}':")
                    display_tasks(results)
                else:
                    display_message(f"No tasks found matching '{keyword}'.")
            else:
                display_message("Search keyword cannot be empty.")

        elif choice == '7':
            # Filter Tasks
            status, priority, tags = get_filter_criteria()
            results = task_ops.filter_tasks(status, priority, tags)
            if results:
                print("\nFiltered tasks:")
                display_tasks(results)
            else:
                display_message("No tasks match the filter criteria.")

        elif choice == '8':
            # Sort Tasks
            if not task_ops.list_tasks():
                display_message("No tasks available to sort.")
                continue

            criteria = get_sort_criteria()
            all_tasks = task_ops.list_tasks()
            sorted_tasks = task_ops.sort_tasks(all_tasks, criteria)

            if criteria == "priority":
                display_message("Tasks sorted by priority (high → medium → low):")
            elif criteria == "title":
                display_message("Tasks sorted by title (alphabetically):")
            elif criteria == "due_date":
                display_message("Tasks sorted by due date:")

            display_tasks(sorted_tasks)

        elif choice == '9':
            # Exit
            display_message("Thank you for using the Todo App. Goodbye!")
            break

        else:
            display_message("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()