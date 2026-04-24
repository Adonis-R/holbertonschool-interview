#!/usr/bin/python3
"""Module for counting keywords in Reddit hot article titles."""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Recursively query Reddit API and count keyword occurrences in titles.

    Args:
        subreddit: subreddit name to query
        word_list: list of keywords to count (case-insensitive)
        counts: dict accumulating keyword counts across recursive calls
        after: pagination token for the next page of results
    """
    if counts is None:
        counts = {}
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "count_words/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            stripped = word.strip(".,!?;:\"'()[]{}")
            if stripped in counts:
                counts[stripped] += 1

    next_after = data.get("after")
    if next_after:
        count_words(subreddit, word_list, counts, next_after)
    else:
        results = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in results:
            if count > 0:
                print("{}: {}".format(word, count))
