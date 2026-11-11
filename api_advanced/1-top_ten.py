#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    Prints None if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/Virginie2026)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        posts = response.json().get("data", {}).get("children", [])
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
