from fastapi import FastAPI

app = FastAPI()


@app.get("/ready")
def read_root():
    return "ok"


@app.get("/health")
def read_root():
    return "ok"


@app.get("/user/{user_id}/profile")
def get_user_profile(user_id: str):
    return {"user_id": user_id}
