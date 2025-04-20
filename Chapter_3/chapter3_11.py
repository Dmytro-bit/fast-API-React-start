from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    id: int = Field()
    username: str = Field(max_length=20, min_length=5)
    email: EmailStr = Field()
    password: str = Field(min_length=5, max_length=20, pattern="^[a-zA-Z0-9]+$")


u = UserModel(
    id=1,
    username="freethrow",
    email="emai@gmail.com",
    password="password123", )

print(u.model_dump())
print(u.model_dump_json(exclude={"password"}))
