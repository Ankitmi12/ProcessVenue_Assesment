from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas

# Books
def get_books(db: Session) -> List[models.Book]:
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Reviews
def get_reviews_by_book_id(db: Session, book_id: int) -> List[models.Review]:
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()

def create_review(db: Session, book_id: int, review: schemas.ReviewCreate) -> models.Review:
    db_review = models.Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
