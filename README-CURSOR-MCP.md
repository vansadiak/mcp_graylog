# Cursor MCP Configuration for Graylog Server

This document provides sample configurations for running the MCP Graylog server with Cursor.

## Configuration Files

### 1. Full Configuration (`cursor-mcp-config.json`)

Use this configuration if you need OAuth2 cookie support:

```json
{
  "mcpServers": {
    "graylog": {
      "command": "/Users/vansadiak/Desktop/codebase/personal/mcp_graylog/myenv/bin/python",
      "args": ["run_server.py"],
      "cwd": "/Users/vansadiak/Desktop/codebase/personal/mcp_graylog",
      "env": {
        "GRAYLOG_ENDPOINT": "https://your-graylog-server:9000",
        "GRAYLOG_TOKEN": "your-api-token-here",
        "GRAYLOG_COOKIES": "key1=value1; key2=value2; key3=value3",
        "GRAYLOG_VERIFY_SSL": "true",
        "GRAYLOG_TIMEOUT": "60",
        "LOG_LEVEL": "INFO",
        "LOG_FORMAT": "json"
      }
    }
  }
}
```

### 2. Minimal Configuration (`cursor-mcp-config-minimal.json`)

Use this configuration for basic token-only authentication:

```json
{
  "mcpServers": {
    "graylog": {
      "command": "/Users/vansadiak/Desktop/codebase/personal/mcp_graylog/myenv/bin/python",
      "args": ["run_server.py"],
      "cwd": "/Users/vansadiak/Desktop/codebase/personal/mcp_graylog",
      "env": {
        "GRAYLOG_ENDPOINT": "https://your-graylog-server:9000",
        "GRAYLOG_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

## Setup Instructions

### 1. Update Configuration

1. Copy one of the configuration files to your Cursor MCP settings
2. Update the following values:
   - `GRAYLOG_ENDPOINT`: Your Graylog server URL
   - `GRAYLOG_TOKEN`: Your Graylog API token
   - `GRAYLOG_COOKIES`: (Optional) Cookie string for OAuth2 authentication

### 2. Cookie Format for OAuth2

If your Graylog is behind Google OAuth2, format cookies as:

```
key1=value1; key2=value2; key3=value3
```

Example:

```
GRAYLOG_COOKIES="sri-dial-tex=value1; en=value2; 1db8b6b9-b4c8-4161-bad2-7c5264eae4b9=value3; sri_dial_tex__mm_admin=value4"
```

### 3. Environment Variables

| Variable             | Required | Description                              |
| -------------------- | -------- | ---------------------------------------- |
| `GRAYLOG_ENDPOINT`   | Yes      | Graylog server URL                       |
| `GRAYLOG_TOKEN`      | Yes      | Graylog API token                        |
| `GRAYLOG_COOKIES`    | No       | Cookie string for OAuth2                 |
| `GRAYLOG_VERIFY_SSL` | No       | Verify SSL certificates (default: true)  |
| `GRAYLOG_TIMEOUT`    | No       | Request timeout in seconds (default: 60) |
| `LOG_LEVEL`          | No       | Logging level (default: INFO)            |
| `LOG_FORMAT`         | No       | Log format (default: json)               |

## Available MCP Tools

Once configured, you'll have access to these MCP tools:

- `search_logs` - Search logs using Elasticsearch query syntax
- `get_log_statistics` - Get log statistics and aggregations
- `list_streams` - List all available Graylog streams
- `get_stream_info` - Get detailed information about a specific stream
- `search_stream_logs` - Search logs within a specific stream
- `get_system_info` - Get Graylog system information
- `test_connection` - Test connection to Graylog server
- `get_error_logs` - Get error logs from the last specified time range
- `get_log_count_by_level` - Get log count aggregated by log level
- `search_streams_by_name` - Search for streams by name
- `get_last_event_from_stream` - Get the last event from a specific stream

## Testing the Configuration

1. Start Cursor with the MCP configuration
2. Open the MCP panel in Cursor
3. Verify the `graylog` server is connected
4. Test with a simple query like:
   ```json
   {
     "query": "*",
     "time_range": "1h",
     "limit": 10
   }
   ```

## Troubleshooting

### Common Issues

1. **Authentication failed (401)**

   - Verify your `GRAYLOG_TOKEN` is correct
   - Check if cookies are needed for OAuth2

2. **Connection failed**

   - Verify `GRAYLOG_ENDPOINT` is accessible
   - Check network connectivity

3. **Server not starting**
   - Ensure you're in the correct directory (`cwd`)
   - Verify Python dependencies are installed in the virtual environment
   - Check that the virtual environment path is correct: `/Users/vansadiak/Desktop/codebase/personal/mcp_graylog/myenv/bin/python`

### Debug Mode

To enable debug logging, add to your environment:

```json
"LOG_LEVEL": "DEBUG"
```

This will provide detailed request/response information for troubleshooting.
