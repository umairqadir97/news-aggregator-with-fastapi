from src.config import *


def sample_response_parser(results):
    """
    :param results: JSON Object
    :return: List of dictionaries
            [
                {
                    "title": "title of the news",
                    "link": "original link of the news source",
                    "source":"your-api-name"
                },
            ...
            ]
    """
    # Change the Body accordingly...
    response = []
    for child in results["data"]["children"]:
        response.append({
            "title": child["data"]["title"],
            "link": child["data"]["url"],
            "source": "your-api-name"
        })
    return response


YOUR_API_MAPPING = {
    "api_name": "your-api-name",
    "parser": sample_response_parser,
    "listing_url": "link-to-your-api-listing?limit={limit}",
    "search_url": "link-to-your-api-search-endpoint?q={query}&limit={limit}"
}
