from pydantic import BaseModel


class TaskModel(BaseModel):
    task: str

    steps: list[str]

    priority: int = 1