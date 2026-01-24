from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP(
    "ReverseWordServer",
    stateless_http=True,
)

# Tool definition
@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    return word[::-1]

# Create FastAPI app ONLY to host MCP
app = FastAPI()

# 🚨 DO NOT define /mcp routes yourself.
# Mount MCP root so its default /mcp endpoint works.
app.mount("/", mcp.streamable_http_app())
