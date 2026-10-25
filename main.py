import os
from mcp.server.fastmcp import FastMCP
from datetime import datetime
port = int(os.environ.get("PORT", 10000))

mcp = FastMCP(
    "ReverseWordServer",
    host="0.0.0.0",
    port=port,
    stateless_http=True,
    json_response=True,
)

@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    """Reverse a single word."""
    return word[::-1]
@mcp.tool(description="Return the current local date and time as a string.")
def current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
