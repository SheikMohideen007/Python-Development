from langchain_mcp_adapters.client import MultiServerMCPClient


def getMCPTools():
    client = MultiServerMCPClient({
        "Personal Info Server": {
            "transport": "stdio",
            "command": "python",
            "args": ["mcp/mcp_server/personal_info.py"],
        },
        "Math_server": {
            "transport": "stdio",
            "command": "python",
            "args": ["mcp/mcp_server/math.py"],
        },
        "Weather Server": {
            "transport": "streamable_http",
            "url": "http://127.0.0.1:9090/",
        },
    })
    return client
