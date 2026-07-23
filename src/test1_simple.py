from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel

class State(BaseModel):
    mes: str
    num: int = 5

def node1(state: State):
    state.mes = state.mes + " World"
    state.num = state.num + 1
    return state

def node2(state: State):
    state.mes = state.mes + " LangGraph"
    state.num = state.num * 2
    return state

builder = StateGraph(State)

builder.add_node("node1", node1)
builder.add_node("node2", node2)

builder.add_edge(START, "node1")
builder.add_edge("node1", "node2")
builder.add_edge("node2", END)

graph = builder.compile()

if __name__ == "__main__":
    state = State(mes="Hello")
    result = graph.invoke(state)
    print(result)
