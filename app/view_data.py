import sqlite3

DATABASE_NAME = "database/finance.db"


def view_users():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    print("\n--- USERS ---")
    for user in users:
        print(user)

    conn.close()


def view_transactions():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        transactions.transaction_id,
        users.name,
        transactions.amount,
        transactions.category,
        transactions.transaction_type,
        transactions.transaction_date
    FROM transactions
    JOIN users
    ON transactions.user_id = users.user_id
    """)

    transactions = cursor.fetchall()

    print("\n--- TRANSACTIONS ---")

    for transaction in transactions:
        print(transaction)

    conn.close()


if __name__ == "__main__":
    view_users()
    view_transactions()