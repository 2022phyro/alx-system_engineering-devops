#!/usr/bin/python3

"""This uses the provided api to get info about users
Here we use json api to get out info about all users
Then we save this information to a file in json format"""

import json
import requests
if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()
    end = {}
    for user in users:
        i = user.get('id')
        todo = requests.get("{}todos?userId={}".format(url, i)).json()
        list_ = []
        for val in todo:
            end_dict = {}
            end_dict.update({"username": user.get('username')})
            end_dict.update({"task": val.get('title')})
            end_dict.update({"completed": val.get('completed')})
            list_.append(end_dict)
        end.update({i: list_})
    with open("todo_all_employees.json", 'w') as fp:
        json.dump(end, fp)
