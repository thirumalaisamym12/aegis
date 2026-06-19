from langgraph.graph import StateGraph, END

from backend.graph.state import AgentState
from backend.graph.nodes import (
    supervisor_node,
    research_node
)


workflow = StateGraph(AgentState)

workflow.add_node(
    "supervisor",
    supervisor_node
)

workflow.add_node(
    "research",
    research_node
)

workflow.set_entry_point("supervisor")

workflow.add_edge(
    "supervisor",
    "research"
)

workflow.add_edge(
    "research",
    END
)

app = workflow.compile()