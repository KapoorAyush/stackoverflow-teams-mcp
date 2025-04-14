import os
from contextlib import asynccontextmanager
import httpx
from typing import Any
from fastmcp import FastMCP, Context
from urllib.parse import quote

import utils

BASE_URL = os.environ.get("BASE_URL", "https://api.stackexchange.com/2.3")
API_KEY = os.environ.get("API_KEY")


@asynccontextmanager
async def lifespan(app: FastMCP):
    """Lifespan context manager for FastMCP."""
    yield
    await httpClient.aclose()


mcp = FastMCP(name="teamsoverflow", lifespan=lifespan)
httpClient = httpx.AsyncClient()


async def make_so_request(url: str) -> dict[str, Any] | None:
    """Make a request to the StackOverflow API with proper error handling."""
    try:
        response = await httpClient.get(url, timeout=10.0)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error making request: {e}")
        return None

@mcp.tool()
async def stackoverflow_questions(query: str, ctx: Context) -> str:
    """
    search stackoverflow for questions and answers matching the query
    :param query: the search query
    :return: A list of search results if successful, otherwise an error message.
    """
    # URL encode the query for safety
    encoded_query = quote(query)
    url = f"{BASE_URL}/search/advanced?key={API_KEY}&q={encoded_query}&order=desc&page=1&pagesize=3&sort=relevance&answers=1&filter=withbody"

    await ctx.info(f"Searching StackOverflow for: {query}")
    await ctx.info(f"Making request to {url}")

    data = await make_so_request(url)

    if not data:
        return "Unable to fetch results or no results found."

    try:
        results = utils.SearchQnA.model_validate(data)
        formatted = [ f"Title: {i.title}\n Body: {i.body} \n Link: {i.link}" for i in results.items]
        return "\n\n".join(formatted)
    except Exception as e:
        await ctx.warning(f"Error parsing response: {e}")
        return f"Error parsing search results: {e}"

@mcp.tool()
async def stackoverflow_excerpts(query: str, ctx: Context) -> str:
    """
    search stackoverflow for excerpts matching the query
    :param query: the search query
    :return: A list of search results if successful, otherwise an error message.
    """
    # URL encode the query for safety
    encoded_query = quote(query)
    url = f"{BASE_URL}/search/excerpts?key={API_KEY}&q={encoded_query}&order=desc&page=1&pagesize=10&sort=relevance&answers=1&filter=withbody"

    await ctx.info(f"Searching StackOverflow for: {query}")
    await ctx.info(f"Making request to {url}")

    data = await make_so_request(url)

    if not data:
        return "Unable to fetch results or no results found."

    def get_link(item: utils.SearchExcerpt) -> str:
        if item.item_type == "question":
            return f"https://stackoverflow.com/questions/{item.question_id}"
        else:
            return f"https://stackoverflow.com/a/{item.answer_id}"

    try:
        results = utils.SearchExcerpts.model_validate(data)
        formatted = [ f"Title: {i.title}\n Body: {i.body}\n Type: {i.item_type}\n Link: {get_link(i)}" 
                     for i in results.items]
        return "\n\n".join(formatted)
    except Exception as e:
        await ctx.warning(f"Error parsing response: {e}")
        return f"Error parsing search results: {e}"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
