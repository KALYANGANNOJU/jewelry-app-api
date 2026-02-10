# Jewelry App API (Backend Project)

This project is a backend REST API for a Jewelry Application built using **FastAPI** and **SQLite**.  
It provides APIs to manage products, categories, and users with filtering and sorting features.

This project is developed as part of the Python Backend Development Internship Task.

---

## 🚀 Features

- CRUD operations for Products
- Category management
- User registration and login
- Password hashing using passlib
- Filter products by price range and metal
- Sort products by price (low to high / high to low)
- Swagger UI for API testing

---

## 🛠️ Technology Stack

- Python 3.7+
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Passlib (for password hashing)
- Swagger UI (for API testing)

---

---

## ▶️ How to Run the Project

### Step 1: Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate


### Step 2: Install dependencies
pip install -r requirements.txt

If you get errors, install manually:
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] email-validator


---

### Step 3: Run the server
python main.py


or

uvicorn main:app --reload


---

### Step 4: Open Swagger UI
Open in browser:
http://127.0.0.1:8000/docs


---

## 📌 API Endpoints

### Products API
- GET /api/products
- GET /api/products/{id}
- POST /api/products
- PUT /api/products/{id}
- DELETE /api/products/{id}

### Categories API
- GET /api/categories
- GET /api/categories/{id}/products

### Filters & Sorting
- /api/products?min_price=100&max_price=1000
- /api/products?metal=gold
- /api/products?sort_by=price&order=asc
- /api/products?sort_by=price&order=desc

### Users API
- POST /users (register user)
- POST /users/login (login user)

---

## 🧪 Example POST /users Request

```json
{
  "name": "Kalyan",
  "email": "kalyan@gmail.com",
  "password": "123456"
}
⚠️ Common Errors and Solutions
Error: uvicorn not recognized
pip install uvicorn

Error: email-validator not installed

pip install email-validator

Error: passlib not installed

pip install passlib[bcrypt]

