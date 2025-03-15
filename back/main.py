from fastapi import FastAPI
from database import init_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()

@app.post("/")
async def root():
    return {"message": "Hello World"}
