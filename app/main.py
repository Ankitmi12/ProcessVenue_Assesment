from fastapi import FastAPI
from app.routers import books, reviews

app = FastAPI(
    title="Book Review API",
    description="API for managing books and their reviews",
    version="1.0.0"
)

# Include routers
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(reviews.router, prefix="/books", tags=["Reviews"])
