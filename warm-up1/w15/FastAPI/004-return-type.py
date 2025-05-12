from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Banh trung thu thap cam", price=45.0),
        Item(name="Banh trung thu dau xanh", price=40.0),
    ]

