#!/usr/bin/python3
"""Query the Reddit API for the subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit, or 0 if invalid."""
    if not isinstance(subreddit, str) or not subreddit:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/alu_student)"}
    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
    except requests.RequestException:
        return 0
    if response.status_code != 200:
        return 0
    try:
        return response.json().get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
