from typing import List
from pydantic import BaseModel


class AgentSkill:
    CREATE_ORDER = "create_order"
    GET_STATUS = "get_status"


class AgentCapabilities(BaseModel):
    skills: List[str]
    supportedContentTypes: List[str]
    supportedOutputTypes: List[str]


class AgentAuthentication(BaseModel):
    api_key: str


class AgentCard(BaseModel):
    id: str
    name: str
    description: str
    capabilities: AgentCapabilities
    authentication: AgentAuthentication
