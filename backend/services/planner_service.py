from backend.services.llm_service import LLMService
from backend.prompts.planner_prompt import PLANNER_PROMPT
from backend.parsers.planner_parser import PlannerParser

class PlannerService:

    def __init__(self):
        self.llm = LLMService()

    def generate_plan(
        self,
        task: str
    ) -> list[str]:

        prompt = PLANNER_PROMPT.format(
            task=task
        )

        response = self.llm.generate(prompt)

        return PlannerParser.parse(response)