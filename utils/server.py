from fastapi import FastAPI
from starlette.responses import JSONResponse
import uvicorn


class A2AServer:

    def __init__(self, agent_card, task_manager, host="0.0.0.0", port=10001):
        self.agent_card = agent_card
        self.task_manager = task_manager
        self.host = host
        self.port = port

        self.app = FastAPI()
        self._setup_routes()

    def _setup_routes(self):
        @self.app.get("/agent")
        def get_agent():
            return self.agent_card.dict()

        @self.app.post("/task")
        def create_task(payload: dict):
            return self.task_manager.create_task(payload)

        @self.app.get("/task/{task_id}")
        def execute_task(task_id: str):
            return self.task_manager.execute_task(task_id)

    def start(self):
        uvicorn.run(self.app, host=self.host, port=self.port)
