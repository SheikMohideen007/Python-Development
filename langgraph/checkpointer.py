from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph


class PipelineState(TypedDict):
    input_value: int
    intermediate: int
    output: int
    next_step: str
    checkpoint_id: str


checkpointer = InMemorySaver()


def save_checkpoint(state: PipelineState) -> PipelineState:
    checkpointer.save(state["checkpoint_id"], state)
    return state


def step1(state: PipelineState) -> PipelineState:
    state["intermediate"] = state["input_value"] * 2
    state["next_step"] = "step2"
    return save_checkpoint(state)


def step2(state: PipelineState) -> PipelineState:
    state["intermediate"] += 3
    state["next_step"] = "step3"
    return save_checkpoint(state)


def step3(state: PipelineState) -> PipelineState:
    state["output"] = state["intermediate"] - 1
    state["next_step"] = "done"
    return save_checkpoint(state)


def dispatch(state: PipelineState) -> str:
    return state["next_step"]


def done(state: PipelineState) -> PipelineState:
    print("Pipeline complete")
    return state


builder = StateGraph(PipelineState)
builder.add_node("dispatch", dispatch)
builder.add_node("step1", step1)
builder.add_node("step2", step2)
builder.add_node("step3", step3)
builder.add_node("done", done)

builder.add_edge(START, "dispatch")
builder.add_conditional_edges(
    "dispatch",
    dispatch,
    {
        "step1": "step1",
        "step2": "step2",
        "step3": "step3",
        "done": "done",
    },
)

builder.add_edge("step1", "dispatch")
builder.add_edge("step2", "dispatch")
builder.add_edge("step3", "dispatch")
builder.add_edge("done", END)

graph = builder.compile()


def run_pipeline(input_value: int, checkpoint_id: str) -> PipelineState:
    starting_state: PipelineState = {
        "input_value": input_value,
        "intermediate": 0,
        "output": 0,
        "next_step": "step1",
        "checkpoint_id": checkpoint_id,
    }
    return graph.invoke(starting_state)


def resume_pipeline(checkpoint_id: str) -> PipelineState:
    state = checkpointer.load(checkpoint_id)
    return graph.invoke(state)


if __name__ == "__main__":
    print("--- Full pipeline run ---")
    final_state = run_pipeline(input_value=4, checkpoint_id="run1")
    print(f"Final output: {final_state['output']}\n")

    print("--- Resume from checkpoint after partial run ---")
    partial_state: PipelineState = {
        "input_value": 7,
        "intermediate": 0,
        "output": 0,
        "next_step": "step1",
        "checkpoint_id": "run2",
    }
    partial_state = step1(partial_state)
    partial_state = step2(partial_state)
    print("State saved after step2, now resuming from checkpoint...\n")
    resumed_state = resume_pipeline("run2")
    print(f"Resumed output: {resumed_state['output']}")
