from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# list to persist items
items = []


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/hello")
def hello():
    return {"Hello": "World"}


@app.get("/item/{name}")
def get_item(name: str):
    return {"name": name, "price": 19.99, "is_offer": True}


@app.post("/item")
def create_item(item: Item):
    items.append(item)


@app.get("/items")
def get_items():
    return items
