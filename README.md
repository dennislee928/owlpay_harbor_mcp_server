# OwlPay Harbor MCP Server

## Overview
The OwlPay Harbor MCP Server provides documentation search capabilities. This server enables large language models (LLMs) to directly retrieve documentation, accelerating system integration.

<img src="./docs/Demo.gif" width="650">
<br><br>

## Components

### Tools

#### Query Tools
- `search_owlpay_harbor_documentation`
   - Search Owlpay Harbor documentation. 
   - Input:
     - `query` (string): Search keywords in English.
   - Returns: Query results as array of objects

## Building

Docker:

```bash
docker build -t mcp/owlpay_harbor . --no-cache
```

## Usage with Claude Desktop

### Docker

For manual installation, open `Settings` -> `Developer` -> `Edit Config`, and add the following JSON block to your `claude_desktop_config.json` in Claude Desktop.

```json
# Add the server to your claude_desktop_config.json
"mcpServers": {
  "owlpay_harbor": {
    "command": "docker",
    "args": [
      "run", 
      "-i", 
      "--rm", 
      "mcp/owlpay_harbor"
    ]
  }
}
```

## Usage with VS Code

For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code. You can do this by pressing `Ctrl + Shift + P` and typing `Preferences: Open Settings (JSON)`.

Optionally, you can add it to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others.

> Note that the `mcp` key is needed when using the `mcp.json` file.


### Docker

```json
{
  "mcp": {
    "servers": {
      "owlpay_harbor": {
        "command": "docker",
        "args": [
          "run", 
          "-i", 
          "--rm", 
          "mcp/owlpay_harbor"
        ]
      }
    }
  }
}
```

## Usage with Cursor
For manual installation, open `Cursor Settings` -> `Add new global MCP server`

```json
# Add the server to your setting.json
"mcpServers": {
  "owlpay_harbor": {
    "command": "docker",
    "args": [
      "run", 
      "-i", 
      "--rm", 
      "mcp/owlpay_harbor"
    ]
  }
}
```
