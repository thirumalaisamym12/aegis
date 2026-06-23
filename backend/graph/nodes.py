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

    return {
        **state,
        "current_agent": "supervisor",
        "next_agent": response.next_agent,
        "plan": response.metadata["plan"]
    }


def research_node(state):
    response = research_agent.execute(state)

    return {
        **state,
        "current_agent": "research",
        "next_agent": response.next_agent,
        "research": response.metadata
    }


def code_node(state):

    response = code_agent.execute(state)

    messages = state["messages"].copy()

    messages.append(
        f"Code attempt #{state['retry_count'] + 1}"
    )

    return {
        **state,
        "messages": messages,
        "retry_count": state["retry_count"] + 1,
        "current_agent": "code",
        "next_agent": response.next_agent,
        "code": response.metadata
    }


def validator_node(state):

    response = validator_agent.execute(state)

    messages = state["messages"].copy()

    messages.append(
        f"Validator score = {response.metadata['quality_score']}"
    )

    return {
        **state,
        "messages": messages,
        "current_agent": "validator",
        "next_agent": response.next_agent,
        "validation": response.metadata
    }