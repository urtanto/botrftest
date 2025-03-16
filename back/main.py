from datetime import datetime
import json

from fastapi import FastAPI, Request
from database import init_db
from database.models import TgUser

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.post("/create_card")
async def root(request: Request):
    body = await request.body()
    body_json = json.loads(body.decode("utf-8"))
    body_json["birth_date"] = str(datetime.fromisoformat(body_json["birth_date"].replace("Z", "+00:00")))

    print(json.dumps(body_json, indent=2))

    return {"id": "123"}
