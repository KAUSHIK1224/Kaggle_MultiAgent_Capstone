from typing import Any
from pydantic import BaseModel


class Task(BaseModel):
    task_id: str
    task_type: str
    payload: Any


class TaskResult(BaseModel):
    task_id: str
    result: Any
    success: bool
    error_message: str | None = None
