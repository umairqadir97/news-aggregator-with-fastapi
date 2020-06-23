[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="reports/new-aggregation.jpg" alt="Logo" width="500" height="250">
  </a>

  <h3 align="center">News Aggregator with FastAPI</h3>

  <p align="center">
    Boilerplate news aggregation application build for Reddit and NewsAPI. Main idea is to use lightweight development frameworks like FastAPI rather than heavy weight lifting with Django/ Flask. Further information can be found in <a hred="https://github.com/umairqadir97/news-aggregator-with-fastapi/blob/master/reports/Problem-Statement.md">Problem Statement</a> document.
    <br />
    <br />
    <br />
    <a href="mailto:umairqadir97@gmail.com">Request Demo</a>
    ·
    <a href="https://github.com/umairqadir97/learning-management-system/issues">Report Bug</a>
    ·
    <a href="https://github.com/umairqadir97/learning-management-system/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](#about-the-project)


The application is built in accordance with <a hred="https://github.com/umairqadir97/news-aggregator-with-fastapi/blob/master/reports/Problem-Statement.md">Problem Statement</a> document. All of the features are implemented. All the contraints are implemented, along with project documentation and unit-tests.

<br>


#### What's Not Implemented
Current version of this project does not implement cache server or job queue to minimize performance dependence on external APIs.


<br>

### Built With

* [Python](http://python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)



<!-- GETTING STARTED -->
## Getting Started

#### General Technique to Aggregate

1. Get list of registered APIs
2. Loop over APIs
3. Make JSON object of configurations for each API
4. Write JSON parsers for each API
5. Combine result in uniform format to display
6. Return results



#### Detailed Approach

Every Request to API should be async; put the request in job tracker, get results and push back responses

##### News Listing Endpoint:
api.route('/news')
def function():
       1. Get all available APIs
       2. Call each API for getting top 10 news in JSON; Listing Function for Each API
       3. Aggregate news from all APIs, discard empty responses
       

##### News Search Endpoint
api.route('/news?query=bitcoin')
def function():
       1. Get all available APIs
       2. Call each API with search query to get top 10 results in JSON; Searching Function for Each API
       3. Aggregate results from all APIs, discard empty responses


##### Other Helper Functions
       1. News_API json parser for listing responses; 
          should return only required fields; ["title",  "link", "source"]
       2. Reddit_API json parser for listing results


##### Steps to Add any New API
       1. Make a new file for new API in ```src/external_api/```
       2. Take ```src/external_api/sample_api.py``` as reference
       3. Prepare API Mapping object
       4. Write JSON parser for that API
       5. Register your API in API_COLLECTION in ```src/api_helper.py```


### Prerequisites

To run this project, should install project dependencies:

1. Python3
2. pip
3. Intsall Python packages


<br>

### Instructions to Run


1. Clone the repo
```sh
git clone https://github.com/umairqadir97/news-aggregator-with-fastapi.git
```
2. Open terminal in project folder
```sh 
cd news-aggregator-with-fastapi
```

3. Install python packages
```sh
pip3 install -r requirements.txt
```

4. Run server
```sh
python3 api.py
```

##### You can run tests with: 
```sh
pytest
```

<br>

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/umairqadir97/news-aggregator-with-fastapi/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b amazing_features`)
3. Commit your Changes (`git commit -m 'Add some Amazing Features'`)
4. Push to the Branch (`git push origin amazing_features`)
5. Open a Pull Request


### Contribution guidelines
1. Writing more unit tests
2. Code review
3. Feature Enhancement

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Muhammad Umair Qadir - [Email](umairqadir97@gmail.com)

LinkedIn: [LinkedIn](https://linkedin.com/in/umairqadir)





<!-- MARKDOWN LINKS & IMAGES -->

<!-- Issues -->
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/umairqadir97/news-aggregator-with-fastapi/issues

<!-- Lisence -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/umairqadir97/news-aggregator-with-fastapi/blob/master/LICENSE.txt

<!-- LinkedIn -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/umairqadir

<!-- Product Screenshot -->
[product-screenshot]: reports/news_aggregator_ss.png
