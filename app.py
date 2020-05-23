from fastapi import FastAPI

app = FastAPI(title="FastAPI 시식회", docs_url=None, redoc_url="/docs", openapi_url=None)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
