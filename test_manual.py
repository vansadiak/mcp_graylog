#!/usr/bin/env python3
"""
Manual MCP testing - shows the proper initialization sequence
"""

import json
import subprocess
import sys
import time

def send_mcp_requests():
    """Send proper MCP initialization and tool requests"""
    
    # MCP initialization sequence
    requests = [
        # 1. Initialize request
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "roots": {
                        "listChanged": True
                    },
                    "sampling": {}
                },
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        },
        # 2. Initialized notification
        {
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        },
        # 3. List tools
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        },
        # 4. Call a tool
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "search_logs",
                "arguments": {
                    "query": "*",
                    "limit": 5
                }
            }
        }
    ]
    
    # Start the server process
    process = subprocess.Popen(
        ["python3", "run_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    print("Sending MCP requests...")
    print("=" * 50)
    
    # Send each request
    for i, request in enumerate(requests, 1):
        print(f"\n{i}. Sending: {request['method']}")
        print(f"   Request: {json.dumps(request, indent=2)}")
        
        # Send the request
        request_json = json.dumps(request) + "\n"
        process.stdin.write(request_json)
        process.stdin.flush()
        
        # Give the server a moment to respond
        time.sleep(0.5)
    
    # Close stdin to signal end of input
    process.stdin.close()
    
    # Read responses
    stdout, stderr = process.communicate(timeout=10)
    
    print(f"\nResponses:")
    print("=" * 50)
    print(stdout)
    
    if stderr:
        print(f"\nErrors:")
        print("=" * 50)
        print(stderr)
    
    return process.returncode

if __name__ == "__main__":
    # Set environment variables
    import os
    os.environ.setdefault("GRAYLOG_ENDPOINT", "http://localhost:9000")
    os.environ.setdefault("GRAYLOG_USERNAME", "admin")
    os.environ.setdefault("GRAYLOG_PASSWORD", "admin")
    
    exit_code = send_mcp_requests()
    sys.exit(exit_code)
