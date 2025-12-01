import json
import logging
from flask import Flask, request, jsonify
from utils.a2a_types import AgentCard
from utils.task_manager import AgentTaskManager

class A2AServer:
    def __init__(self, agent, host="0.0.0.0", port=8000):
        self.agent = agent
        self.host = host
        self.port = port
        self.app = Flask(__name__)
        self.task_manager = AgentTaskManager()
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route("/agent/card", methods=["GET"])
        def get_card():
            return jsonify(self.agent.card.dict())

        @self.app.route("/agent/run", methods=["POST"])
        def run_agent():
            payload = request.json
            task = self.task_manager.create_task(payload)
            result = self.agent.run(task)
            self.task_manager.complete_task(task["id"], result)
            return jsonify(result)

    def start(self):
        logging.info(f"Starting server at {self.host}:{self.port}")
        self.app.run(host=self.host, port=self.port)
