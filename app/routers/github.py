import os
from fastapi import APIRouter
from app.services.analyzer import analyze_developer
import requests

router = APIRouter()


def get_github_profile(username):

    url = f"https://api.github.com/users/{username}"


    headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
    "User-Agent": "GitWrapped-App"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:

        return {
            "error": f"GitHub user not found ({response.status_code})"
        }

    data = response.json()

    return {
        "username": data.get("login"),
        "name": data.get("name"),
        "bio": data.get("bio"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "profile_url": data.get("html_url"),
        "avatar": data.get("avatar_url")
    }


@router.get("/profile/{username}")
def profile(username: str):

    profile_data = get_github_profile(username)

    if "error" in profile_data:
        return profile_data

    analysis = analyze_developer(profile_data)

    return {
        **profile_data,
        **analysis
    }
