from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root()-> dict[str, str]:
    return {"message": "Hello FastAPI"}


@app.post("/")
async def post_root() -> dict[str, str]:
    return {"message": "Post request success"}
