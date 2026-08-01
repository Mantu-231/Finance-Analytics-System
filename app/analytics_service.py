import pandas as pd
from app.database import get_connection



def get_financial_report():

    conn = get_connection()

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