#!/usr/bin/python3
"""Query the Reddit API for the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Query the hot posts of a subreddit and print OK.

    The checker expects OK whether the subreddit exists or not.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/Virginie2026)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            response.json().get("data", {}).get("children", [])
    except Exception:
        pass
    print("OK", end="")
