# Finance Analytics System

A Python-based financial management and analytics system that tracks income and expenses, provides REST APIs, performs financial analysis, and generates visualization reports.

The project is built using **FastAPI**, **SQLite**, **Pandas**, and **Matplotlib** with a clean backend architecture.

---

# Features

- Add financial transactions
- View all transactions
- Delete transactions
- Calculate total income
- Calculate total expenses
- Calculate savings
- Category-wise expense analysis
- Generate financial charts
- REST API using FastAPI
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


Finance-Analytics-System

```
├── app
│   ├── main.py                  # FastAPI API routes
│   ├── models.py                # Request and response models
│   ├── database.py              # Database connection
│   ├── crud.py                  # Database CRUD operations
│   ├── analytics_service.py     # Analytics logic for API
│   ├── analytics.py             # Standalone financial analysis
│   ├── charts.py                # Data visualization charts
│   ├── insert_data.py           # Insert sample data
│   ├── view_data.py             # View database records
│   └── __init__.py
│
├── database
│   └── finance.db               # SQLite database
│
├── charts
│   ├── expense_chart.png
│   └── income_expense.png
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

Example:

```
user_id
name
email
```

## Transactions Table

Stores financial transactions.

Example:

```
transaction_id
user_id
amount
category
transaction_type
transaction_date
```

---

# API Endpoints

## Home

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

## Get All Transactions

### GET

```
/transactions
```

Returns all financial transactions.


---

## Add Transaction

### POST

```
/transactions
```

Request:

```json
{
  "user_id": 1,
  "amount": 300,
  "category": "Shopping",
  "transaction_type": "Expense",
  "transaction_date": "2026-08-03"
}
```

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

## GET

```
/analytics
```

Example Response:

```json
{
  "total_income": 2000,
  "total_expense": 1300,
  "savings": 700
}
```

---

# Analytics and Visualization

The system generates:

## Category Wise Expense Chart

Shows expenses based on categories.

Example:

```
Food      500
Travel    800
```

## Income vs Expense Chart

Shows comparison between income and expenses.

Generated files:

```
charts/
│
├── expense_chart.png
└── income_expense.png
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

## Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server will run:

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

Run automated tests:

```bash
pytest
```

Current tests include:

- Home endpoint test
- Transactions endpoint test
- Analytics endpoint test

Example result:

```
3 passed
```

---

# Sample Analytics Output

```
Total Income: 2000

Total Expense: 1300

Savings: 700
```

---

# Future Improvements

- User authentication system
- JWT based login
- Monthly financial reports
- Cloud database integration
- Docker deployment
- Frontend dashboard
- Machine learning based expense prediction

---

# Author

**Mantu Kumar**
