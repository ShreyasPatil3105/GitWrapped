from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import github

app = FastAPI(
    title="GitWrapped 🚀",
    description="Spotify Wrapped for Developers",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(github.router)

@app.get("/")
def home():

    return {
        "project": "GitWrapped",
        "message": "Spotify Wrapped for Developers 🚀"
    }
