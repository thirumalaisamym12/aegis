from abc import ABC, abstractmethod

from backend.graph.state import AgentState
from backend.models.agent_response import AgentResponse


class BaseAgent(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(
            self,
            state: AgentState
    ) -> AgentResponse:
        pass