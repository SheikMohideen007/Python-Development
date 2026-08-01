from mcp.server.fastmcp import FastMCP


personal_mcp=FastMCP("Personal Info Server")

@personal_mcp.tool()
def get_name():
    "Name of the user"
    return "Yogesh"

@personal_mcp.tool()
def get_team():
    return ["Bala","Sheik","Suresh"]

@personal_mcp.tool()
def get_height():
    return "6.1 FT"

@personal_mcp.tool()
def user_loves():
    "This is user, what loves"
    return "AVASOFT"


if __name__ =="__main__":
    personal_mcp.run(transport="stdio")