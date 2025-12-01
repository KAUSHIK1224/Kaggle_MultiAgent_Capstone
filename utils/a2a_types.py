from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

class AgentSkill(str, Enum):
    CREATE_ORDER = "create_order"
    SEND_NOTIFICATION = "send_notification"
    HANDLE_JWKS = "handle_jwks"

class AgentCapabilities(BaseModel):
    skills: List[AgentSkill]
    # ADK often validates these; keep them present but optional
    supportedContentTypes: Optional[List[str]] = None
    supportedOutputModes: Optional[List[str]] = None
    # This field was missing in your earlier run and caused a validation error
    pushNotifications: bool = True

class AgentAuthentication(BaseModel):
    api_key: str
    jwks_url: Optional[str] = None

class AgentCard(BaseModel):
    id: str
    name: str
    description: str
    capabilities: AgentCapabilities
    authentication: AgentAuthentication
