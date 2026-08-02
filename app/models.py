from pydantic import BaseModel


# POST ke liye request model
# user_id token se aayega, isliye yahan nahi hoga
class TransactionCreate(BaseModel):

    amount: float
    category: str
    transaction_type: str
    transaction_date: str



# Response model
class Transaction(BaseModel):

    transaction_id: int
    user_id: int
    amount: float
    category: str
    transaction_type: str
    transaction_date: str