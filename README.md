# Finance Analytics System

A Python-based financial management and analytics system that tracks income and expenses, provides REST APIs, performs financial analysis, and generates visualization reports.

Built with **FastAPI**, **SQLite**, **Pandas**, **Matplotlib**, and **Streamlit**, with JWT-based user authentication.

## Features

- User registration & login
- JWT authentication
- Protected REST APIs
- Add / view / delete financial transactions
- Calculate total income, total expenses, and savings
- Category-wise expense analysis
- Financial chart generation
- Interactive Streamlit dashboard
- SQLite database integration
- Automated API testing with Pytest

## Tech Stack

| Category | Tools |
|---|---|
| Backend | Python, FastAPI, Pydantic, Uvicorn |
| Database | SQLite |
| Authentication | JWT, OAuth2 Password Flow, Passlib, Bcrypt |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Streamlit |
| Testing | Pytest, FastAPI TestClient |

## Project Structure

```
Finance-Analytics-System
├── app
│   ├── main.py               # FastAPI API routes
│   ├── models.py              # Request and response models
│   ├── database.py            # Database connection
│   ├── crud.py                 # Database CRUD operations
│   ├── analytics_service.py   # User-based analytics logic
│   ├── users.py                # Register and login APIs
│   ├── auth.py                 # JWT token creation
│   ├── security.py             # Password hashing
│   ├── dependencies.py         # JWT authentication
│   ├── migrate.py              # Database migration
│   └── __init__.py
│
├── dashboard
│   └── app.py                  # Streamlit dashboard
│
├── database
│   └── finance.db              # SQLite database
│
├── screenshots
│   ├── login.png
│   ├── dashboard.png
│   ├── expense.png
│   └── add_transaction.png
│
├── tests
│   └── test_api.py             # API test cases
│
├── requirements.txt
└── README.md
```

## Database Design

**Users**

| Field | Description |
|---|---|
| `user_id` | Primary key |
| `name` | User's name |
| `email` | User's email |
| `password` | Hashed password |

**Transactions**

| Field | Description |
|---|---|
| `transaction_id` | Primary key |
| `user_id` | Foreign key to Users |
| `amount` | Transaction amount |
| `category` | Expense/income category |
| `transaction_type` | `"Income"` or `"Expense"` |
| `transaction_date` | Date of transaction |

## Installation & Setup

```bash
git clone https://github.com/Mantu-231/Finance-Analytics-System.git
cd Finance-Analytics-System
```

Create and activate a virtual environment (Windows):

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

- API: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI schema: `http://127.0.0.1:8000/openapi.json`

## Authentication

### Register — `POST /register`

```json
{
  "name": "Mantu Kumar",
  "email": "mantu@gmail.com",
  "password": "123456"
}
```

### Login — `POST /login`

```json
{
  "username": "mantu@gmail.com",
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

Use this token to authorize requests in Swagger UI.

## API Endpoints

### Home

`GET /` → `{ "message": "Finance Analytics API Running" }`

### Transactions
*(all require JWT authentication)*

| Method | Endpoint | Description |
|---|---|---|
| GET | `/transactions` | Get the logged-in user's transactions |
| POST | `/transactions` | Add a transaction (`user_id` taken from JWT) |
| DELETE | `/transactions/{transaction_id}` | Delete a transaction |

**Add transaction — request body:**

```json
{
  "amount": 300,
  "category": "Shopping",
  "transaction_type": "Expense",
  "transaction_date": "2026-08-03"
}
```

### Analytics

`GET /analytics` — returns the logged-in user's financial summary:

```json
{
  "total_income": 2000,
  "total_expense": 1300,
  "savings": 700
}
```

## Streamlit Dashboard

An interactive dashboard connects to the FastAPI backend for managing and visualizing financial data.

**Features:** JWT login, income/expense/savings overview, transaction management, category-wise expense charts, real-time data.

**Run it:**

```bash
pip install streamlit plotly requests
uvicorn app.main:app --reload        # terminal 1
streamlit run dashboard/app.py       # terminal 2
```

Dashboard: `http://localhost:8501`

## Analytics & Visualization

- **Category-wise expense chart** — e.g. Food, Travel, Shopping breakdown
- **Income vs. expense chart** — total income compared to total expenses

Generated charts are saved to `charts/expense_chart.png` and `charts/income_expense.png`.

## Running Tests

```bash
pytest
```

Covers the home, transactions, and analytics endpoints (`3 passed`).

## Future Improvements

- Monthly financial reports
- Cloud database integration
- Docker deployment
- Advanced dashboard improvements
- ML-based expense prediction
- Cloud hosting deployment

## Screenshots

| Login | Dashboard |
|---|---|
| ![Login](screenshots/login.png) | ![Dashboard](screenshots/dashboard.png) |

| Expense Analysis | Add Transaction |
|---|---|
| ![Expense Analysis](screenshots/expense.png) | ![Add Transaction](screenshots/add_transaction.png) |

## Author

**Mantu Kumar**
