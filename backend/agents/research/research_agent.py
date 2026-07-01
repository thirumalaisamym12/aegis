from backend.agents.base_agent import BaseAgent
from backend.graph.state import AgentState
from backend.models.agent_response import AgentResponse
from backend.services.research_service import ResearchService

class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__("Research")
        self.research_service = ResearchService()

    def execute(
        self,
        state: AgentState
    ) -> AgentResponse:

        task = state["task"]
        plan = state["plan"]
        research = self.research_service.analyze(
            task,
            plan
            )

        return AgentResponse(
            success=True,
            agent_name=self.name,
            content="AI research completed.",
            confidence=0.95,
            next_agent="code",
            metadata=research
)
    