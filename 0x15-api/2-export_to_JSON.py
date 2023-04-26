#!/usr/bin/python3

"""This uses the provided api to print stuff
Here we use json api to print out info about a specific employee
Then we save this information to a file in json format"""

import csv
import json
import requests
import sys
if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    name = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    u_name = name.get('username')
    todo = requests.get("{}todos?userId={}".format(url, sys.argv[1])).json()
    end_dict = {}
    list_ = []
    for val in todo:
        end_dict.update({"task": val.get('title')})
        end_dict.update({"completed": val.get('completed')})
        end_dict.update({"username": u_name})
        list_.append(end_dict)
    with open("{}.json".format(sys.argv[1]), 'w') as fp:
        json.dump({sys.argv[1]: list_}, fp)
