import traceback
import uvicorn
from fastapi import FastAPI, Request
from src.api_helper import *

app = FastAPI()


@app.get("/news")
def list_news(request: Request, q: str = None, limit: int = 10):
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
