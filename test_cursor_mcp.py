#!/usr/bin/env python3
"""
Test script to verify MCP server works exactly as Cursor would call it.
"""

import subprocess
import json
import time
import sys

def test_mcp_server():
    """Test the MCP server by simulating Cursor's behavior."""
    
    # Environment variables
    env = {
        "GRAYLOG_ENDPOINT": "https://graylog.strawmine.com/",
        "GRAYLOG_TOKEN": "10sm46kti9civbep5gtpgd3mj74adlciaqpf1o3h2qc0dvjrr6ua",
        "GRAYLOG_COOKIES": "_oauth2_proxy=d6LfE9n5ayTXCW8ihos4-FnO0r200ki5LdpQSJpEwQdqosROYduf1VFHqAmYGrA9pPYly5EupFRN1Bz9cUkJStbVIzM4ESE4LfrMwSj2u6CzDbWFuSj4mgA9B4uwrFnEDQo110PbpC-CWmb-Vd40HhiZ_1N_4ItsHR33EoQzcSizruSZWEZsfoAGtAiDtsrFgLJOMT_qxM28O6Fdolw28_DYPXkmAT40h7dX9PmD_zfX68YVvqwEYOCP3qRBGENKPy2dEPGknyhgVz2jUXw8pMQ3u2afO_7mwiGQc3LzIdKX_3YxFuC4w6LX-bjFCVT6XQmzBVn7Ep0FlRZi4H78gvh-Nu8sJO6yXUGvPk8gy0LnHhGiGImo7DtAqRH099Do4PhFUcOKzYlS5F44ffVXWWVtXA5q0DVP476YLLIp-gMe3udSVK2p-c5Vbr3SKT0CQBf12aHW0hXZpKLNMVa3g08QXfbS-TYT8X7Hz3skEapG6wTcIrWtf6v7rmTx1CVooH7DCMnwKEhirdw-h5xsR6rrRZzYwVC5vH0sbQ2ngk0TpgAr2kbZvYogktAIZjTpjVQxei8KilffLxcIdjXSiIUnhcoG18-MbNPRt3E9pF8AZTf40MMZKNWUSz_ejnfj3XQvef_8URWsuRFb51uNmF5zrJOJr__hWqcAFzeGYVK4Ebe_5VlYPwzaxIvZNprrBGYk-QK7vVIv-xAs_VV_mET5MX-EGo_7mtraBd_hmZFI4DcmFw4D02GQqyTY-VKero5rGxVWK2uI3pHBpWx2TuFFVk41P1j93et6k2Mfsn4Z-1ZPDUh2tJ51JD1iuGYTbbqdSI_OTtUBdnYgf-0EPG7QBudGvlRBqVCdok4jQIG9dQ95E9cmgN2o5GN4AmCTdKbUMAwaC0O-zEdTDKBzc06YhNkr62EcaW29_HyPDQ6livuJ0ZFrfxThiwRpPGuSOZk4l8OS_JLnNZ-H1ZZanxLS4PeThpgo_BN3ayC9kYCQyEbgT5FwRwzGdpehUkwtG3zhYLs_1Mtsh2W9GdLnWCUKUEtZveGIFsOtpUDjkYAJ8sVPnr56iN7Bg11qE7b_zJnCviI0LtqTSBtFqcJUCxoAOh0KzpclUnDdzPyWgxsf-Go3ttehK7yY7xN4kk7UjXikoodJx2nMsNr9hu1CZefOgKtGuDICmfzhvl7TjOH6b2vkDXYGUWqNJfOwYKhUWRPuF-Kylf_HX6m85MVkSKBv4WaM69mOQ2sKCfj2dY87WAzVNrKHRJFim1YCPdyufnJtXlC-_jwlK-csSH67gTNRVOQffgaDWyeQJuL9rOQT25IieD274IOQrnxAEWnG3_wUTSGJuZYmfuAWOIhAUtTIQMneXpXvL6qYSy93Hvl37xlP4CiV-YJpxVfBHNqIxAe3_783q7xZeV13AXJh1q61vXgOqzIDVrRpQ53SWD2YzuTvPUWwoxsUGUbyO-5nTDv7YiwBP8MeZoPvlaqG5U5b0UAa9_gGjkO2WozadHkW4ZnbYPe-punvw2R6HQPjcB6DAx3oevlHtuU72JtubpGjbtifSz_ci_-CXveKv4KoLupt1es84rOon-lbYDWF2gAFeG4LuYJJE_w0BTgLTgAK-aDDEdpnfEl9KpbKPrNIS8D5WNmvLU1inlYCksAALv10haoBXLilb4OKDU5tk7CthiA7CBL6FkVO2ek6BKIsKSauMLVmFHKU|1760853323|mzwh5xUsBvDTju6a67RvCuzOs-Jsd8qZAd7DiSJmxfY=; _oauth2_proxy_csrf=3ddb669846bceea29a3762884b1cfd7f;",
        "PATH": "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }
    
    # Command to run
    cmd = [
        "/Users/vansadiak/Desktop/codebase/personal/mcp_graylog/myenv/bin/python",
        "run_server.py"
    ]
    
    cwd = "/Users/vansadiak/Desktop/codebase/personal/mcp_graylog"
    
    print("Starting MCP server process...")
    print(f"Command: {' '.join(cmd)}")
    print(f"Working directory: {cwd}")
    print(f"Environment: GRAYLOG_ENDPOINT={env['GRAYLOG_ENDPOINT']}")
    print()
    
    # Start the server process
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        env=env,
        text=True,
        bufsize=1
    )
    
    # Wait a moment for server to start
    time.sleep(2)
    
    # Send initialize request
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    print("Sending initialize request...")
    proc.stdin.write(json.dumps(init_request) + "\n")
    proc.stdin.flush()
    
    # Read response
    response_line = proc.stdout.readline()
    print(f"Initialize response: {response_line}")
    
    # Send tools/list request
    tools_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }
    
    print("\nSending tools/list request...")
    proc.stdin.write(json.dumps(tools_request) + "\n")
    proc.stdin.flush()
    
    # Read response
    response_line = proc.stdout.readline()
    print(f"Tools list response: {response_line}")
    
    if response_line:
        try:
            response = json.loads(response_line)
            if "result" in response and "tools" in response["result"]:
                tools = response["result"]["tools"]
                print(f"\n✓ Found {len(tools)} tools:")
                for tool in tools:
                    print(f"  - {tool.get('name', 'unknown')}")
            else:
                print("\n✗ No tools found in response")
                print(f"Response: {json.dumps(response, indent=2)}")
        except json.JSONDecodeError as e:
            print(f"\n✗ Failed to parse response: {e}")
    
    # Check stderr for any errors
    print("\n--- Server stderr output ---")
    # Non-blocking read of stderr
    import select
    if select.select([proc.stderr], [], [], 0.1)[0]:
        stderr_output = proc.stderr.read()
        print(stderr_output)
    
    # Cleanup
    proc.terminate()
    proc.wait(timeout=5)
    print("\nServer process terminated")

if __name__ == "__main__":
    test_mcp_server()

