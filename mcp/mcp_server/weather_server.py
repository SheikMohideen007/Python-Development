from fastapi import FastAPI, HTTPException
import uvicorn
from mcp.server.fastmcp import FastMCP


weather_mcp=FastMCP("Weather Server")

app=FastAPI(title="Weather Server")


@app.get('/weather')
def getWeather():
    return {
        'chennai':"Current weather is cloudy",
        'hyderabad':"Current weather is Rainy",
        'delhi':"Current weather is Summer",
        'kashmir':"Current weather is Snowy"
    }


@weather_mcp.tool()
def get_weather_tool():
    return getWeather()



if __name__=="__main__":
    # Mount the FastMCP SSE Starlette app under /mcp so a single uvicorn
    # process serves both the FastAPI endpoints and the MCP SSE endpoints.
    app.mount("/mcp", weather_mcp.sse_app(mount_path="/mcp"))
    # Run a single uvicorn server (serves /weather and /mcp/*)
    uvicorn.run(app=app, host="0.0.0.0", port=9090)

