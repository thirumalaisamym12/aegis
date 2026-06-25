from backend.planner.task_planner import TaskPlanner

planner = TaskPlanner()

tasks = [
    "Build Employee Management API",
    "Build E-commerce Website",
    "Build AI Chatbot",
    "Build School Management System"
]

for task in tasks:
    print()
    print("Task:", task)
    print("Plan:")

    plan = planner.generate_plan(task)

    for step in plan:
        print("-", step)