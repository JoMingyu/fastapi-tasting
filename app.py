from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI 시식회", docs_url=None, redoc_url="/docs", openapi_url=None)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: int = None):
    return {"item_id": item_id, "q": q}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


class X(str, Enum):
    A = "a"
    B = "b"
    C = "c"


@app.get("/enum/{x}")
def query_with_enum(x: X):
    return {"value": x}


@app.get("/files/{file_path:path}")
def get_file(file_path):
    return {"path": file_path}


@app.get("/bool/{x}")
def handle_bool_path_param(x: bool, q: bool):
    return {"path": x, "qs": q}


class Item(BaseModel):
    name: str
    description: str
    sellPrice: float
    buyPrice: float


@app.post("/items")
def add_item(item: Item):
    return item.dict()
