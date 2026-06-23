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
    "code": {},
    "validation": {},
    "retry_count": 0,
    "max_retries": 3,
}

result = app.invoke(initial_state)

print()
print("Current Agent:", result["current_agent"])
print()
print("Approved:", result["validation"]["approved"])
print("Quality Score:", result["validation"]["quality_score"])
print()
print("Issues:")
for issue in result["validation"]["issues"]:
    print("-", issue)

    print()
print("Execution History:")

for message in result["messages"]:
    print("-", message)