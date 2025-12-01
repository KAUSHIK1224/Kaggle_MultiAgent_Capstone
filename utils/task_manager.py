import logging
from typing import List
from pydantic import BaseModel

class AgentTask(BaseModel):
    id: str
    agent_id: str
    payload: dict
    status: str = "created"


class AgentTaskManager:
    def __init__(self):
        self.tasks: List[AgentTask] = []

    def add_task(self, task: AgentTask):
        self.tasks.append(task)
        logging.info(f"Task added: {task.id}")

    def get_pending(self, agent_id: str):
        return [t for t in self.tasks if t.agent_id == agent_id and t.status == "created"]

    def mark_completed(self, task_id: str):
        for t in self.tasks:
            if t.id == task_id:
                t.status = "completed"
                logging.info(f"Task completed: {task_id}")
                return True
        return False
