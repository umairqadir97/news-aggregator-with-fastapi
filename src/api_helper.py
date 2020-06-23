from src.config import *
from src.external_api.reddit_api import *
from src.external_api.news_api import *

#
# Register your API in this API-COLLECTION
API_COLLECTION = [
    REDDIT_API_MAPPING,
    NEWS_API_MAPPING
]

# === Listing Endpoint ===
# Verify required Fields in API Parser's response
def verify_attribute(response):
    """
    This function is intended to make sure we are receiving right fields from
    dependent APIs.

    :param response: Response object received from sub APIs.
    :return: Return response object if valid, otherwise raise exception.
    """
    required_fields = ["title", "link", "source"]
    return None


# === Search Endpoint ===
# Call 'Search' endpoint of all registered APIs
def get_news(limit):
    """
    This function will get top news from all registered APIs (in API_COLLECTION).
    :param limit: Integer number to limit number of responses from each API.
    :return: Return aggregated news results.
    """
    response = []
    for api in API_COLLECTION:
        result = requests.get(api["listing_url"].format(limit=limit),
                              headers={'User-agent': 'your bot 0.1'}).json()
        if result:
            response += api["parser"](result)
    return response


#
# Call 'Search' endpoint of all registered APIs
def search_news(query, limit):
    """
     This function will get search results for given QUERY from all registered APIs (in API_COLLECTION).

    :param query: Search Query.
    :param limit: Integer number to limit number of responses from each API.
    :return: Return aggregated news results.
    """
    response = []
    for api in API_COLLECTION:
        result = requests.get(api["search_url"].format(query=query, limit=limit),
                              headers={'User-agent': 'your bot 0.1'}).json()
        if result:
            response += api["parser"](result)
    return response
