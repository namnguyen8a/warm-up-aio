from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

items = [
    {
        "name": "Banh thap cam",
        "price": 45.0,
        "description": "Description of the banh trung thu thap cam",
    },
    {
        "name": "Banh Dau xanh",
        "price": 40.0,
        "description": "Description of the banh dau xanh",
    },
]

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0, description="Price of the mooncake")
    description: str | None = Field(
        None, max_length=500, description="Optional description"
    )

@app.get("/search_items/")
async def search_items(
    q: Annotated[str, Query(min_length=3, max_length=50, description="Search query")],
    max_price: Annotated[float | None, Query(gt=0, description="Maximum price")] = None,
):
    results = [item for item in items if q.lower() in item["name"].lower()]

    if max_price:
        results = [item for item in results if item["price"] <= max_price]
    
    return results

# Purpose: Add metadata to Pydantic models
# Annotated: Used for adding custom metadata to types
# Field: User for:
# - Defining model field details (e.g., default values, validation)
# - Including metadata for documentation or serialization