# FastMCP LED Control Server

## Requirements
- Python 3.10+
- Arduino Uno with LED connected to `LED_BUILTIN`
- Serial port access to Arduino device

## Installation (uv recommended)
```bash
# Create and activate virtual environment
uv venv .venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# System setup (one-time)
sudo usermod -a -G dialout $USER  # Serial port access
sudo reboot  # Apply group changes
```

## Configuration
Create `cline_mcp_settings.json`:
```json
{
  "mcpServers": {
    "blink-led-server": {
      "disabled": false,
      "timeout": 60,
      "command": "python",
      "args": [
        "/path/to/server_mcp.py"
      ],
      "env": {},
      "transportType": "stdio"
    }
  }
}
```

## Running the Application
1. Upload Arduino sketch first
2. Start client (auto-starts server):
```bash
python client_mcp.py
```

## Expected Output
```
2025-05-16 15:00:00 - __main__ - INFO - Connecting to MCP server...
2025-05-16 15:00:00 - __main__ - INFO - Sending LED state: on
Server response: LED is on
2025-05-16 15:00:01 - __main__ - INFO - Sending LED state: off
Server response: LED is off
```

## Troubleshooting
- Ensure Arduino is connected to `/dev/ttyACM1`
- Verify serial port permissions with `ls -l /dev/ttyACM1`
- Check Arduino IDE → Tools → Port matches configured port

## Key Features
- MCP server with serial hardware control
- Async client with status feedback
- Type-safe LED state validation
- Automatic server lifecycle management
- Cross-platform serial communication
