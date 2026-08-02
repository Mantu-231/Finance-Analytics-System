# Finance Analytics System

A Python-based financial management and analytics system that tracks income and expenses, provides REST APIs, performs financial analysis, and generates visualization reports.

The project is built using **FastAPI**, **SQLite**, **Pandas**, and **Matplotlib** with JWT based user authentication.

---

# Features

- User registration
- User login
- JWT authentication
- Protected REST APIs
- Add financial transactions
- View user transactions
- Delete transactions
- Calculate total income
- Calculate total expenses
- Calculate savings
- Category-wise expense analysis
- Generate financial charts
- SQLite database integration
- Automated API testing using Pytest

---

# Tech Stack

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## Database

- SQLite

## Authentication

- JWT Authentication
- OAuth2 Password Flow
- Passlib
- Bcrypt

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn

## Testing

- Pytest
- FastAPI TestClient

---

# Project Structure

```
Finance-Analytics-System

├── app
│   ├── main.py                  # FastAPI API routes
│   ├── models.py                # Request and response models
│   ├── database.py              # Database connection
│   ├── crud.py                  # Database CRUD operations
│   ├── analytics_service.py     # User based analytics logic
│   ├── users.py                 # Register and Login APIs
│   ├── auth.py                  # JWT token creation
│   ├── security.py              # Password hashing
│   ├── dependencies.py          # JWT authentication
│   ├── migrate.py               # Database migration
│   └── __init__.py
│
├── database
│   └── finance.db               # SQLite database
│
├── tests
│   └── test_api.py              # API test cases
│
├── requirements.txt
└── README.md
```

---

# Database Design

## Users Table

Stores user information.

```
user_id
name
email
password
```

---

## Transactions Table

Stores financial transactions.

```
transaction_id
user_id
amount
category
transaction_type
transaction_date
```

---

# Authentication API

## Register User

### POST

```
/register
```

Request:

```json
{
  "name": "Mantu Kumar",
  "email": "mantu@gmail.com",
  "password": "123456"
}
```

Response:

```json
{
  "message": "User registered successfully"
}
```

---

# Login API

### POST

```
/login
```

Request:

```json
{
  "email": "mantu@gmail.com",
  "password": "123456"
}
```

Response:

```json
{
  "access_token": "your_token",
  "token_type": "bearer"
}
```

Use this token in Swagger Authorize.

---

# API Endpoints

## Home API

### GET

```
/
```

Response:

```json
{
  "message": "Finance Analytics API Running"
}
```

---

# Transactions API

All transaction APIs require JWT authentication.

---

## Get Transactions

### GET

```
/transactions
```

Returns only logged-in user's transactions.

Example:

```json
[
  {
    "transaction_id": 1,
    "user_id": 1,
    "amount": 500,
    "category": "Food",
    "transaction_type": "Expense",
    "transaction_date": "2026-08-01"
  }
]
```

---

## Add Transaction

### POST

```
/transactions
```

Request:

```json
{
  "amount": 300,
  "category": "Shopping",
  "transaction_type": "Expense",
  "transaction_date": "2026-08-03"
}
```

Note:

`user_id` is automatically taken from JWT token.

Response:

```json
{
  "message": "Transaction added successfully"
}
```

---

## Delete Transaction

### DELETE

```
/transactions/{transaction_id}
```

Example:

```
/transactions/1
```

Response:

```json
{
  "message": "Transaction deleted successfully"
}
```

---

# Financial Analytics API

## Get Analytics

### GET

```
/analytics
```

Returns financial summary of logged-in user.

Example Response:

```json
{
  "total_income": 2000,
  "total_expense": 1300,
  "savings": 700
}
```

---

# Installation and Setup

## Clone Repository

```bash
git clone https://github.com/Mantu-231/Finance-Analytics-System.git
```

Move into project directory:

```bash
cd Finance-Analytics-System
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

OpenAPI:

```
http://127.0.0.1:8000/openapi.json
```

---

# Running Tests

Run:

```bash
pytest
```

Current tests:

- Home endpoint test
- Transactions endpoint test
- Analytics endpoint test

Example result:

```
3 passed
```

---

# Future Improvements

- Monthly financial reports
- Cloud database integration
- Docker deployment
- Frontend dashboard
- Machine learning based expense prediction

---

# Author

**Mantu Kumar**