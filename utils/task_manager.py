from typing import Dict, Any
from .task_manager_base import TaskManagerBase


class AgentTaskManager(TaskManagerBase):

    def __init__(self):
        super().__init__()

    def invoke(self, agent_id: str, user_query: str, session_id: str) -> Dict[str, Any]:

        payload = {
            "agent_id": agent_id,
            "user_query": user_query,
            "session_id": session_id
        }

        # Create Task
        task = self.create_task(payload)
        task_id = task["task_id"]

        # Execute Task
        result = self.execute_task(task_id)
        return result
