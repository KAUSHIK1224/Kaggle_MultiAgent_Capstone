import uuid
from typing import Dict
from .task_manager_base import Task, TaskResult


class AgentTaskManager:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.results: Dict[str, TaskResult] = {}

    def create_task(self, task_type: str, payload) -> Task:
        task_id = str(uuid.uuid4())
        task = Task(task_id=task_id, task_type=task_type, payload=payload)
        self.tasks[task_id] = task
        return task

    def store_result(self, task_id: str, result, success=True, error_message=None):
        task_result = TaskResult(
            task_id=task_id,
            result=result,
            success=success,
            error_message=error_message
        )
        self.results[task_id] = task_result

    def get_result(self, task_id: str) -> TaskResult | None:
        return self.results.get(task_id)
