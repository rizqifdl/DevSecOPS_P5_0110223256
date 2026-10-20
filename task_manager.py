"""Core task-management operations."""
from pathlib import Path
from storage import load_tasks, save_tasks
from validators import validate_title

class TaskManager:
    def __init__(self, storage_path: Path = Path("tasks.json")):
        self.storage_path = storage_path

    def list_tasks(self) -> list[dict]:
        return load_tasks(self.storage_path)

    def add_task(self, title: str) -> dict:
        cleaned = validate_title(title)
        tasks = self.list_tasks()
        task = {"id": max((item.get("id", 0) for item in tasks), default=0) + 1,
                "title": cleaned, "completed": False}
        tasks.append(task)
        save_tasks(tasks, self.storage_path)
        return task

    def complete_task(self, task_id: int) -> dict:
        tasks = self.list_tasks()
        for task in tasks:
            if task.get("id") == task_id:
                task["completed"] = True
                save_tasks(tasks, self.storage_path)
                return task
        raise KeyError(f"Task with id {task_id} was not found.")
