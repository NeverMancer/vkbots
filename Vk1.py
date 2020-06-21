import sqlite3
from uuid import uuid4

def create_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE users
            (id text, name text, surname text, status text)
        """)

def add_user(name, surname, status):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users VALUES ( '{0}', '{1}', '{2}', '{3}' )".format('1', name, surname, status))
    conn.commit()

def show_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    print(cursor.execute("SELECT name FROM users WHERE name='Tom'").fetchall())

show_table()