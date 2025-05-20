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
            logger.info("Calling hello-world tool...")
            response = await client.call_tool(
                name="hello-world", 
                arguments={"name": "World"}
            )
            
            # Debug: Show raw response structure
            logger.info(f"Raw response type: {type(response)}")
            logger.info(f"Raw response contents: {response}")
            
            # Debug: Inspect first response item if list
            if isinstance(response, list) and len(response) > 0:
                first_item = response[0]
                logger.info(f"First item type: {type(first_item)}")
                logger.info(f"First item dir: {dir(first_item)}")
                if hasattr(first_item, 'model_dump'):
                    logger.info(f"First item dump: {first_item.model_dump()}")
            
            # Concatenate responses
            full_response = "".join(
                r.text for r in response 
                if hasattr(r, 'text')
            )
            
            if full_response:
                print("Server response:", full_response)
            else:
                logger.error("No valid responses received. Debug info:")
                logger.error(f"Response structure: {response}")
    except Exception as e:
        logger.error(f"Client error: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
