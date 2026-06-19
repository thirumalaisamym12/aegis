from backend.agents.base_agent import BaseAgent
from backend.graph.state import AgentState
from backend.models.agent_response import AgentResponse


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__("Research")

    def execute(
        self,
        state: AgentState
    ) -> AgentResponse:

        requirements = [
            "CRUD operations",
            "Employee table",
            "REST API endpoints",
            "Validation",
            "Error handling"
        ]

        technologies = [
            "FastAPI",
            "Pydantic",
            "MySQL"
        ]

        constraints = [
            "Follow REST standards",
            "Use Python 3.12"
        ]

        return AgentResponse(
            success=True,
            agent_name=self.name,
            content="Research completed.",
            confidence=0.95,
            next_agent="code",
            metadata={
                "requirements": requirements,
                "technologies": technologies,
                "constraints": constraints
            }
        )