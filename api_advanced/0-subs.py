#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit.

    Returns 0 if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/Virginie2026)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except Exception:
        return 0
