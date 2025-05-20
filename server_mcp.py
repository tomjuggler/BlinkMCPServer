import logging
from fastmcp import FastMCP
import serial
from typing import Literal

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

mcp = FastMCP("BlinkLEDServer")
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

@mcp.tool(name="blink-led")
def control_led(led_state: Literal["on", "off"]) -> str:
    """Control the LED state.
     
    Args:
        led_state: Desired LED state (on/off)
        
    Returns:
        Current LED status confirmation
    """
    logger.info(f"Setting LED to {led_state}")
    ser.write(b'1' if led_state == "on" else b'0')
    response = ser.readline().decode().strip()
    return f"LED is {response}"

if __name__ == "__main__":
    try:
        logger.info("Starting MCP server...")
        mcp.run()
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise
