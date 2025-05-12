# OwlPay Harbor MCP Server

## Overview
The OwlPay Harbor MCP Server provides documentation search capabilities. This server enables large language models (LLMs) to directly retrieve documentation, accelerating system integration.

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

For quick installation, click the installation buttons below:

[![Install with UV in VS Code](https://img.shields.io/badge/VS_Code-UV-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sqlite&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22db_path%22%2C%22description%22%3A%22SQLite%20Database%20Path%22%2C%22default%22%3A%22%24%7BworkspaceFolder%7D%2Fdb.sqlite%22%7D%5D&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-server-sqlite%22%2C%22--db-path%22%2C%22%24%7Binput%3Adb_path%7D%22%5D%7D) [![Install with UV in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-UV-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sqlite&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22db_path%22%2C%22description%22%3A%22SQLite%20Database%20Path%22%2C%22default%22%3A%22%24%7BworkspaceFolder%7D%2Fdb.sqlite%22%7D%5D&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-server-sqlite%22%2C%22--db-path%22%2C%22%24%7Binput%3Adb_path%7D%22%5D%7D&quality=insiders)

[![Install with Docker in VS Code](https://img.shields.io/badge/VS_Code-Docker-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sqlite&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22db_path%22%2C%22description%22%3A%22SQLite%20Database%20Path%20(within%20container)%22%2C%22default%22%3A%22%2Fmcp%2Fdb.sqlite%22%7D%5D&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22-v%22%2C%22mcp-sqlite%3A%2Fmcp%22%2C%22mcp%2Fsqlite%22%2C%22--db-path%22%2C%22%24%7Binput%3Adb_path%7D%22%5D%7D) [![Install with Docker in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Docker-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sqlite&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22db_path%22%2C%22description%22%3A%22SQLite%20Database%20Path%20(within%20container)%22%2C%22default%22%3A%22%2Fmcp%2Fdb.sqlite%22%7D%5D&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22-v%22%2C%22mcp-sqlite%3A%2Fmcp%22%2C%22mcp%2Fsqlite%22%2C%22--db-path%22%2C%22%24%7Binput%3Adb_path%7D%22%5D%7D&quality=insiders)

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