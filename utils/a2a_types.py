from enum import Enum
from pydantic import BaseModel
from typing import List, Optional


class AgentSkill(str, Enum):
    CREATE_ORDER = "create_order"
    SEND_NOTIFICATION = "send_notification"
    HANDLE_JWKS = "handle_jwks"


class AgentCapabilities(BaseModel):
    skills: List[AgentSkill]


class AgentAuthentication(BaseModel):
    api_key: str
    jwks_url: Optional[str] = None


class AgentCard(BaseModel):
    id: str
    name: str
    description: str
    capabilities: AgentCapabilities
    authentication: AgentAuthentication
