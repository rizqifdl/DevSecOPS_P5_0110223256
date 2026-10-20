"""Small JSON storage layer for task data."""
import json
from pathlib import Path
from typing import Any

DEFAULT_PATH = Path("tasks.json")

def load_tasks(path: Path = DEFAULT_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise ValueError("Could not read task storage file.") from exc
    if not isinstance(data, list):
        raise ValueError("Task storage must contain a JSON list.")
    return data

def save_tasks(tasks: list[dict[str, Any]], path: Path = DEFAULT_PATH) -> None:
    path.write_text(json.dumps(tasks, indent=2, ensure_ascii=False), encoding="utf-8")
