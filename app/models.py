from pydantic import BaseModel


class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    category: str
    transaction_type: str
    transaction_date: str


class Transaction(BaseModel):
    transaction_id: int
    user_id: int
    amount: float
    category: str
    transaction_type: str
    transaction_date: str