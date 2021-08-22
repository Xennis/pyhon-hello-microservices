import os
import urllib

import httpx
import requests
from fastapi import FastAPI, HTTPException

backend_host = os.getenv("BACKEND_HOST", "http://localhost:2501")


app = FastAPI()


@app.get("/ready")
def read_root():
    return "ok"


@app.get("/health")
def read_root():
    return "ok"


@app.get("/user/{user_id}/profile")
def get_user_profile(user_id: str):
    backend_url = urllib.parse.urljoin(backend_host, "/user/")
    resp = httpx.get(backend_url, params={"id": user_id})
    if resp.status_code == 404:
        raise HTTPException(status_code=404, detail="user not found")
    if resp.status_code != 200:
        raise HTTPException(status_code=500, detail="can not fetch user")
    return {"data": resp.json()}
