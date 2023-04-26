#!/usr/bin/python3

"""This uses the provided api to print stuff
Here we use json api to get info about a specific employee
Then we write this info to a csv file"""

import csv
import requests
import sys
if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    name = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    u_name = name.get('username')
    todo = requests.get("{}todos?userId={}".format(url, sys.argv[1])).json()
    for val in todo:
        val.update({"username": u_name})
        val.pop('id')
    with open("{}.csv".format(sys.argv[1]), 'w') as fp:
        columns = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(fp, fieldnames=columns,
                                delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for to in todo:
            writer.writerow(to)
