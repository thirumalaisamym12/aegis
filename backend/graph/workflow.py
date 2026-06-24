from langgraph.graph import StateGraph, END

from backend.graph.state import AgentState
from backend.graph.nodes import (
    supervisor_node,
    research_node,
    code_node,
    validator_node,
    reflection_node
)


def should_continue(state: AgentState):

    approved = state["validation"]["approved"]

    retry_count = state["retry_count"]

    max_retries = state["max_retries"]

    if approved:
        return "end"

    if retry_count < max_retries:
        return "reflection"

    return "end"


workflow = StateGraph(AgentState)

workflow.add_node(
    "supervisor",
    supervisor_node
)

workflow.add_node(
    "research",
    research_node
)

workflow.add_node(
    "code",
    code_node
)

workflow.add_node(
    "validator",
    validator_node
)

workflow.add_node(
    "reflection",
    reflection_node
)

workflow.set_entry_point(
    "supervisor"
)

workflow.add_edge(
    "supervisor",
    "research"
)

workflow.add_edge(
    "research",
    "code"
)

workflow.add_edge(
    "code",
    "validator"
)

workflow.add_edge(
    "reflection",
    "code"
)

workflow.add_conditional_edges(
    "validator",
    should_continue,
    {
        "reflection": "reflection",
        "end": END
    }
)

app = workflow.compile()