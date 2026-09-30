from mcp.server import FastMCP  
# high-level MCP server class: handles protocol handshake, tool registry, and transport wiring

mcp = FastMCP("math")  
# server instance name — this is how a connecting client identifies/discovers this server


# registers the function as an MCP tool, auto-building its JSON schema from the type hints
@mcp.tool()  
def add(a:int, b:int)-> int:
    "Add two numbers "  # docstring becomes the tool description sent to the LLM client, guiding when it picks this tool
    return a+b

@mcp.tool()  # each tool needs its own decorator call — one registration per function
def multiply(a:int, b:int)->int:
    "multiply two number"
    return a*b


# stdio: client launches this file as a subprocess and talks over stdin/stdout — use for local, single-machine tools (alternatives: "sse"/"streamable-http" for network-reachable servers)

if __name__ == "__main__":
    mcp.run(transport="stdio")  