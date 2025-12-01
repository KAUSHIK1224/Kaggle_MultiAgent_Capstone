from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse
import uvicorn
from .task_manager import AgentTaskManager
from .a2a_types import AgentCard
import json


class A2AServer:
    def __init__(
        self,
        agent_card: AgentCard,
        task_manager: AgentTaskManager,
        api_base="http://0.0.0.0:10001",
        host="0.0.0.0",
        port=10001,
        auth_username=None,
        auth_password=None
    ):

        self.agent_card = agent_card
        self.task_manager = task_manager
        self.api_base = api_base

        self.host = host
        self.port = port

        self.auth = HTTPBasic()
        self.auth_username = auth_username
        self.auth_password = auth_password

        self.app = FastAPI()
        self._setup_routes()

    def _verify_auth(self, creds: HTTPBasicCredentials):
        if self.auth_username is None:
            return
        if creds.username != self.auth_username or creds.password != self.auth_password:
            raise HTTPException(status_code=401, detail="Invalid credentials")

    def _setup_routes(self):

        @self.app.get("/agent")
        def get_agent():
            return self.agent_card

        @self.app.get("/jwks.json")
        def jwks():
            return {"keys": []}

        @self.app.post("/task/{agent_id}/{task_id}")
        def post_task(agent_id: str, task_id: str, body: dict,
                      creds: HTTPBasicCredentials = Depends(self.auth)):

            self._verify_auth(creds)

            result = {
                "status": "completed",
                "agent_id": agent_id,
                "task_id": task_id,
                "response": f"Agent received: {body}"
            }

            return JSONResponse(result)

    def start(self):
        uvicorn.run(self.app, host=self.host, port=self.port)
