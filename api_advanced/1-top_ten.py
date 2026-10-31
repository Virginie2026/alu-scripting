#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first
10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'alu-scripting-agent/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get("data", {})
            posts = data.get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        except ValueError:
            print(None)
    else:
            print(None)
