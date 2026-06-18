from pydantic import BaseModel


class AgentResponse(BaseModel):
    success: bool

    agent_name: str

    content: str

    confidence: float

    next_agent: str

    metadata: dict = {}