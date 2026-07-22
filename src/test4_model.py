from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START
from pydantic import BaseModel, Field
from typing import Annotated, Sequence
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class AgentState(BaseModel):
    messages: Annotated[Sequence[BaseMessage], add_messages] = Field(default_factory=list)

def create_llm():
    return ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        model=os.getenv("MODEL_NAME", "qwen3.7-plus")
    )

def llm_node(state: AgentState):
    response = create_llm().invoke(state.messages)
    return {"messages": [response]}

builder = StateGraph(AgentState)
builder.add_node("llm", llm_node)
builder.add_edge(START, "llm")

graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke({"messages": [("user", "你好，请介绍一下自己")]})
    print(result["messages"][-1].content)
