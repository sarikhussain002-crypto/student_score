import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    email TEXT,
    password TEXT
)
""")

conn.commit()


def add_user(name, email, password):

    cursor.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        (name, email, password)
    )

    conn.commit()


def login_user(email, password):

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    data = cursor.fetchone()

    return data