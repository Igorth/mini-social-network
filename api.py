from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()


# Define pydantic models
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class PostCreate(BaseModel):
    username: str
    content: str


class PostResponse(BaseModel):
    post_id: int
    author: str
    content: str
    timestamp: str


# Initialize in-memory storage
class InMemoryStorage:
    users = {}
    posts = []
    post_count = 0


storage = InMemoryStorage()


@app.post("/users/")
async def register_user(user: UserCreate):
    if user.username in storage.users:
        raise HTTPException(status_code=400, detail="Username already registered")
    # Mocked user creation logic
    storage.users[user.username] = user
    return {"message": "User registered successfully", "user": user}


@app.post("/posts/", response_model=PostResponse)
async def create_post(post: PostCreate):
    if post.username not in storage.users:
        raise HTTPException(status_code=400, detail="User not found")

    post_id = len(storage.posts) + 1
    new_post = {
        "post_id": post_id,
        "author": post.username,
        "content": post.content,
        "timestamp": "2024-08-30T12:00:00Z"  # Mocked timestamp
    }
    storage.posts.append(new_post)
    return new_post


@app.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    post = next((p for p in storage.posts if p["post_id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.get("/users/{username}")
async def get_user(username: str):
    user = storage.users.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
