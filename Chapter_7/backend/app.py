from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor import motor_asyncio

from config import BaseConfig
from routers.cars import router as car_router
from routers.users import router as users_router

settings = BaseConfig()

origins = ['*']


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.client = motor_asyncio.AsyncIOMotorClient(settings.MONGO_DB_URI)
    app.db = app.client[settings.MONGO_DB_NAME]

    try:
        app.client.admin.command("ping")
        print("Pinged your deployment. You have successfully connected to MongoDB!")
        print("Mongo address:", settings.MONGO_DB_URI)
    except Exception as e:
        print(e)

    yield
    app.client.close()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(car_router, prefix="/cars", tags=["cars"])
app.include_router(users_router, prefix="/users", tags=["users"])


@app.get("/")
async def get_root():
    return {"message": "Root working"}
