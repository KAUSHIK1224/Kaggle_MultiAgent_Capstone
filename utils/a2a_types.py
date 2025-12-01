from typing import Optional, Dict, Any
from pydantic import BaseModel


class AgentCapability(BaseModel):
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class AgentSkill(BaseModel):
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class AgentCard(BaseModel):
    agent_id: str
    agent_name: str
    capabilities: Optional[list[AgentCapability]] = None
    skills: Optional[list[AgentSkill]] = None
