from app.database import get_connection


def get_all_transactions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM transactions
    """)

    rows = cursor.fetchall()

    conn.close()

    transactions = []

    for row in rows:
        transactions.append({
            "transaction_id": row[0],
            "user_id": row[1],
            "amount": row[2],
            "category": row[3],
            "transaction_type": row[4],
            "transaction_date": row[5]
        })

    return transactions



def add_transaction(transaction):

    conn = get_connection()
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



def remove_transaction(transaction_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM transactions
    WHERE transaction_id = ?
    """,
    (transaction_id,))

    conn.commit()
    conn.close()