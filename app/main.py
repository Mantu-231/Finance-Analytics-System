from fastapi import FastAPI
from typing import List

from app.models import Transaction, TransactionCreate
from app.crud import (
    get_all_transactions,
    add_transaction,
    remove_transaction
)
from app.analytics_service import get_financial_report


app = FastAPI(
    title="Finance Analytics API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Finance Analytics API Running"
    }



# GET all transactions
@app.get("/transactions", response_model=List[Transaction])
def get_transactions():

    return get_all_transactions()



# POST new transaction
@app.post("/transactions")
def create_transaction(transaction: TransactionCreate):

    add_transaction(transaction)

    return {
        "message": "Transaction added successfully"
    }



# DELETE transaction
@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):

    remove_transaction(transaction_id)

    return {
        "message": "Transaction deleted successfully"
    }



# Analytics API
@app.get("/analytics")
def get_analytics():

    return get_financial_report()