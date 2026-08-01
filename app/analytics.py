import sqlite3
import pandas as pd


DATABASE_NAME = "database/finance.db"


def load_transactions():

    conn = sqlite3.connect(DATABASE_NAME)

    query = """
    SELECT 
        category,
        amount,
        transaction_type,
        transaction_date
    FROM transactions
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def generate_report():

    df = load_transactions()

    print("\n--- TRANSACTION DATA ---")
    print(df)


    total_income = df[df["transaction_type"] == "Income"]["amount"].sum()

    total_expense = df[df["transaction_type"] == "Expense"]["amount"].sum()

    savings = total_income - total_expense


    print("\n--- FINANCIAL REPORT ---")
    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Savings:", savings)


    print("\n--- CATEGORY WISE EXPENSE ---")

    expense_data = df[df["transaction_type"] == "Expense"]

    category_expense = expense_data.groupby("category")["amount"].sum()

    print(category_expense)



if __name__ == "__main__":
    generate_report()