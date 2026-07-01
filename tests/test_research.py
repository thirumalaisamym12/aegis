from backend.agents.research.research_agent import ResearchAgent
from backend.services.planner_service import PlannerService

planner = PlannerService()

task = "Build Employee Management API"

plan = planner.generate_plan(task)

state = {
    "task": task,
    "plan": plan
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