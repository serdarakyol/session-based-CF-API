# Recommendation system for e-commerce (Session based Collaborative Filtering)
This repository contains Jupyter Notebook and Python. Jupyter Notebook used for preprocessing and manilulation the data. Python used for API

For that project used 10K products and 54K session

# Run time test
Each request is unique, contain n different product and returns n products for recommend. Please note that, the project tested on **12th Gen Intel(R) Core(TM) i7-12700H** CPU. For that CPU. Runtime table as below
Number of API Request | Average latency (ms) | Lowest latency (ms) | Highest latency (ms) | n product per request | n product per response
--- | --- | --- | --- | --- | ---
100 | 138 | 130 | 173 | 10 | 10
1000 | 151 | 132 | 232 | 5 | 5
3000 | 138 | 131 | 182 | 3 | 3
# Usage
That project developed on Python 3.9. For run that repository, just run below code
```
$ git clone https://github.com/serdarakyol/session-based-CF-API.git
$ cd session-based-CF-API/
$ bash prepare_api.sh
```
Please note that prepare_api.sh creates necessary folders, download files and fill to make ready to API. For more information [click](prepare_api.sh)

## Docker
```
$ docker image build -t cf_api:0.0.1 .
$ docker run -dp 1234:1234 cf_api:0.0.1
```
