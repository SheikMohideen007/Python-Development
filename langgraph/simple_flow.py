from langgraph.graph import StateGraph, START, END
from langchain_core.tools import tool
from typing_extensions import TypedDict
from IPython.display import Image, display # pyright: ignore[reportMissingModuleSource]



# creating a global state for the graph
class GlobalState(TypedDict):
    task:dict


# creating nodes for the graph
def func1(state: GlobalState):
    print('Function 1 is executed here',state['task']['hello'])
    state['task']['func1']='here is a func1'
    return state

def func2(state: GlobalState):
    print('Function 2 is executed here',state['task']['func1'])
    state['task']['func2']='here is a func2'
    return state

builder=StateGraph(GlobalState)
builder.add_node("function1",func1)
builder.add_node("function2",func2)

builder.add_edge(START,"function1")
builder.add_edge("function1","function2")
builder.add_edge("function2",END)


graph=builder.compile()

graph.invoke({'task':{
    'hello':'world'
}})

graph_obj = graph.get_graph()
try:
    display(Image(graph_obj.draw_mermaid_png()))
except Exception as e:
    print(f"Mermaid PNG rendering failed: {e}")
    print("Fallback to Mermaid text:")
    print(graph_obj.draw_mermaid())


