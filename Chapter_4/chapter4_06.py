from typing import Dict

from fastapi import FastAPI, Body

app = FastAPI()



@app.post("/cars")
async def post_cars(data: Dict = Body(...)) -> Dict[str, Dict]:
    print(data)
    return {"massage": data}
