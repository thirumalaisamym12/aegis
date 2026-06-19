from pydantic import BaseModel


class ResearchResponse(BaseModel):
    requirements: list[str]

    constraints: list[str]

    technologies: list[str]