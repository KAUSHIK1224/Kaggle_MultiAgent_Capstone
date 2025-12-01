from flask import Flask
import logging

class A2AServer:
    def __init__(self, agent_card, task_manager, agent, notification_sender_auth,
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
