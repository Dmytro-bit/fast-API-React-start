from fastapi import FastAPI, Body
from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    name: str


class InsertCar(BaseModel):
    brand: str
    model: str
    year: int


app = FastAPI()


@app.post("/cars")
async def new_car_model(car: InsertCar, user: UserModel, code: int = Body(None)):
    return {"car": car, "user": user, "code": code}
