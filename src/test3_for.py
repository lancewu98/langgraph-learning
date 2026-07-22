from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END

loopcount = 0
class LoopState(BaseModel):
    num: int = 0
  
def increment(loop_state: LoopState):
    global loopcount
    loopcount += 1
    loop_state.num += 8
    return loop_state

def isBreak(loop_state: LoopState):
    return loop_state.num >= 67

builder = StateGraph(LoopState)
builder.add_node("increment", increment)

builder.add_edge(START, "increment")
builder.add_conditional_edges("increment", isBreak, {
    True: END,
    False: "increment"
})

graph = builder.compile()
graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
result = graph.invoke(LoopState())
print(result)
print(loopcount)



