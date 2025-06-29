from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Review Schemas
class ReviewBase(BaseModel):
    review_text: str
    rating: int = Field(..., ge=1, le=5)

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Book Schemas
class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    created_at: datetime
    reviews: Optional[List[Review]] = []

    class Config:
        orm_mode = True
