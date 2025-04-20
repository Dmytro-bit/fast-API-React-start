from typing import Literal

from pydantic import BaseModel, Field

external_api_data = {
    "user_id": 234,
    "name": "Marko",
    "email": "email@gmail.com",
    "account_type": "personal",
    "nick": "freethrow",
}


class UserModelFields(BaseModel):
    id: int = Field(alias="user_id")
    username: str = Field(alias="name")
    email: str = Field()
    account: Literal["personal", "business"] | None = Field(alias="account_type", default=None)
    nickname: str | None = Field(default=None, alias="nick")


user = UserModelFields.model_validate(external_api_data)
print(user)