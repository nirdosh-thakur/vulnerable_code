import sqlite3
from sqlite3 import Error

def create_db():
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def add_user(name, age):
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def get_user_by_id(user_id):
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        query = "SELECT * FROM users WHERE id = ?"
        c.execute(query, (user_id,))
        user = c.fetchone()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        return user