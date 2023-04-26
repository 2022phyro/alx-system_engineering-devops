#!/usr/bin/python3

"""This uses the provided api to print stuff
Here we use json api to print out a specific employee"""


import requests
import sys
url = "https://jsonplaceholder.typicode.com/"
name = requests.get("{}users/{}".format(url, sys.argv[1])).json()['name']
todo = requests.get("{}todos?userId={}".format(url, sys.argv[1])).json()
print("Employee {} is done with".format(name), end=" ")
completed = 0
i = 0
for val in todo:
    if val['completed']:
        completed += 1
    i += 1
print("tasks({}/{})".format(completed, i))
for val in todo:
    if val['completed']:
        print("\t {}".format(val['title']))
