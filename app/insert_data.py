import sqlite3

DATABASE_NAME = "database/finance.db"


def insert_user():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (name, email)
    VALUES (?, ?)
    """, ("Mantu Kumar", "mantu@gmail.com"))

    conn.commit()
    conn.close()

    print("User added successfully!")


def insert_transaction():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    transactions = [
        (1, 500, "Food", "Expense", "2026-08-01"),
        (1, 2000, "Salary", "Income", "2026-08-01"),
        (1, 800, "Travel", "Expense", "2026-08-02")
    ]

    cursor.executemany("""
    INSERT INTO transactions
    (user_id, amount, category, transaction_type, transaction_date)
    VALUES (?, ?, ?, ?, ?)
    """, transactions)

    conn.commit()
    conn.close()

    print("Transactions added successfully!")


if __name__ == "__main__":
    insert_user()
    insert_transaction()