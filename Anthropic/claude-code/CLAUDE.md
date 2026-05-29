# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Create and activate virtual environment
uv venv && source .venv/bin/activate

# Install in development mode
uv pip install -e .

# Start the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

This is a Python MCP (Model Context Protocol) server that exposes document-processing tools to AI assistants.

**Entry point**: `main.py` creates a `FastMCP` server instance and registers tools via `mcp.tool()`. The server communicates over stdio by default.

**Tools** live in `tools/`. Each tool is a plain Python function registered with the server in `main.py`:
```python
mcp.tool()(my_function)
```

**Current tools**:
- `tools/math.py` — `add(a, b)`: registered in main.py
- `tools/document.py` — `binary_document_to_markdown(binary_data, file_type)`: implemented but not yet registered; converts raw bytes (DOCX, PDF, etc.) to markdown using the MarkItDown library

**Tests** are in `tests/` using pytest. Fixtures (`.docx`, `.pdf`) live in `tests/fixtures/`.

## Tool Definition Conventions

Use `pydantic.Field` for parameter descriptions. Docstrings should include a one-line summary, detailed explanation, when to use/avoid, and a usage example. See existing tools for the pattern.
