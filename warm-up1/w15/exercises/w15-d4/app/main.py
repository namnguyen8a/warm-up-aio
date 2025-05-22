from fastapi import FastAPI
from app.routers import patients

app = FastAPI()

app.include_router(patients.router)

@app.get("/ping")
async def get_access():
    return {"pong"}