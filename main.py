from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
#hi
# Create an MCP server (stateless is perfect for simple tools)
mcp = FastMCP("ReverseWordServer", stateless_http=True)

@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    return word[::-1]

# FastAPI wrapper (optional but useful for health checks / homepage)
app = FastAPI(title="Reverse MCP Server")

@app.get("/mcp")
def home():
    return {
        "status": "ok",
        "message": "Reverse MCP server is running. MCP endpoint is at /mcp",
        "example": {"tool": "reverse_word", "input": "user", "output": "resu"},
    }

@app.get("/health")
def health():
    return {"ok": True}

# IMPORTANT: mount at "/" so the MCP app keeps its default mount path "/mcp"
# => your MCP endpoint becomes: https://<service>.onrender.com/mcp
app.mount("/", mcp.streamable_http_app())
