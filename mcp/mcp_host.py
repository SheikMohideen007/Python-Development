from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from mcp_client.mcp_client import getMCPTools
import asyncio

ollama_model = ChatOllama(
    base_url='http://192.168.0.119:11434',
    model='gemma4:latest',
)

async def main():
    client = getMCPTools()
    mcp_tools =await client.get_tools()

    agent = create_agent(
        model=ollama_model,
        name="MCP Agent",
        tools=mcp_tools,
        system_prompt="You are a powerful and friendly AI Agent which answer the user query"
    )

    math_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what's (3 + 5) - 12?"}]}
        )
    weather_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what is the weather in chennai?"}]}
        )
    personal_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what is the name of the mine?"}]}
        )
    
    print(math_response)
    print(weather_response)
    print(personal_response)

if __name__ == "__main__":
    asyncio.run(main())


