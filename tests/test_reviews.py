from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_review():
    # Create book first
    book_resp = client.post("/books/", json={"title": "Review Book", "author": "Ankit"})
    book_id = book_resp.json()["id"]

    # Add review
    review_resp = client.post(f"/books/{book_id}/reviews", json={
        "review_text": "Great book!",
        "rating": 5
    })
    assert review_resp.status_code == 200
    assert review_resp.json()["rating"] == 5

def test_get_reviews():
    # Create book
    book_resp = client.post("/books/", json={"title": "Review Book 2", "author": "Ankit"})
    book_id = book_resp.json()["id"]

    # Add review
    client.post(f"/books/{book_id}/reviews", json={"review_text": "Nice", "rating": 4})

    # Fetch reviews
    resp = client.get(f"/books/{book_id}/reviews")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
