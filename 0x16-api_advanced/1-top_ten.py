#!/usr/bin/python3
"""This file atempts no 0"""
import requests


def top_ten(subreddit):
    """Gets the top ten spots"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {'User-Agent': 'my_bot/1.0 by my_username'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
    domain = response.json().get('data').get('children')
    if domain:
        for i in range(10):
            print(domain[i].get('data').get('title'))
    else:
        print("None")
