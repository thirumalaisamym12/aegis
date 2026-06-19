from backend.agents.base_agent import BaseAgent
from backend.graph.state import AgentState
from backend.models.agent_response import AgentResponse


class CodeAgent(BaseAgent):

    def __init__(self):
        super().__init__("Code")

    def execute(
        self,
        state: AgentState
    ) -> AgentResponse:

        research = state["research"]

        requirements = research["requirements"]
        technologies = research["technologies"]

        files = [
            "main.py",
            "routes.py",
            "models.py",
            "schemas.py"
        ]

        return AgentResponse(
            success=True,
            agent_name=self.name,
            content="Code generation completed.",
            confidence=0.95,
            next_agent="validator",
            metadata={
                "requirements": requirements,
                "technologies": technologies,
                "files": files,
                "framework": "FastAPI",
                "database": "MySQL"
            }
        )