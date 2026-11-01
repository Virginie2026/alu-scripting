#!/usr/bin/python3
"""Recursively query the Reddit API for all hot article titles."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of the titles of all hot articles of a subreddit.

    Uses pagination through the 'after' parameter, recursively.
    Returns None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/Virginie2026)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
    except Exception:
        return None

    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
