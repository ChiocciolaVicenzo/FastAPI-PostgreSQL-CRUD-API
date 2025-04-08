from pydantic import BaseModel, Field

class ArticlesBase(BaseModel):
    title: str
    content: str
    author: str

class ArticlesCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=40)
    content: str = Field(..., min_length=10)
    author: str = Field(..., min_length=2)

class ArticlesOut(ArticlesBase):
    id: int

    class Config:
        from_attributes = True