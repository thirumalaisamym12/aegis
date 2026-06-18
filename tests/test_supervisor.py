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

print(response)