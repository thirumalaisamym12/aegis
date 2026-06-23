from backend.agents.supervisor.supervisor_agent import SupervisorAgent
from backend.agents.research.research_agent import ResearchAgent
from backend.agents.code.code_agent import CodeAgent
from backend.agents.validator.validator_agent import ValidatorAgent

supervisor_agent = SupervisorAgent()
research_agent = ResearchAgent()
code_agent = CodeAgent()
validator_agent = ValidatorAgent()

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

def code_node(state):
    response = code_agent.execute(state)
    state["current_agent"] = "code"
    state["next_agent"] = response.next_agent
    state["code"] = response.metadata
    return state

def validator_node(state):
    response = validator_agent.execute(state)
    state["current_agent"] = "validator"
    state["next_agent"] = response.next_agent
    state["validation"] = response.metadata
    return state