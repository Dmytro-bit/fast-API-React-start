from authentication import AuthHandler
from fastapi import APIRouter, Body, HTTPException, Request, Response, Depends
from models import UserBase, UserIn, UserList
from starlette.responses import JSONResponse

router = APIRouter()
auth_handler = AuthHandler()


@router.post("/register", response_description="Register user")
async def register(request: Request, newUser: UserIn = Body(...)) -> UserBase:
    users = request.app.db["users"]
    newUser.password = auth_handler.get_password_hash(newUser.password)

    if existing_username := await users.find_one({"username": newUser["username"]}) is not None:
        raise HTTPException(status_code=409, detail="Username already taken")

    new_user = await users.insert_one(newUser)
    created_user = await users.find_one({"_id": new_user.inserted_id})
    return created_user


@router.post("/login", response_description="Login user")
async def login(request: Request, loginUser: UserIn = Body(...)) -> JSONResponse:
    users = request.app.db["users"]
    user = users.find_one({"username": loginUser["username"]})

    if (user is None) or (not auth_handler.verify_password(loginUser.password, user["password"])):
        raise HTTPException(status_code=401, detail="Invalid username and/or password ")
    token = auth_handler.encode_token(str(user["_id"]), user["username"])
    response = JSONResponse(content={"token": token, "username": user["username"], "user_id": user["_id"]})
    return response


@router.get("/me", response_description="My info")
async def me(request: Request, response: Response, user_data=Depends(auth_handler.auth_wrapper)):
    users = request.app.db["users"]
    currentUser = await users.find_one({"_id": user_data["user_id"]})
    return currentUser
