from typing import List, Optional
from pydantic import BaseModel


class AgentSkill:
    CREATE_ORDER = "CREATE_ORDER"
    SEARCH = "SEARCH"
    ANSWER = "ANSWER"


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
    authentication: Optional[AgentAuthentication] = None
