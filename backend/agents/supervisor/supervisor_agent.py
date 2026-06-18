from backend.agents.base_agent import BaseAgent
from backend.graph.state import AgentState
from backend.models.agent_response import AgentResponse


class SupervisorAgent(BaseAgent):

    def __init__(self):
        super().__init__("Supervisor")

    def execute(
            self,
            state: AgentState
    ) -> AgentResponse:

        return AgentResponse(
            success=True,
            agent_name=self.name,
            content="Task received.",
            confidence=1.0,
            next_agent="research"
        )
    