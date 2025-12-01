from flask import Flask
import logging

class A2AServer:
    def __init__(self, agent_card, task_manager, agent, notification_sender_auth,from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

from .a2a_types import AgentCard, AgentCapabilities, AgentAuthentication, AgentSkill
from .task_manager import AgentTaskManager, InvokeRequest, InvokeResponse

class A2AServer:
    def __init__(self, agent_card: AgentCard, task_manager: AgentTaskManager, notification_sender_auth_router):
        self.app = FastAPI(title="A2A Agent Server")
        self.agent_card = agent_card
        self.task_manager = task_manager

        # endpoints
        @self.app.get("/")
        async def root():
            return {"status": "ok", "agent": self.agent_card.model_dump()}

        # well-known/jwks.json comes from notification sender auth router
        self.app.include_router(notification_sender_auth_router)

        # A2A invoke endpoint (POST /invoke)
        class InvokeBody(BaseModel):
            query: str
            sessionId: str

        @self.app.post("/invoke", response_model=InvokeResponse)
        async def invoke(body: InvokeBody):
            # super-simple intent: if query contains "order" -> use create_burger_order
            # else ask for confirmation
            q = body.query.lower()
            if any(w in q for w in ["order", "buy", "get", "cheeseburger", "burger"]):
                # Parse a simple item name; real project should use a parser/LLM
                payload = {"order_items": [{"name": "Classic Cheeseburger", "quantity": 1, "price": 85000}]}
                return self.task_manager.invoke("create_burger_order", payload)
            else:
                return InvokeResponse(
                    status="input_required",
                    message="What would you like to order? (Classic, Double, Spicy Chicken, Spicy Cajun)"
                )

    def run(self, host: str = "0.0.0.0", port: int = 10001):
        uvicorn.run(self.app, host=host, port=port, log_level="info")

                 host="0.0.0.0", port=8080, auth_username="", auth_password=""):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.agent_card = agent_card
        self.task_manager = task_manager
        self.agent = agent
        self.notification_sender_auth = notification_sender_auth

    def start(self):
        logging.info(f"Starting A2A Server on {self.host}:{self.port}")
        self.app.run(host=self.host, port=self.port)
