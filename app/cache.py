from datetime import datetime
import redis
import json
from app.schemas import Book
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

CACHE_KEY_BOOKS = "books"

def get_books_from_cache() -> List[Book]:
    data = r.get("books")
    if data:
        print("Cache HIT: /books")
        return json.loads(data)
    print("Cache MISS: /books")
    return None


def set_books_in_cache(books):
    print("Updating Redis cache: /books")

    try:
        books_data = [Book.from_orm(book).dict() for book in books]

        def serialize(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return obj

        books_json = json.dumps(books_data, default=serialize)

        result = r.set("books", books_json, ex=300)
        print("📬 Redis SET result:", result)

    except Exception as e:
        print("Redis SET failed:", e)



