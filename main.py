from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory DB
db: dict[int, "Item"] = {}

# --- Hello World (slide 02) ---
@app.get("/")
def read_root():
    return {"message": "Hello, API!"}

# --- Path & Query Params (slide 03) ---
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(404, "Not found")
    return db[item_id]

@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}

# --- Request Bodies (slide 04) ---
class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # default -> optional

# --- Methods & Responses (slide 05) ---
@app.post("/items", status_code=201)
def create_item(item: Item):
    db[item.id] = item
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(404, "Not found")
    db[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(404, "Not found")
    del db[item_id]
    return {"deleted": item_id}

# --- Async & Deps (slide 06) ---
@app.get("/data")
async def get_data():
    return {"data": "async response"}

# --- Full Example / CRUD (slide 07) ---
@app.get("/items")
def list_items():
    return list(db.values())