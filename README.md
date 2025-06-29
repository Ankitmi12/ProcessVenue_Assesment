# 📚 Book Review API

A fully functional backend service for managing books and their reviews, built with **FastAPI**, **PostgreSQL**, **Redis**, and **Alembic**.

---

## 🚀 Features

- CRUD APIs for books and their reviews  
- Redis caching for `/books` endpoint  
- PostgreSQL with Alembic for migrations  
- Modular project structure  
- Swagger and ReDoc auto-generated docs  
- Environment-based configuration using `.env`  
- Unit and integration tests with Pytest  

---

## 🧱 Tech Stack

| Layer      | Tool/Library       |
|------------|--------------------|
| Language   | Python 3.8+        |
| Framework  | FastAPI            |
| Database   | PostgreSQL         |
| ORM        | SQLAlchemy         |
| Caching    | Redis              |
| Migrations | Alembic            |
| Testing    | Pytest, TestClient |
| Docs       | Swagger (OpenAPI)  |

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ankitmi12/ProcessVenue_Assesment.git
cd ProcessVenue_Assesment/book_review_api
```

---

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=book_review
DB_USER=postgres
DB_PASSWORD=your_password
REDIS_HOST=localhost
REDIS_PORT=6379
```

---

## 🛠 Database Setup

### 1. Start PostgreSQL and Create DB

```sql
CREATE DATABASE book_review;
```

### 2. Run Alembic Migrations

```bash
alembic upgrade head
```

---

## 🔁 Redis Setup

```bash
sudo apt update
sudo apt install redis-server
redis-server
```

✅ Confirm it's running:

```bash
redis-cli ping
# PONG
```

---

## 🟢 Run the Application

```bash
uvicorn app.main:app --reload
```

Open in browser:

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔗 API Endpoints

| Method | Endpoint              | Description                   |
| ------ | --------------------- | ----------------------------- |
| GET    | `/books/`             | List all books (Redis cached) |
| POST   | `/books/`             | Add a new book                |
| GET    | `/books/{id}/reviews` | Get reviews for a book        |
| POST   | `/books/{id}/reviews` | Add review to a book          |

---

## ✅ Testing

Make sure Redis & PostgreSQL are running.

Run tests:

```bash
PYTHONPATH=. pytest tests/
```

Tests cover:

* Book creation
* Review creation
* Cache integration for `/books`

---

## 📦 Folder Structure

```
book_review_api/
│
├── app/
│   ├── main.py            # FastAPI app setup
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # DB interactions
│   ├── cache.py           # Redis caching logic
│   ├── database.py        # DB connection
│   └── routers/
│       ├── books.py
│       └── reviews.py
│
├── tests/
│   ├── test_books.py
│   └── test_reviews.py
│
├── migrations/            # Alembic migrations
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```


## 🧠 Author

**Ankit Mishra**
💼 GitHub: [@Ankitmi12](https://github.com/Ankitmi12)
📧 Email: [ankitmishra.dev@gmail.com](mailto:ankitmishra.dev@gmail.com)

---

## 📌 License

This project is for technical evaluation only.
