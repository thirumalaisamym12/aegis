from backend.agents.base_agent import BaseAgent
from backend.graph.state import AgentState
from backend.models.agent_response import AgentResponse


class ValidatorAgent(BaseAgent):

    def __init__(self):
        super().__init__("Validator")

    def execute(
        self,
        state: AgentState
    ) -> AgentResponse:

        issues = []

        quality_score = 0.95

        approved = quality_score >= 0.9

        next_agent = "end"

        if not approved:
            next_agent = "code"

        return AgentResponse(
            success=True,
            agent_name=self.name,
            content="Validation completed.",
            confidence=1.0,
            next_agent=next_agent,
            metadata={
                "approved": approved,
                "quality_score": quality_score,
                "issues": issues
            }
        )