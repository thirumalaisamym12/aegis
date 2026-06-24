from backend.agents.base_agent import BaseAgent
from backend.graph.state import AgentState
from backend.models.agent_response import AgentResponse


class ReflectionAgent(BaseAgent):

    def __init__(self):
        super().__init__("Reflection")

    def execute(
        self,
        state: AgentState
    ) -> AgentResponse:

        issues = state["validation"]["issues"]

        reflection = []

        for issue in issues:
            reflection.append(
                f"Improve: {issue}"
            )

        return AgentResponse(
            success=True,
            agent_name=self.name,
            content="Reflection completed.",
            confidence=1.0,
            next_agent="code",
            metadata={
                "reflection": reflection
            }
        )