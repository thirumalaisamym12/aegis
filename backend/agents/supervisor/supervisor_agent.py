from backend.agents.base_agent import BaseAgent
from backend.graph.state import AgentState
from backend.models.agent_response import AgentResponse
from backend.planner.task_planner import TaskPlanner


class SupervisorAgent(BaseAgent):

    def __init__(self):
        super().__init__("Supervisor")
        self.planner = TaskPlanner()

    def execute(
        self,
        state: AgentState
    ) -> AgentResponse:

        task = state["task"]

        plan = self.planner.generate_plan(task)

        return AgentResponse(
            success=True,
            agent_name=self.name,
            content=f"Generated dynamic plan for: {task}",
            confidence=1.0,
            next_agent="research",
            metadata={
                "plan": plan
            }
        )