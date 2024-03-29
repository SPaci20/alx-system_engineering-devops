#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "web:ll04-6IuWkz_3ve6YaEZw:v1.0.0 (by /u/SPaci20)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for successful response (status code 200)
    if response.status_code == 200:
        try:
            results = response.json().get("data")
            return results.get("subscribers")
        except ValueError as e:
            print(f"Error parsing JSON: {e}")
            return 0
    elif response.status_code == 404:
        return 0
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print the response content for debugging
        return 0
