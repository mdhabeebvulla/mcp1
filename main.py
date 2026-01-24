from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP(
    "ReverseWordServer",
    stateless_http=True,
)

@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    return word[::-1]


# IMPORTANT:
# Use MCP's run() compatible ASGI app (with lifespan)
app = mcp.streamable_http_app(lifespan=True)
