from fastapi import FastAPI, status

app = FastAPI()

@app.get("/", status_code=status.HTTP_208_ALREADY_REPORTED)
async def raw_response():
    return {"message": "Fast API response"}