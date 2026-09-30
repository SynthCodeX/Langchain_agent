from mcp.server import FastMCP


mcp = FastMCP("weather")

@mcp.tool()
def weather(city :str)->str:

    "check weather of a city "
    return f"Weather is 25 degree celcius of city {city}"


if __name__ =="__main__":
    mcp.run(transport="streamable-http")