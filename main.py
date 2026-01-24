from mcp.server.fastmcp import FastMCP
import os
import time

mcp = FastMCP(
    "ReverseWordServer",
    stateless_http=True,
)

@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    return word[::-1]


if __name__ == "__main__":
    # Some MCP builds spawn the server in a background task.
    # Keep process alive so Render doesn't kill the container.
    mcp.run()

    while True:
        time.sleep(3600)
