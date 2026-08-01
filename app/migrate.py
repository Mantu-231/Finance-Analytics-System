import sqlite3


DATABASE_NAME = "database/finance.db"


conn = sqlite3.connect(DATABASE_NAME)

cursor = conn.cursor()


try:

    cursor.execute("""
    ALTER TABLE users
    ADD COLUMN password TEXT
    """)

    print("Password column added successfully")


except Exception as e:

    print("Migration error:", e)



conn.commit()

conn.close()