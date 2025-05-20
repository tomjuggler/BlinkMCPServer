import logging
from fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

mcp = FastMCP("HelloWorldServer")

@mcp.tool(name="hello-world")
def hello_world(name: str) -> str:
    """Greet a user by name.
    
    Args:
        name: The name to greet
        
    Returns:
        A personalized greeting message
    """
    logger.info(f"Received hello request for name: {name}")
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}! Welcome to FastMCP!"

if __name__ == "__main__":
    try:
        logger.info("Starting MCP server...")
        mcp.run()
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise
