from backend.graph.workflow import app


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
    "code": {}
}

result = app.invoke(initial_state)

print()

print("Current Agent:", result["current_agent"])

print()

print("Generated Files:")

for file in result["code"]["files"]:
    print("-", file)

print()

print("Framework:", result["code"]["framework"])

print("Database:", result["code"]["database"])