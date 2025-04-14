import requests
import os
from dotenv import load_dotenv

load_dotenv()

def web_search(data):
    query = data.get("query")
    if not query:
        raise ValueError("Missing 'query' parameter")

    params = { "q": query, "format": "json" }

    if "categories" in data:
        params["categories"] = data["categories"]
    if "language" in data:
        params["language"] = data["language"]
    if "time_range" in data:
        params["time_range"] = data["time_range"]

    base_url = os.getenv("WEB_SEARCH_URL", "http://localhost:7999/search")
    url = base_url.split('?')[0]

    res = requests.get(url, params=params, timeout=10)
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
