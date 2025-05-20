# FastMCP Hello World Example

## Requirements
- Python 3.10+
- fastmcp package

## Installation
```bash
pip install fastmcp
```

## Running the Application

Run just the client (it will automatically start the server):
```bash
python client_mcp.py
```

Expected output:
```
2025-05-16 15:00:00 - __main__ - INFO - Connecting to MCP server...
2025-05-16 15:00:00 - __main__ - INFO - Calling hello-world tool...
Server response: Hello, World! Welcome to FastMCP!
```

## Key Features Demonstrated
- MCP server with STDIO transport
- Tool definition with type hints and docstrings
- Async client communication
- Error handling and validation
- Logging for observability
- Response status checking
