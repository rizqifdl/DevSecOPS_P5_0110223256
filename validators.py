"""Input validation helpers for SecureTask Manager."""

def validate_title(title: str) -> str:
    if not isinstance(title, str):
        raise ValueError("Task title must be text.")
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Task title cannot be empty.")
    if len(cleaned) > 120:
        raise ValueError("Task title must be 120 characters or fewer.")
    return cleaned
