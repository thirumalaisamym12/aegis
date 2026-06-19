from backend.agents.supervisor.supervisor_agent import SupervisorAgent


state = {
    "task": "Build Employee Management API",

    "plan": [],

    "current_step": "",

    "current_agent": "",

    "next_agent": "",

    "messages": [],

    "memories": [],

    "confidence": 1.0,

    "quality_score": 1.0,

    "status": "started"
}


agent = SupervisorAgent()

response = agent.execute(state)

print()

print("Agent:", response.agent_name)

print("Content:", response.content)

print("Confidence:", response.confidence)

print("Next Agent:", response.next_agent)

print()

print("Plan:")

for step in response.metadata["plan"]:
    print("-", step)