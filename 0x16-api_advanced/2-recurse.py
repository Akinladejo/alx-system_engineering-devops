#!/usr/bin/python3
"""Module for task 2"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns all hot posts of the subreddit"""
    BASE_URL = 'http://reddit.com/r/{}/hot.json'
    headers = {'User-Agent': 'My-User-Agent'}
    params = {'limit': 100}

    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list

    response = requests.get(BASE_URL.format(subreddit),
                            headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    after = data.get('after', 'STOP')

    if not after:
        after = "STOP"

    hot_list += [post.get('data', {}).get('title')
                 for post in data.get('children', [])]

    return recurse(subreddit, hot_list, after)
