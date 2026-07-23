from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel
from typing import Optional

class State(BaseModel):
    num: int
    result: Optional[str] = None

def init(state: State):
    return state

def isEven(state: State):
    return state.num % 2 == 0

def handleEven(state: State):
    state.result = "这是一个偶数"
    return state

def handleOdd(state: State):
    state.result = "这是一个奇数"
    return state

builder = StateGraph(State)

builder.add_node("init", init)
builder.add_node("handleEven", handleEven)
builder.add_node("handleOdd", handleOdd)

builder.add_edge(START, "init")
builder.add_conditional_edges("init", isEven, {
    True: "handleEven",
    False: "handleOdd"
})
builder.add_edge("handleEven", END)
builder.add_edge("handleOdd", END)

graph = builder.compile()

if __name__ == "__main__":
    # 保存流程图到文件
    try:
        graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
        print("流程图已保存为 graph.png")
    except Exception as e:
        print(f"保存流程图时出错: {e}")
        print("提示: 可能需要安装 graphviz，请运行: brew install graphviz")

    num_input = input("请输入一个数字：")
    result = graph.invoke(State(num=int(num_input)))
    print(result)
