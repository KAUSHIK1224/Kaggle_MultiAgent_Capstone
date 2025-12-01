import json
import logging
from typing import Optional
from pydantic import BaseModel


class PushNotificationSenderAuth(BaseModel):
    api_key: str
    jwks_url: Optional[str] = None

    def handle_jwks_endpoint(self):
        from flask import jsonify
        return jsonify({"jwks": "placeholder"})


class NotificationSenderAuth(BaseModel):
    api_key: str

    def validate(self, key: str) -> bool:
        return key == self.api_key

