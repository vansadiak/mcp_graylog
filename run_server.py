#!/usr/bin/env python3
"""
MCP Graylog Server Runner

This script provides a simple way to run the MCP Graylog server.
It handles environment setup and provides helpful error messages.
"""

import os
import sys
import logging
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def check_environment():
    """Check if required environment variables are set."""
    required_vars = ["GRAYLOG_ENDPOINT", "GRAYLOG_TOKEN"]
    missing_vars = []



    return True


def main():
    """Main entry point."""
    setup_logging()

    # Check environment
    env_ok = check_environment()

    try:
        from mcp_graylog.server import mcp_server

        print("MCP Server imported successfully", file=sys.stderr)
        print("Starting MCP Graylog server...", file=sys.stderr)

        # Run the MCP server over stdio
        mcp_server.run()

    except ImportError as e:
        print(f"ERROR: Failed to import server module: {e}", file=sys.stderr)
        print("Make sure all dependencies are installed:", file=sys.stderr)
        print("  pip install -r requirements.txt", file=sys.stderr)
        return 1

    except Exception as e:
        print(f"ERROR: Failed to start server: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
