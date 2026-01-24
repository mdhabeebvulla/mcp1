import os
from mcp.server.fastmcp import FastMCP

# Create MCP server with stateless HTTP mode for cloud deployment
mcp = FastMCP(
    "ReverseWordServer",
    stateless_http=True,  # Required for cloud deployments
    json_response=True,   # Recommended for optimal scalability
)


@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    """Reverse a single word."""
    return word[::-1]


if __name__ == "__main__":
    # Get port from environment variable (Render sets PORT)
    port = int(os.environ.get("PORT", 10000))
    
    # Run with streamable-http transport for remote access
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",  # Bind to all interfaces
        port=port,
    )
