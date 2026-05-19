def analyze_developer(public_repos, followers):

    if public_repos < 10:
        developer_type = "Casual Coder"

    elif public_repos < 50:
        developer_type = "Open Source Explorer"

    else:
        developer_type = "Code Wizard"

    if followers == 0:
        fame_level = "Future Legend 🌱"

    elif followers < 50:
        fame_level = "Underground Builder"

    elif followers < 500:
        fame_level = "Rising Developer"

    else:
        fame_level = "GitHub Celebrity"

    return {
        "developer_type": developer_type,
        "fame_level": fame_level
    }


def analyze_languages(repos):

    language_count = {}

    for repo in repos:

        language = repo["language"]

        if language is None:
            continue

        if language in language_count:
            language_count[language] += 1

        else:
            language_count[language] = 1

    if not language_count:

        favorite_language = "Unknown"

    else:

        favorite_language = max(
            language_count,
            key=language_count.get
        )

    if favorite_language == "Python":

        personality = "Python Wizard 🐍"

    elif favorite_language == "JavaScript":

        personality = "Frontend Magician ✨"

    elif favorite_language == "Java":

        personality = "Enterprise Warrior ☕"

    elif favorite_language == "C++":

        personality = "Memory Master ⚡"

    elif favorite_language == "Go":

        personality = "Backend Speed Demon 🚀"

    elif favorite_language == "HTML":

        personality = "Frontend Artist 🎨"

    else:

        personality = "Open Source Explorer 🌍"

    return {
        "favorite_language": favorite_language,
        "language_breakdown": language_count,
        "developer_personality": personality
    }