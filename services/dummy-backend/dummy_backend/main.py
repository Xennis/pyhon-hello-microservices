import asyncio

from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_user_db = {
    "dummy-123": {"name": "Tony", "age": 34},
    "dummy-987": {"name": "Maria", "age": 25},
}


@app.get("/user/")
async def get_user_data(id: str = ""):
    if not id:
        raise HTTPException(status_code=400, detail="parameter id is empty")
    # Fake a slow database access
    await asyncio.sleep(1)
    user_data = fake_user_db.get(id)
    if not user_data:
        raise HTTPException(status_code=404, detail="user not found")
    return user_data
