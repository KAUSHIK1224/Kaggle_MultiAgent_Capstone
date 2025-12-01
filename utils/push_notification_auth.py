from typing import Optional
from pydantic import BaseModel


class NotificationSenderAuth(BaseModel):
    sender_id: str
    auth_token: str
    endpoint: Optional[str] = None

    def is_valid(self) -> bool:
        return self.sender_id is not None and self.auth_token is not None
