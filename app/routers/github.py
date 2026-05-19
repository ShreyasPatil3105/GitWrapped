from fastapi import APIRouter
import requests

from app.services.analyzer import (
    analyze_developer,
    analyze_languages
)

router = APIRouter()

@router.get("/profile/{username}")
def get_github_profile(username: str):

    # GitHub profile API
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "GitHub user not found"}

    data = response.json()

    # GitHub repos API
    repos_url = f"https://api.github.com/users/{username}/repos"

    repos_response = requests.get(repos_url)

    repos_data = repos_response.json()

    # Developer analysis
    analysis = analyze_developer(
        data["public_repos"],
        data["followers"]
    )

    # Language analysis
    language_analysis = analyze_languages(repos_data)

    return {
        "username": data["login"],
        "name": data["name"],
        "bio": data["bio"],
        "public_repos": data["public_repos"],
        "followers": data["followers"],
        "following": data["following"],
        "profile_url": data["html_url"],
        "avatar": data["avatar_url"],
        "developer_analysis": analysis,
        "language_analysis": language_analysis
    }