# 📚 Book Review API — FastAPI + PostgreSQL + Redis

A simple backend API for managing books and their reviews.

---

## 🚀 Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL + SQLAlchemy
- **Migrations:** Alembic
- **Cache:** Redis
- **Tests:** Pytest
- **Documentation:** Swagger UI (auto-generated)

---

## 📂 Features

- Create and fetch books
- Add and view reviews for each book
- Caching for `/books` using Redis
- Error fallback if cache is down
- Alembic migrations
- Unit + integration tests

---

## 🔧 Setup Instructions

### 1. Clone Repo

```bash
git clone <your_repo_url>
cd book_review_api
