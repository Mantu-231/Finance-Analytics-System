markdown
# Finance Analytics System

A Python-based financial management and analytics system that tracks income and expenses, provides REST APIs, and generates financial insights using data analysis and visualization.

## Features

- Add financial transactions
- View all transactions
- Delete transactions
- Calculate income, expenses, and savings
- Category-wise expense analysis
- Generate financial charts
- REST API using FastAPI
- SQLite database integration

## Tech Stack

- Python
- FastAPI
- SQLite
- Pandas
- NumPy
- Matplotlib
- Seaborn
- REST APIs

## Project Structure

Finance-Analytics-System

├── app
│   ├── main.py
│   ├── analytics.py
│   ├── charts.py
│   └── view_data.py
│
├── database
│   └── finance.db
│
├── charts
│   ├── expense_chart.png
│   └── income_expense.png
│
├── requirements.txt
└── README.md


## API Endpoints

### Get Transactions


GET /transactions


Returns all user transactions.


### Add Transaction


POST /transactions


Example:

json
{
  "user_id":1,
  "amount":300,
  "category":"Shopping",
  "transaction_type":"Expense",
  "transaction_date":"2026-08-03"
}



### Delete Transaction

DELETE /transactions/{id}


### Financial Analytics

GET /analytics

Example Response:

json
{
 "total_income":2000,
 "total_expense":1300,
 "savings":700
}

## Running the Project

Install dependencies:

pip install -r requirements.txt

Run API server:

uvicorn app.main:app --reload


Open Swagger documentation:

http://127.0.0.1:8000/docs


## Analytics Visualization

Generated reports:

* Category Wise Expenses
* Income vs Expense Analysis


## Author

Mantu Kumar
