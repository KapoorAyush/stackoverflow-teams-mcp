# TeamsOverflow MCP

A Model Context Protocol (MCP) server that provides access to the Stack Exchange API for Teams, allowing AI assistants to search and retrieve information from Stack Overflow.

## Project Overview

This project exposes two main MCP tools:

1. `stackoverflow_questions` - Search Stack Overflow for questions and answers matching a query
2. `stackoverflow_excerpts` - Search Stack Overflow for excerpts matching a query

The server uses the Stack Exchange API to fetch data and formats the results in a structured way.

## Project Structure

```
teamsoverflow-mcp/
├── .vscode/mcp.json # Dogfooding - Using this server with VSCode Copilot in this project
├── main.py          # MCP server logic
└── utils.py         # data models
```

## Setup Instructions

This project uses `uv` for Python package management. Follow these steps to set up the project:

### Prerequisites

- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd teamsoverflow-mcp
   ```

2. Create a virtual environment and install dependencies using uv:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

## Running the Server

### For Development

Use `fastmcp dev` for local development.

It runs the [inspector tool](https://github.com/modelcontextprotocol/inspector) written by Anthropic.

```bash
fastmcp dev main.py
```

Supply these 2 env variables before starting the MCP server.

- BASE_URL (base url for the api)
- API_KEY (api key)

### For using with VSCode Copilot

Check out `.vscode/mcp.json`