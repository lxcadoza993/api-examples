"""Minimal client for the JSONPlaceholder demo REST API.

Usage:
    pip install -r requirements.txt
    python python_client.py
"""

import sys

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT_SECONDS = 10


def list_posts(session, user_id=None, limit=3):
    """GET /posts, optionally filtered by user."""
    params = {"userId": user_id} if user_id is not None else None
    response = session.get(f"{BASE_URL}/posts", params=params, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()[:limit]


def get_post(session, post_id):
    """GET /posts/{id}. Returns None for a missing resource instead of raising."""
    response = session.get(f"{BASE_URL}/posts/{post_id}", timeout=TIMEOUT_SECONDS)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


def create_post(session, title, body, user_id=1):
    """POST /posts. The demo API echoes the record back with a generated id."""
    payload = {"title": title, "body": body, "userId": user_id}
    response = session.post(f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def main():
    with requests.Session() as session:
        session.headers.update({"Accept": "application/json"})

        print("-- list posts for user 1 --")
        for post in list_posts(session, user_id=1):
            print(f"  [{post['id']}] {post['title']}")

        print("\n-- fetch post 1 --")
        post = get_post(session, 1)
        print(f"  title: {post['title']}")

        print("\n-- fetch a post that does not exist --")
        missing = get_post(session, 9999)
        print(f"  result: {missing}")

        print("\n-- create a post --")
        created = create_post(session, "Example title", "Example body.")
        print(f"  server assigned id: {created['id']}")


if __name__ == "__main__":
    try:
        main()
    except requests.HTTPError as error:
        print(f"http error: {error}", file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as error:
        print(f"request failed: {error}", file=sys.stderr)
        sys.exit(1)
