from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, models
from app.database import get_db
from app.cache import get_books_from_cache, set_books_in_cache
import redis

router = APIRouter()

@router.get("/", response_model=List[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    try:
        cached_books = get_books_from_cache()
        if cached_books:
            return cached_books
    except Exception:
        pass  # fallback to DB if Redis fails

    books = crud.get_books(db)
    try:
        print("🔁 Calling set_books_in_cache")
        set_books_in_cache(books)
    except Exception:
        pass  # ignore cache write if Redis fails

    return books

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)
