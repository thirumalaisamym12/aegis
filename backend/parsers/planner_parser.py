import re


class PlannerParser:

    @staticmethod
    def parse(response: str) -> list[str]:

        steps = []

        for line in response.splitlines():

            line = line.strip()

            if re.match(r"^\d+\.", line):

                steps.append(line)

        return steps