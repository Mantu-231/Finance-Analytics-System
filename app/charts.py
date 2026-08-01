import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


DATABASE_NAME = "database/finance.db"


def load_data():

    conn = sqlite3.connect(DATABASE_NAME)

    query = """
    SELECT category, amount, transaction_type
    FROM transactions
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df



def expense_chart():

    df = load_data()

    expenses = df[df["transaction_type"] == "Expense"]

    category_data = expenses.groupby("category")["amount"].sum()


    plt.figure(figsize=(7,5))

    category_data.plot(
        kind="bar",
        color="skyblue"
    )

    plt.title("Category Wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("charts/expense_chart.png")

    plt.close()



def income_expense_chart():

    df = load_data()

    summary = df.groupby("transaction_type")["amount"].sum()


    plt.figure(figsize=(6,5))

    summary.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Income vs Expense")

    plt.ylabel("")

    plt.savefig("charts/income_expense.png")

    plt.close()



if __name__ == "__main__":

    expense_chart()

    income_expense_chart()