from backend.agents.supervisor.supervisor_agent import SupervisorAgent
from backend.agents.research.research_agent import ResearchAgent


supervisor_agent = SupervisorAgent()
research_agent = ResearchAgent()


def supervisor_node(state):

    response = supervisor_agent.execute(state)

    state["current_agent"] = "supervisor"

    state["next_agent"] = response.next_agent

    state["plan"] = response.metadata["plan"]

    return state


def research_node(state):

    response = research_agent.execute(state)

    state["current_agent"] = "research"

    state["next_agent"] = response.next_agent

    state["research"] = response.metadata

    return state