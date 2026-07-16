{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "25a82f8b",
   "metadata": {},
   "source": [
    "# LangGraph Conditional Edges (Odd or Even)\n",
    "This notebook shows how to route execution using `add_conditional_edges()` based on whether a number is odd or even."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d153387",
   "metadata": {
    "vscode": {
     "languageId": "code"
    }
   },
   "outputs": [],
   "source": [
    "from langgraph.graph import StateGraph, START, END\n",
    "from typing_extensions import TypedDict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73b2d097",
   "metadata": {},
   "outputs": [],
   "source": [
    "class NumberState(TypedDict):\n",
    "    number: int\n",
    "    parity: str\n",
    "    result: str\n",
    "\n",
    "\n",
    "def check_number(state: NumberState):\n",
    "    number = state[\"number\"]\n",
    "    parity = \"even\" if number % 2 == 0 else \"odd\"\n",
    "    print(f\"Checking number {number} -> {parity}\")\n",
    "    return {**state, \"parity\": parity}\n",
    "\n",
    "\n",
    "def even_node(state: NumberState):\n",
    "    print(\"Even node executed\")\n",
    "    return {**state, \"result\": f\"{state['number']} is EVEN\"}\n",
    "\n",
    "\n",
    "def odd_node(state: NumberState):\n",
    "    print(\"Odd node executed\")\n",
    "    return {**state, \"result\": f\"{state['number']} is ODD\"}\n",
    "\n",
    "\n",
    "def route_by_parity(state: NumberState):\n",
    "    return state[\"parity\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bd50fa0",
   "metadata": {},
   "outputs": [],
   "source": [
    "builder = StateGraph(NumberState)\n",
    "builder.add_node(\"check_number\", check_number)\n",
    "builder.add_node(\"even_node\", even_node)\n",
    "builder.add_node(\"odd_node\", odd_node)\n",
    "\n",
    "builder.add_edge(START, \"check_number\")\n",
    "builder.add_conditional_edges(\n",
    "    \"check_number\",\n",
    "    route_by_parity,\n",
    "    {\n",
    "        \"even\": \"even_node\",\n",
    "        \"odd\": \"odd_node\",\n",
    "    },\n",
    ")\n",
    "builder.add_edge(\"even_node\", END)\n",
    "builder.add_edge(\"odd_node\", END)\n",
    "\n",
    "graph = builder.compile()\n",
    "\n",
    "for value in [1, 2, 7, 10]:\n",
    "    print(\"\\n---\")\n",
    "    output = graph.invoke({\"number\": value, \"parity\": \"\", \"result\": \"\"})\n",
    "    print(output[\"result\"])"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
