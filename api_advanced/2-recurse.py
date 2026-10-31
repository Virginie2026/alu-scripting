#!/usr/bin/python3
"""
Recursive module to query the Reddit API and return a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles
    of all hot posts for a given subreddit. Returns None if invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alu-scripting-agent/1.0'}
    params = {'after': after} if after else {}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after")

        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)
        
        return hot_list if hot_list else None
    except ValueError:
        return None
