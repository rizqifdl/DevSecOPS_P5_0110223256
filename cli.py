"""Command-line interface for SecureTask Manager."""
from task_manager import TaskManager

def run_cli() -> None:
    manager = TaskManager()
    print("SecureTask Manager")
    while True:
        print("\n1. List tasks  2. Add task  3. Complete task  4. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                tasks = manager.list_tasks()
                if not tasks:
                    print("No tasks yet.")
                for task in tasks:
                    status = "done" if task["completed"] else "pending"
                    print(f'{task["id"]}. {task["title"]} [{status}]')
            elif choice == "2":
                task = manager.add_task(input("Task title: "))
                print(f'Added task #{task["id"]}.')
            elif choice == "3":
                task = manager.complete_task(int(input("Task ID: ")))
                print(f'Task #{task["id"]} marked complete.')
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Please choose 1, 2, 3, or 4.")
        except (ValueError, KeyError) as exc:
            print(f"Error: {exc}")
