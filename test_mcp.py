#!/usr/bin/env python3
"""
MCP client for testing the server via stdio with proper initialization
"""

import asyncio
import json
import subprocess
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    """Test the MCP server with proper initialization"""
    
    # Set up server parameters
    server_params = StdioServerParameters(
        command="/Users/vansadiak/Desktop/codebase/personal/mcp_graylog/myenv/bin/python",
        args=["run_server.py"],
        env={
            "GRAYLOG_ENDPOINT": "https://graylog.strawmine.com/",
            "GRAYLOG_TOKEN": "token",
        }
    )
    
    print("Testing MCP Graylog Server")
    print("=" * 40)
    
    try:
        async with stdio_client(server_params) as (reader, writer):
            async with ClientSession(reader, writer) as session:
                print("1. Initializing MCP session...")
                await session.initialize()
                print("✓ Initialization successful")
                
                print("\n2. Listing available tools...")
                tools = await session.list_tools()
                print(f"✓ Found {len(tools.tools)} tools:")
                for tool in tools.tools:
                    print(f"  - {tool.name}: {tool.description}")
                
                print("\n3. Testing search_logs tool...")
                result = await session.call_tool(
                    "search_logs", 
                    arguments={
                        "query": "*",
                        "limit": 5
                    }
                )
                print(f"✓ Search result: {result.content}")
                
                print("\n4. Testing list_streams tool...")
                streams = await session.call_tool("list_streams", arguments={})
                print(f"✓ Streams result: {streams.content}")
                
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    # Set environment variables for testing
    import os
    os.environ.setdefault("GRAYLOG_ENDPOINT", "http://localhost:9000")
    os.environ.setdefault("GRAYLOG_USERNAME", "admin")
    os.environ.setdefault("GRAYLOG_PASSWORD", "admin")
    
    success = asyncio.run(test_mcp_server())
    sys.exit(0 if success else 1)
