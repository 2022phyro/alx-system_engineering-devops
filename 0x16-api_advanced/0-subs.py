#!/usr/bin/python3
"""This file atempts no 0"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'my_bot/1.0 by my_username'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    x = response.json().get('data').get('subscribers')
    if x:
        return x
    return 0
