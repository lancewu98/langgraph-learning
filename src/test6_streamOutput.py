from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START
from pydantic import BaseModel, Field
from typing import Annotated, Sequence
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from src.test4_model import llm_node,create_llm

class AgentState(BaseModel):
    messages: Annotated[Sequence[BaseMessage], add_messages] = Field(default_factory=list)

# 创建图
builder = StateGraph(AgentState)
builder.add_node("llm", llm_node)
builder.add_edge(START, "llm")
graph = builder.compile()

if __name__ == "__main__":
    print("--- 普通输出 ---")
    result = graph.invoke({"messages": [("user", "你好，请介绍一下自己")]})
    print(result["messages"][-1].content)
    
    print("\n--- 流式输出 ---")
    # 直接使用 LLM 的流式功能
    full_response = ""
    for chunk in create_llm().stream([("user", "你好，请介绍一下自己")]):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content
    print()
