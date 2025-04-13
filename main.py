from contextlib import asynccontextmanager
import httpx
from typing import Any
from fastmcp import FastMCP, Context
from pydantic_settings import BaseSettings

import utils


class Settings(BaseSettings):
    baseUrl: str
    apiKey: str


@asynccontextmanager
async def lifespan(app: FastMCP):
    """Lifespan context manager for FastMCP."""
    yield
    await httpClient.aclose()


mcp = FastMCP(name="teamsoverflow", lifespan=lifespan)
httpClient = httpx.AsyncClient()


async def make_so_request(url: str) -> dict[str, Any] | None:
    """Make a request to the StackOverflow API with proper error handling."""
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {Settings.apiKey}",
    }
    try:
        response = await httpClient.get(url, headers=headers, timeout=10.0)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


@mcp.tool()
async def search_stackoverflow(
    query: str, ctx: Context
) -> utils.PaginatedSearchResults | str:
    """
    Search StackOverflow for a given query.
    :param query:
    :return: A list of search results if successful, otherwise an error message.
    """
    url = f"{Settings.baseUrl}/search?q={query}&page=1&pageSize=15&sort=relevance"
    await ctx.info(f"Making request to {url}")
    data = await make_so_request(url)

    if not data:
        return "Unable to fetch results or no results found."

    return utils.PaginatedSearchResults.model_validate(data)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
