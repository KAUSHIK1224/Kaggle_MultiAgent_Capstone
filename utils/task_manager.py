from typing import Any, Dict
from pydantic import BaseModel
from .task_manager_base import TaskManagerBase

class InvokeRequest(BaseModel):
    query: str
    sessionId: str

class InvokeResponse(BaseModel):
    status: str  # "input_required" | "error" | "completed"
    message: str

class AgentTaskManager(TaskManagerBase):
    def __init__(self):
        super().__init__()

    def invoke(self, tool_name: str, payload: Dict[str, Any]) -> InvokeResponse:
        tool = self.get(tool_name)
        if not tool:
            return InvokeResponse(status="error", message=f"Unknown tool: {tool_name}")
        try:
            msg = tool(**payload)
            return InvokeResponse(status="completed", message=msg)
        except Exception as e:
            return InvokeResponse(status="error", message=f"{e}")
