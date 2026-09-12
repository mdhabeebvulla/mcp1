import os
import nest_asyncio
import threading
from mcp.server.mcpserver import MCPServer

# Apply nest_asyncio to allow running asyncio in existing event loops (e.g., Colab)
nest_asyncio.apply()

# Get port from environment variable (Render sets PORT)
port = int(os.environ.get("PORT", 10000))

# Create MCP server with HTTP configuration in constructor
mcp = MCPServer(
    "ReverseWordServer"
)


@mcp.tool(description="Reverse a single word. Example: 'user' -> 'resu'")
def reverse_word(word: str) -> str:
    """Reverse a single word."""
    return word[::-1]


def run_mcp_server_in_thread():
    """Function to run the MCP server, intended for a separate thread."""
    print("Attempting to start MCP server in a new thread...")
    try:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
    except Exception as e:
        print(f"Error running MCP server in thread: {e}")


if __name__ == "__main__":
    # Start the server in a daemon thread so it exits with the main program
    server_thread = threading.Thread(target=run_mcp_server_in_thread, daemon=True)
    server_thread.start()
    print(f"MCP Server thread started on http://0.0.0.0:{port}. It should be running in the background.")
    print("You can now continue interacting with other notebook cells.")
    import time
    time.sleep(1) # Give it a moment to start up and print any initial messages
