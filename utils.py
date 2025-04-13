from typing import Any
from main import httpClient
from settings import Settings


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
