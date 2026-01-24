from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "ReverseWordServer",
    stateless_http=True,
)

@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    return word[::-1]


if __name__ == "__main__":
    mcp.run()
