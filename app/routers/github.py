from fastapi import APIRouter
from app.services.analyzer import analyze_developer
import requests
import os

router = APIRouter()

@router.get("/profile/{username}")
def get_profile(username: str):

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

    profile_data = {
        "username": data.get("login"),
        "name": data.get("name"),
        "bio": data.get("bio"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "profile_url": data.get("html_url"),
        "avatar": data.get("avatar_url")
    }

    profile_data["developer_analysis"] = analyze_developer(
        profile_data
    )

    return profile_data