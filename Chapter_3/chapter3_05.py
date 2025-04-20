from datetime import datetime

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int = 2
    username: str
    email: str
    dob: datetime
    favorite_color: list[str] | None = ["red", "green", "blue"]


try:
    user = User(id=1, username="johndoe", email="johndoe@me.com", dob=datetime.now())
    print(user)
except ValidationError as e:
    print(e.json())
