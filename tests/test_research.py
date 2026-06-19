from backend.agents.research.research_agent import ResearchAgent


state = {
    "task": "Build Employee Management API"
}

agent = ResearchAgent()

response = agent.execute(state)

print()

print("Agent:", response.agent_name)

print("Content:", response.content)

print("Next Agent:", response.next_agent)

print()

print("Requirements")

for req in response.metadata["requirements"]:
    print("-", req)

print()

print("Technologies")

for tech in response.metadata["technologies"]:
    print("-", tech)