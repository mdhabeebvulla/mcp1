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

# FastAPI app
app = FastAPI(title="Reverse MCP Server")

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Reverse MCP server running",
        "mcp_endpoint": "/mcp",
    }

@app.get("/health")
def health():
    return {"ok": True}

# 🚨 CRITICAL:
# Mount MCP FIRST and do NOT create /mcp routes yourself.
mcp_app = mcp.streamable_http_app()
app.mount("/", mcp_app)
