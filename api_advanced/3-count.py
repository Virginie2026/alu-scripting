#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot articles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords found in hot titles.

    Case-insensitive, words delimited by spaces. Prints nothing if the
    subreddit is invalid or if no keyword matches.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/Virginie2026)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except Exception:
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title") or ""
        for word in title.lower().split():
            counts[word] = counts.get(word, 0) + 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    totals = {}
    for word in word_list:
        word = word.lower()
        if word in counts:
            totals[word] = totals.get(word, 0) + counts[word]

    for word, total in sorted(totals.items(), key=lambda kv: (-kv[1], kv[0])):
        print("{}: {}".format(word, total))
