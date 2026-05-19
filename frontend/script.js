async function getProfile() {

    try {

        const username =
            document.getElementById("username").value;

        document.getElementById("loading").innerHTML =
            "🚀 Analyzing Developer...";

        const response = await fetch(
            `http://127.0.0.1:8000/profile/${username}`
        );

        const data = await response.json();

        document.getElementById("loading").innerHTML = "";

        document.getElementById("profile-card").innerHTML = `

            <img
                class="profile-image"
                src="${data.avatar}"
            />

            <div class="name">
                ${data.name || data.username}
            </div>

            <div class="bio">
                ${data.bio || "No bio available"}
            </div>

            <div class="personality">
                ${data.language_analysis.developer_personality}
            </div>

            <div class="stat-card">
                💡 Building the future one commit at a time
            </div>

            <div class="stats">

                <div class="stat-card">
                    ⭐ Favorite Language:
                    ${data.language_analysis.favorite_language}
                </div>

                <div class="stat-card">
                    👥 Followers:
                    ${data.followers}
                </div>

                <div class="stat-card">
                    🚀 ${data.developer_analysis.fame_level}
                </div>

            </div>

            <a
                class="github-btn"
                href="${data.profile_url}"
                target="_blank"
            >
                🔗 View GitHub Profile
            </a>

        `;

    } catch (error) {

        console.error(error);

        document.getElementById("loading").innerHTML =
            "❌ Something went wrong";
    }
}

document
    .getElementById("username")
    .addEventListener("keypress", function(event) {

        if (event.key === "Enter") {

            getProfile();
        }
});