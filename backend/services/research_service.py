from backend.services.llm_service import LLMService
from backend.prompts.research_prompt import RESEARCH_PROMPT
from backend.parsers.research_parser import ResearchParser


class ResearchService:

    def __init__(self):

        self.llm = LLMService()

    def analyze(
        self,
        task: str,
        plan: list[str]
    ) -> dict:

        prompt = RESEARCH_PROMPT.format(
            task=task,
            plan="\n".join(plan)
        )

        response = self.llm.generate(prompt)

        print("\n===== RAW LLM RESPONSE =====\n")
        print(response)
        print("\n============================\n")

        return ResearchParser.parse(response)