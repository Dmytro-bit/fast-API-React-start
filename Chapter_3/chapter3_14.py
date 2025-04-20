from pydantic import BaseModel, field_validator


class Article(BaseModel):
    id: int
    title: str
    content: str
    published: bool = False

    @field_validator("title")
    @classmethod
    def check_title(cls, value: str) -> str:
        if "FARM stack" not in value:
            raise ValueError("Title must contain 'FARM stack'")
        return value.title()


article = Article.model_validate({"id": 1, "title": "FARM stack title", "content": "content"})
print(article)

article2 = Article(**{"id": 1, "title": "FARM stack title", "content": "content"})
print(article2)
