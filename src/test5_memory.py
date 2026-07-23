from langgraph.graph import StateGraph, START
from pydantic import BaseModel, Field
from typing import Annotated, Sequence
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from src.test4_model import llm_node

class AgentState(BaseModel):
    messages: Annotated[Sequence[BaseMessage], add_messages] = Field(default_factory=list)

builder = StateGraph(AgentState)
builder.add_node("llm", llm_node)
builder.add_edge(START, "llm")

"""
测试多轮对话记忆，通过同一个thread_id来实现对话记忆
"""
memory_saver = MemorySaver()
graph = builder.compile(checkpointer=memory_saver)

thread_config = {"configurable": {"thread_id": "session_1"}}

if __name__ == "__main__":
    state1 = graph.invoke({"messages": [("user", "你好，我是张三")]}, config=thread_config)
    print(state1["messages"][-1].content)
    state2 = graph.invoke({"messages": [("user", "你还记得我叫什么吗")]}, config=thread_config)
    print(state2["messages"][-1].content)
    ## 测试不同的thread_id，是否能实现不同的对话记忆
    state3 = graph.invoke({"messages": [("user", "你还记得我叫什么吗")]}, config={"configurable": {"thread_id": "session_2"}})
    print(state3["messages"][-1].content)
    ## 查看session_1的对话记忆
    print(graph.get_state(thread_config).values["messages"])
