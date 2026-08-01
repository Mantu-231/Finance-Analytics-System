from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import sqlite3
import pandas as pd


app = FastAPI(
    title="Finance Analytics API",
    version="1.0"
)


DATABASE_NAME = "database/finance.db"


# Response Model
class Transaction(BaseModel):
    transaction_id: int
    user_id: int
    amount: float
    category: str
    transaction_type: str
    transaction_date: str


# Request Model (POST ke liye)
class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    category: str
    transaction_type: str
    transaction_date: str



@app.get("/")
def home():
    return {
        "message": "Finance Analytics API Running"
    }



# GET all transactions
@app.get("/transactions", response_model=List[Transaction])
def get_transactions():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM transactions
    """)

    rows = cursor.fetchall()

    conn.close()


    transactions = []

    for row in rows:

        transactions.append(
            {
                "transaction_id": row[0],
                "user_id": row[1],
                "amount": row[2],
                "category": row[3],
                "transaction_type": row[4],
                "transaction_date": row[5]
            }
        )


    return transactions



# POST new transaction
@app.post("/transactions")
def create_transaction(transaction: TransactionCreate):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO transactions
    (user_id, amount, category, transaction_type, transaction_date)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        transaction.user_id,
        transaction.amount,
        transaction.category,
        transaction.transaction_type,
        transaction.transaction_date
    ))


    conn.commit()

    conn.close()


    return {
        "message": "Transaction added successfully"
    }



@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM transactions
    WHERE transaction_id = ?
    """, (transaction_id,))


    conn.commit()

    conn.close()


    return {
        "message": "Transaction deleted successfully"
    }


@app.get("/analytics")
def get_analytics():

    conn = sqlite3.connect(DATABASE_NAME)

    query = """
    SELECT amount, transaction_type
    FROM transactions
    """

    df = pd.read_sql_query(query, conn)

    conn.close()


    total_income = df[
        df["transaction_type"] == "Income"
    ]["amount"].sum()


    total_expense = df[
        df["transaction_type"] == "Expense"
    ]["amount"].sum()


    savings = total_income - total_expense


    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "savings": savings
    }