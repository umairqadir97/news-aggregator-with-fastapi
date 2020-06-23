import traceback
import uvicorn
from fastapi import FastAPI
from src.api_helper import *

app = FastAPI()

# === Application Main Endpoint
@app.get("/news")
def list_news(q: str = None, limit: int = 10):
    """
    This single endpoint will server getting Top-Listings and Search functionality
    for news aggregation APIs.

    :param q: Search query in request url.
    :param limit: Integer number to limit number of results to fetch from each dependent API.
    :return: JSON response of aggregated results.
    """
    try:
        if q:
            # call search endpoint
            result = search_news(q, limit)
        else:
            # call news listing endpoint
            result = get_news(limit)
        return result
    except:
        return traceback.print_exc()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
