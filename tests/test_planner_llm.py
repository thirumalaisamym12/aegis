from backend.services.planner_service import PlannerService

planner = PlannerService()

plan = planner.generate_plan(
    "Build Employee Management API"
)

print()

print("Generated Plan:")

for step in plan:
    print("-", step)