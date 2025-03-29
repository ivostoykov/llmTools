import requests
import os
from dotenv import load_dotenv

load_dotenv()

def web_search(data):
    query = data.get("query")
    if not query:
        raise ValueError("Missing 'query' parameter")

    base_url = os.getenv("WEB_SEARCH_URL", "http://localhost:7999/search?q={query}&format=json")
    url = base_url.replace("{query}", requests.utils.quote(query))

    res = requests.get(url, timeout=10)
    res.raise_for_status()

    results = res.json().get("results", [])

    limit = int(os.getenv("WEB_SEARCH_RESULTS", "5") or "5")
    return [
        {
            "title": r.get("title"),
            "url": r.get("url"),
            "snippet": r.get("content")
        }
        for r in results[:limit]
    ]
