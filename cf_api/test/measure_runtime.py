import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(ROOT_DIR))

from time import time
from requests import post
from json import dumps
from random import sample
from statistics import mean
from argparse import ArgumentParser

from cf_api.utils.utils import load_json

TOKEN = "serdarakyol55@outlook.com"
API_URL = "http://0.0.0.0:1234/api/collaborativefilter"

def request_api(input_data) -> dict:
    result_status_code = -1
    result_data = None
    try:
        headers = {'token': TOKEN, 'content-type': 'application/json'}
        post_data = dumps({
            "item": [
            "HBV00000PQP07"
            ],
            "n_item": 5
        })
        #print("Request sent")
        req_api = post(API_URL, data=post_data, headers=headers)
        
        if req_api.status_code == 200:
            #print("Processed successfully.")
            result_status_code = req_api.status_code
            result_data = req_api.json()
        else:
            print("ERROR! - ", req_api.text)
    except Exception as error:
        print(f"Error occurred {str(error)}")
    
    return result_status_code, result_data

def calculate_runtime(path, total_request:int, n_item:int):
    product_json_path = ROOT_DIR + path
    products = load_json(product_json_path)
    products = [prod['productid'] for prod in products['meta']]
    # shufftle list
    products = sample(products, len(products))

    
    all_runtime = []
    counter = 0
    for i in range(total_request):
        temp = {
                "item": [],
                "n_item": n_item
            }

        temp_list = products[i:counter]
        for item in temp_list:
            temp["item"].append(item)
        counter += n_item

        if i%100 == 0 and i !=0:
            print(f"{str(i)}. request sent")

        start = time()
        result_code, resut_data = request_api(input_data=temp)
        all_runtime.append(time()-start)
    
    return all_runtime, total_request

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-tr", "--total_request", type=int, help="Number of total request", required=True)
    parser.add_argument("-n", "--n_item", type=int, help="Number of suggestion product", required=True)
    args = parser.parse_args()

    all_runtime, total_request = calculate_runtime(
        path="/data/meta.json", 
        total_request=args.total_request, 
        n_item=args.n_item
    )

    print(f"Average of API response {str(mean(all_runtime))}")
    print(f"Highest latency of API is {str(max(all_runtime))}")
    print(f"The best response time of API is {str(min(all_runtime))}")
    # for check if really sent 1K request
    if len(all_runtime) == total_request:
        print(f"Succesfully sent {str(len(all_runtime))} requests")
    else:
        print(f"Missing {str(total_request - len(all_runtime))}")