class ResearchParser:

    @staticmethod
    def parse(response: str) -> dict:

        result = {
            "requirements": [],
            "technologies": [],
            "architecture": [],
            "constraints": [],
            "risks": [],
            "best_practices": []
        }

        current_section = None

        for line in response.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            if "requirements" in lower:
                current_section = "requirements"
                continue

            elif "recommended technologies" in lower:
                current_section = "technologies"
                continue

            elif "architecture" in lower:
                current_section = "architecture"
                continue

            elif "constraints" in lower:
                current_section = "constraints"
                continue

            elif "risks" in lower:
                current_section = "risks"
                continue

            elif "best practices" in lower:
                current_section = "best_practices"
                continue

            if line.lstrip().startswith("-") and current_section:

                result[current_section].append(
                    line.lstrip("- ").strip()
                )

        return result