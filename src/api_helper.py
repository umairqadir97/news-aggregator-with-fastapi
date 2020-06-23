from src.config import *
from src.external_api.reddit_api import *
from src.external_api.news_api import *

#
# Register your API in this API-COLLECTION
API_COLLECTION = [
    REDDIT_API_MAPPING,
    NEWS_API_MAPPING
]


#
# Verify required Fields in API Parser's response
def verify_attribute(response):
    required_fields = ["title", "link", "source"]
    return None


#
# Call 'Search' endpoint of all registered APIs
def get_news(limit):
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
    response = []
    for api in API_COLLECTION:
        result = requests.get(api["search_url"].format(query=query, limit=limit),
                              headers={'User-agent': 'your bot 0.1'}).json()
        if result:
            response += api["parser"](result)
    return response
