from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool,Tool
from langchain_ollama import ChatOllama
from langgraph.graph import START, StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain.agents import create_agent


@tool
def add(a: int, b: int) -> dict:
    """Add two numbers together."""
    return {"answer": a + b}

@tool
def sub(a: int, b: int) -> dict:
    """Subtract second number from first number."""
    return {"answer": a - b}


TOOLS = [add, sub]


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


llm = ChatOllama(
    model="gemma4:latest",
    base_url="http://192.168.0.119:11434",
    temperature=0,
)
llm_with_tools = llm.bind_tools(TOOLS)

# agent=create_agent(model=llm,tools=TOOLS,prompt="You are a simple bot")

def assistant_node(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])
    print("tool calls made on this assistant now",response.tool_calls)
    return {"messages": [response]}


builder = StateGraph(AgentState)
builder.add_node("assistant", assistant_node)
builder.add_node("tools", ToolNode(TOOLS))

builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")
builder.add_edge("assistant", END)

graph = builder.compile()


def run_agent(user_query: str):
    return graph.invoke(
        {
            "messages": [
                SystemMessage(
                    content=(
                        "You are a math assistant. Use tool calls for arithmetic. "
                        "Use add for addition and sub for subtraction."
                    )
                ),
                HumanMessage(content=user_query),
            ]
        }
    )


if __name__ == "__main__":
    prompts = [
        "Add 12 and 8.",
        "Subtract 8 from 12.",
        "Add 101 and 299, then subtract 50 from that result.",
    ]

    for prompt in prompts:
        print("\n---")
        print(f"User: {prompt}")
        result = run_agent(prompt)
        print(f"Assistant: {result['messages'][-1].content}")
