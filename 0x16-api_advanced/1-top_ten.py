#!/usr/bin/python3

"""Function to print top 10 hot posts on a given Reddit subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            results = response.json().get("data")
            if results:
                for child in results.get("children"):
                    print(child.get("data").get("title"))
            else:
                print("None")
        else:
            print("None")
    except requests.RequestException as e:
        print("Error occurred:", e)
        print("None")


# Test the function
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
