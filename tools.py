import utils
from main import mcp, Settings, httpClient
from typing import Any


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
async def search_stackoverflow(query: str) -> utils.PaginatedSearchResults | str:
    """
    Search StackOverflow for a given query.
    :param query:
    :return: A list of search results, which can be questions, answers or articles.
    """
    url = f"{Settings.baseUrl}/search?q={query}&page=1&pageSize=15&sort=relevance"
    data = await make_so_request(url)

    if not data:
        return "Unable to fetch results or no results found."

    return utils.PaginatedSearchResults.model_validate(data)
