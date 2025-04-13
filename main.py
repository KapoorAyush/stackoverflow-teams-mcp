from contextlib import asynccontextmanager
import httpx
from mcp.server.fastmcp import FastMCP

from settings import Settings
from utils import make_so_request


@asynccontextmanager
async def lifespan(app: FastMCP):
    """Lifespan context manager for FastMCP."""
    yield
    await httpClient.aclose()


mcp = FastMCP(name="teamsoverflow", lifespan=lifespan)
httpClient = httpx.AsyncClient()


@mcp.tool()
async def search_stackoverflow(query: str) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{Settings.baseUrl}/search"
    data = await make_so_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    return "abc"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
