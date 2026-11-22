from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# --- Hello World (slide 02) ---
@app.get("/")
def read_root():
    return {"message": "Hello, API!"}

# --- Path & Query Params (slide 03) ---
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}

# --- Request Bodies (slide 04) ---
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True  # default -> optional

@app.post("/items")
def create_item(item: Item):
    return {"name": item.name, "total": item.price * 1.2}