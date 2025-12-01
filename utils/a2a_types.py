from typing import List
from pydantic import BaseModel


class AgentSkill:
    CREATE_ORDER = "CREATE_ORDER"


class AgentCapabilities(BaseModel):
    skills: List[str]
    supportedContentTypes: List[str]
    supportedOutputTypes: List[str]


class AgentCard(BaseModel):
    id: str
    name: str
    description: str
    capabilities: AgentCapabilities
    authentication: dict
