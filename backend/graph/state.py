from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict):
    task: str

    plan: List[str]

    current_step: str

    current_agent: str

    next_agent: str

    messages: List[Dict[str, Any]]

    memory: List[Dict[str, Any]]

    confidence: float

    quality_score: float

    status: str

    research: Dict[str, Any]

    code: Dict[str, Any]

    validation: Dict[str, Any]

    retry_count: int
    
    max_retries: int

    reflection: Dict[str, Any]
    
    memory: List[Dict[str, Any]]