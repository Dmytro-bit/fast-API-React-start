from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()


class InsertCar(BaseModel):
    brand:str
    model:str
    year: int


@app.post("/carsmodel",status_code=status.HTTP_201_CREATED)
async def new_car_model(car: InsertCar):
    if car.year > 2022:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE, detail="The car does not exist yet!"
        )
    return {"car": car}