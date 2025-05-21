from fastapi import FastAPI, UploadFile, File, Form
import shutil

app = FastAPI()


@app.post("/upload")
async def upload(picture: UploadFile = File(...), brand: str = Form(...), model: str= Form(...)):
    with open("saved_file.png", "wb") as buffer:
        shutil.copyfileobj(picture.file, buffer)
    return {"brand": brand, "model": model, "file_name": picture.filename}