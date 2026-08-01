import sqlite3


DATABASE_NAME = "database/finance.db"


def get_connection():

    conn = sqlite3.connect(DATABASE_NAME)

    return conn