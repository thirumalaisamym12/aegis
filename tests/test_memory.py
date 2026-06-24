from backend.graph.workflow import app
from backend.memory.memory_store import get_memories


initial_state = {
    "task": "Build Employee Management API",
    "plan": [],
    "current_step": "",
    "current_agent": "",
    "next_agent": "",
    "messages": [],
    "memories": [],
    "confidence": 1.0,
    "quality_score": 1.0,
    "status": "started",
    "research": {},
    "code": {},
    "validation": {},
    "reflection": {},
    "memory": [],
    "retry_count": 0,
    "max_retries": 3
}

app.invoke(initial_state)

print()

print("Stored Memories:")

for memory in get_memories():

    print(memory)