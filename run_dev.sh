#!/bin/bash
# Sci-Hub MCP Server Development Script

echo "🚀 Starting Sci-Hub MCP Server in development mode..."
echo "📖 MCP Inspector will be available at: http://127.0.0.1:6274"
echo ""

uv run fastmcp dev sci_hub_server.py 