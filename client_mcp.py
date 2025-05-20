import logging
import asyncio
from fastmcp import Client

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def main():
    try:
        logger.info("Connecting to MCP server...")
        async with Client("server_mcp.py") as client:
            # Test sequence: on -> off -> off with delays
            for state in ["on", "off", "off"]:
                logger.info(f"Sending LED state: {state}")
                response = await client.call_tool(
                    name="blink-led", 
                    arguments={"led_state": state}
                )
                print(f"Server response: {response}")
                if state != "off":  # No delay after last command
                    await asyncio.sleep(1)
                    
    except Exception as e:
        logger.error(f"Client error: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
