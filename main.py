import os
from mcp.server.fastmcp import FastMCP

# Get port from environment variable (Render sets PORT)
port = int(os.environ.get("PORT", 10000))

# Create MCP server with HTTP configuration in constructor
mcp = FastMCP(
    "ReverseWordServer",
    host="0.0.0.0",        # Bind to all interfaces
    port=port,             # Port from environment
    stateless_http=True,   # Required for cloud deployments
    json_response=True,    # Recommended for scalability
)


@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    """Reverse a single word."""
    return word[::-1]


if __name__ == "__main__":
    # Run with streamable-http transport for remote access
    mcp.run(transport="streamable-http")
