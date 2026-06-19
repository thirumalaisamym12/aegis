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

    "research": {}
}


result = app.invoke(initial_state)

print()

print("Current Agent:", result["current_agent"])

print()

print("Plan")

for step in result["plan"]:
    print("-", step)

print()

print("Requirements")

for req in result["research"]["requirements"]:
    print("-", req)

print()

print("Technologies")

for tech in result["research"]["technologies"]:
    print("-", tech)