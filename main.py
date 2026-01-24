from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

# Create MCP server (stateless is good for cloud)
mcp = FastMCP("ReverseWordServer", stateless_http=True)

@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    return word[::-1]

# FastAPI app for health/info
app = FastAPI(title="Reverse MCP Server")

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "Reverse MCP server is running.",
        "mcp_endpoint": "/mcp (JSON-RPC over HTTP POST)",
        "example": {"tool": "reverse_word", "input": "user", "output": "resu"},
        "note": "OpenAI must point server_url to https://<host>/mcp (no trailing slash)."
    }

@app.get("/health")
def health():
    return {"ok": True}

# IMPORTANT:
# FastMCP streamable HTTP app exposes MCP at /mcp by default.
# So mount it under "/" and DO NOT create your own FastAPI route at "/mcp".
app.mount("/", mcp.streamable_http_app())
