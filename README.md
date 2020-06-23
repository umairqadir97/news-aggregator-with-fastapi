## General Technique to aggregate

1. get list of registered APIs
2. Loop over APIs
3. Make JSON pbject of configurations for each API
4. Write JSON parsers for each API
5. Combine result in uniform format to display
6. return results

---

## Detailed Approach

Every Request to API should be async; put the request in job tracker, get results and push back responses

#### News Listing Endpoint
api.route('/news')
def function():
       1. Get all available APIs
       2. Call each API for getting top 10 news in JSON; Listing Function for Each API
       3. Aggregate news from all APIs, discard empty responses
       

#### News Search Endpoint
api.route('/news?query=bitcoin')
def function():
       1. Get all available APIs
       2. Call each API with searach query to get top 10 resultsin JSON; Searching Function for Each API
       3. Aggregate results from all APIs, discard empty responses


#### Other Helper Functions
       1. News_API json parser for listing responses; should return only required fields; ["title",  "link", "source"]
       2. Reddit_API json parser for listing results


#### Adding New API
       1. Make a new file for new API in ```src/external_api/```
       2. Take ```src/external_api/sample_api.py``` as reference
       3. Prepare API Mapping object
       4. Write JSON parser for that API
       5. Register your API in API_COLLECTION in ```src/api_helper.py```


