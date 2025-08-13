# Sci-Hub MCP Server

[![smithery badge](https://smithery.ai/badge/@JackKuo666/sci-hub-mcp-server)](https://smithery.ai/server/@JackKuo666/sci-hub-mcp-server)

🔍 Enable AI assistants to search, access, and analyze academic papers through Sci-Hub using a simple MCP interface.

The Sci-Hub MCP Server provides a bridge between AI assistants and Sci-Hub's repository of academic literature through the Model Context Protocol (MCP). It allows AI models to search for scientific articles by DOI, title, or keywords, access their metadata, and download PDFs in a programmatic way.

## ✨ Core Features

- 🔎 Paper Search by DOI: Find papers using their Digital Object Identifier ✅
- 🔍 Paper Search by Title: Locate papers using their full or partial title ✅
- 🔑 Paper Search by Keyword: Discover papers related to specific research areas ✅
- 📊 Metadata Access: Retrieve detailed metadata for specific papers ✅
- 📄 PDF Download: Download full-text PDF content when available ✅

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- uv (Python package manager) - [Install UV](https://github.com/astral-sh/uv)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gyasis/Sci-Hub-MCP-Server.git
   cd Sci-Hub-MCP-Server
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. (Optional) Install development dependencies:
   ```bash
   uv sync --extra dev
   ```

## 📊 Usage

### Development Mode (Testing with MCP Inspector)

Start the MCP server with the MCP Inspector for interactive testing:

```bash
# Using uv directly
uv run fastmcp dev sci_hub_server.py

# Or using the convenience script
./run_dev.sh
```

The MCP Inspector will be available at: http://127.0.0.1:6274

### Production Mode (For MCP Clients)

Start the MCP server for production use with MCP clients:

```bash
uv run python sci_hub_server.py
```

## 🔧 MCP Client Configuration

### For Cursor IDE

Add this configuration to your `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "scihub": {
      "command": "/home/gyasis/.local/bin/uv",
      "args": ["run", "--directory", "/home/gyasis/Documents/code/Sci-Hub-MCP-Server", "python", "sci_hub_server.py"],
      "cwd": "/home/gyasis/Documents/code/Sci-Hub-MCP-Server",
      "env": {},
      "enabled": true
    }
  }
}
```

**Note:** Replace the paths with your actual project location.

### For Claude Desktop

Add this configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "scihub": {
      "command": "/path/to/your/project/.venv/bin/python",
      "args": ["/path/to/your/project/sci_hub_server.py"],
      "cwd": "/path/to/your/project",
      "env": {},
      "enabled": true
    }
  }
}
```

**Note:** Replace `/path/to/your/project` with your actual project path.

## 🛠 MCP Tools

The Sci-Hub MCP Server provides the following tools:

1. `search_scihub_by_doi`: Search for a paper on Sci-Hub using its DOI (Digital Object Identifier).
2. `search_scihub_by_title`: Search for a paper on Sci-Hub using its title.
3. `search_scihub_by_keyword`: Search for papers on Sci-Hub using a keyword.
4. `download_scihub_pdf`: Download a paper PDF from Sci-Hub.
5. `get_paper_metadata`: Get metadata information for a paper using its DOI.

### Searching Papers by DOI

You can ask the AI assistant to search for papers using DOI:
```
Can you search Sci-Hub for the paper with DOI 10.1038/nature09492?
```

### Searching Papers by Title

You can search for papers using their title:
```
Can you find the paper titled "Choosing Assessment Instruments for Posttraumatic Stress Disorder Screening and Outcome Research" on Sci-Hub?
```

### Searching Papers by Keyword

You can search for papers related to specific keywords:
```
Can you search Sci-Hub for recent papers about artificial intelligence in medicine?
```

### Downloading Papers

Once you have found a paper, you can download it:
```
Can you download the PDF for this paper to my_paper.pdf?
```

### Getting Paper Metadata

You can request metadata for a paper using its DOI:
```
Can you show me the metadata for the paper with DOI 10.1038/nature09492?
```

## 📁 Project Structure

- `sci_hub_server.py`: The main MCP server implementation using FastMCP
- `sci_hub_search.py`: Contains the logic for searching Sci-Hub and retrieving paper information
- `pyproject.toml`: Project configuration and dependencies (uv-based)
- `run_dev.sh`: Convenience script for starting development mode
- `.venv/`: Virtual environment created by uv (auto-generated)

## 🔧 Dependencies

- Python 3.10+
- uv (Python package manager)
- fastmcp>=2.0.0
- requests>=2.31.0
- beautifulsoup4>=4.12.0
- mcp>=0.1.0
- scihub

All dependencies are managed through `pyproject.toml` and can be installed with `uv sync`.

## 🔍 Troubleshooting

### Common Issues

**1. "No module named 'fastmcp'" error**
- Make sure you've run `uv sync` to install dependencies
- Ensure you're using the virtual environment: `uv run python sci_hub_server.py`

**2. MCP client connection fails**
- Verify your MCP client configuration paths are correct
- Check that the server starts without errors: `uv run python sci_hub_server.py`
- Ensure the `cwd` (current working directory) is set correctly

**3. "TypeError: unexpected keyword argument 'timeout'"**
- This has been fixed in the current version
- The server now uses `mcp.run(transport='stdio')` without timeout parameter

**4. Development vs Production confusion**
- **Development**: Use `uv run fastmcp dev sci_hub_server.py` for testing with MCP Inspector
- **Production**: Use `uv run python sci_hub_server.py` for MCP client integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This tool is for research purposes only. Please respect copyright laws and use this tool responsibly. The authors do not endorse or encourage any copyright infringement.
