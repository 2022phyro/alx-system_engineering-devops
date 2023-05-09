#!/usr/bin/python3
"""This file atempts no 0"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively get all posts"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    headers = {
            'User-Agent': 'my_bot/1.0 by my_username',
            }
    if after:
        params = {'after': after}
    else:
        params={}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return hot_list
    print(response.status_code)
    for k in response.json().keys:
        print(k)
    """
    domain = response.json().get('data').get('children')
    if not domain:
        return hot_list
    hot_list += [x.get('data').get('title') for x in domain]
    print(len(set(hot_list)))
    x = domain[-1]['data']['id']
    return hot_list
#    return recurse(subreddit, hot_list, after=x)"""
