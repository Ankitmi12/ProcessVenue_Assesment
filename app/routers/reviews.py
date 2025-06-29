from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/{book_id}/reviews", response_model=List[schemas.Review])
def read_reviews(book_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews_by_book_id(db, book_id)

@router.post("/{book_id}/reviews", response_model=schemas.Review)
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, book_id, review)
