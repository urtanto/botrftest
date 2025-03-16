import json

from fastapi import FastAPI, Request
from database import init_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.post("/create_card")
async def root(request: Request):
    body = await request.body()
    body_json = json.loads(body.decode("utf-8"))

    print(json.dumps(body_json, indent=2))

    return {"message": "Hello World"}
