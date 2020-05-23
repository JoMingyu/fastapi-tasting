from fastapi import FastAPI

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
