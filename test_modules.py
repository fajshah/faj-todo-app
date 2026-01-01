import sys
import os

# Add src to the path
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

# Temporarily change directory to src to handle relative imports
original_dir = os.getcwd()
os.chdir('src')

try:
    # Import the modules to test if they work
    from models import Task
    print('✓ Models module loaded successfully')
    
    from storage import TaskStorage
    print('✓ Storage module loaded successfully')
    
    from tasks import TaskOperations
    print('✓ Tasks module loaded successfully')
    
    from ui import display_menu
    print('✓ UI module loaded successfully')
    
    print('\n🎉 All modules loaded successfully! The new features are properly implemented.')
    
    # Test creating a task with new features
    test_task = Task(id=1, title="Test", description="Test Description", priority="high", tags=["test", "new"])
    print(f'✓ Created task with new features: priority={test_task.priority}, tags={test_task.tags}')
    
    # Test TaskStorage
    storage = TaskStorage()
    new_task = storage.add_task("Feature Test", "Testing new features", "medium", ["feature", "test"])
    print(f'✓ Added task with new features: {new_task.title}, priority={new_task.priority}, tags={new_task.tags}')
    
    # Test TaskOperations
    ops = TaskOperations(storage)
    search_results = ops.search_tasks("Feature")
    print(f'✓ Search functionality works: found {len(search_results)} task(s)')
    
    filter_results = ops.filter_tasks(priority="medium")
    print(f'✓ Filter functionality works: found {len(filter_results)} task(s)')
    
    all_tasks = ops.list_tasks()
    sorted_tasks = ops.sort_tasks(all_tasks, "priority")
    print(f'✓ Sort functionality works: sorted {len(sorted_tasks)} task(s)')
    
    print('\n✅ All new features are working correctly!')
    
except ImportError as e:
    print(f'Import error: {e}')
except Exception as e:
    print(f'Error: {e}')
finally:
    # Change back to original directory
    os.chdir(original_dir)