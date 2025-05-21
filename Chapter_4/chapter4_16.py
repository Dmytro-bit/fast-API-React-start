from fastapi import FastAPI

from routers.cars import router as cars_router
from routers.users import router as user_router

app = FastAPI()

app.include_router(cars_router, prefix="/cars", tags=["cars"])
app.include_router(user_router, prefix="/users", tags=["users"])
