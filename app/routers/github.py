from fastapi import APIRouter
from app.services.analyzer import (
    analyze_developer,
    analyze_languages
)

import requests
import os

router = APIRouter()


@router.get("/profile/{username}")
def get_profile(username: str):

    try:

        # User profile API

        user_url = f"https://api.github.com/users/{username}"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
            "User-Agent": "GitWrapped-App"
        }

        user_response = requests.get(
            user_url,
            headers=headers
        )

        if user_response.status_code != 200:

            return {
                "error":
                f"GitHub user not found ({user_response.status_code})"
            }

        user_data = user_response.json()

        # Repositories API

        repos_url = f"https://api.github.com/users/{username}/repos"

        repos_response = requests.get(
            repos_url,
            headers=headers
        )

        repos_data = repos_response.json()

        # Main profile data

        profile_data = {

            "username": user_data.get("login"),

            "name": user_data.get("name"),

            "bio": user_data.get("bio"),

            "public_repos": user_data.get("public_repos"),

            "followers": user_data.get("followers"),

            "following": user_data.get("following"),

            "profile_url": user_data.get("html_url"),

            "avatar": user_data.get("avatar_url")
        }

        # Developer analysis

        developer_analysis = analyze_developer(
            profile_data["public_repos"],
            profile_data["followers"]
        )

        # Language analysis

        language_analysis = analyze_languages(
            repos_data
        )

        # Final response

        return {

            **profile_data,

            "developer_analysis":
                developer_analysis,

            "language_analysis":
                language_analysis
        }

    except Exception as e:

        return {
            "error": str(e)
        }
    
    