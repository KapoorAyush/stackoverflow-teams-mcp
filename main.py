from contextlib import asynccontextmanager
import httpx
from mcp.server.fastmcp import FastMCP
from pydantic_settings import BaseSettings


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

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
