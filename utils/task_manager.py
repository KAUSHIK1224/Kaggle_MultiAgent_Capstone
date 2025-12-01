from typing import Any, Dict
from pydantic import BaseModel
from .task_manager_base import TaskManagerBase
import requests
import json


class InvokeResponse(BaseModel):
    status: str
    message: str


class AgentTaskManager(TaskManagerBase):
    def __init__(self, api_base="http://0.0.0.0:10001"):
        super().__init__()
        self.api_base = api_base

    def run_task(self, agent_card, user_query, session_id):
        # build payload
        payload = {
            "query": user_query,
            "session_id": session_id
        }

        # create task
        task = self.create_task(payload)
        task_id = task["task_id"]

        # call server
        url = f"{self.api_base}/task/{agent_card.id}/{task_id}"
        headers = {"Authorization": f"Bearer {agent_card.authentication.api_key}"}

        r = requests.post(url, json=payload, headers=headers)
        result = r.json()

        # update task
        self.update_task(task_id, result)

        return result
