import os
from mcp.server.fastmcp import FastMCP

PORT = int(os.environ.get("PORT", "10000"))

mcp = FastMCP("ReverseWordServer", stateless_http=True)

@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    return word[::-1]

if __name__ == "__main__":
    mcp.run(host="0.0.0.0", port=PORT)
