import pandas as pd

from app.database import get_connection



def get_financial_report(user_id):

    conn = get_connection()


    query = """
    SELECT amount, transaction_type
    FROM transactions
    WHERE user_id = ?
    """


    df = pd.read_sql_query(
        query,
        conn,
        params=(user_id,)
    )


    conn.close()


    if df.empty:

        return {
            "total_income": 0,
            "total_expense": 0,
            "savings": 0
        }



    total_income = df[
        df["transaction_type"] == "Income"
    ]["amount"].sum()



    total_expense = df[
        df["transaction_type"] == "Expense"
    ]["amount"].sum()



    savings = total_income - total_expense



    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "savings": float(savings)
    }