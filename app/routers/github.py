from fastapi import APIRouter
from app.services.analyzer import analyze_developer
import requests
import os

router = APIRouter()

@router.get("/profile/{username}")
def get_profile(username: str):

    try:

        url = f"https://api.github.com/users/{username}"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
            "User-Agent": "GitWrapped-App"
        }

        response = requests.get(url, headers=headers)

        print("STATUS:", response.status_code)

        data = response.json()

        print(data)

        if response.status_code != 200:
            return {
                "error": f"GitHub user not found ({response.status_code})"
            }

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
        profile_data["public_repos"],
        profile_data["followers"]
        )

        return profile_data

    except Exception as e:

        return {
            "error": str(e)
        }
    