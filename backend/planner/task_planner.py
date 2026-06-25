class TaskPlanner:

    def generate_plan(self, task: str) -> list[str]:

        task = task.lower()

        if "employee" in task:
            return [
                "Analyze employee requirements",
                "Design database schema",
                "Create Pydantic models",
                "Implement CRUD APIs",
                "Add validation",
                "Write unit tests"
            ]

        elif "e-commerce" in task or "ecommerce" in task:
            return [
                "Design product catalog",
                "Implement user authentication",
                "Develop shopping cart",
                "Integrate payment gateway",
                "Create order management",
                "Write integration tests"
            ]

        elif "chatbot" in task:
            return [
                "Choose LLM",
                "Design prompt pipeline",
                "Implement chat API",
                "Add conversation memory",
                "Build frontend",
                "Deploy application"
            ]

        else:
            return [
                "Analyze requirements",
                "Design architecture",
                "Generate code",
                "Write tests",
                "Validate output"
            ]