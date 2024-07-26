import sqlite3

from test2.create_db import create_and_populate_db


def parse_db():
    conn = sqlite3.connect('users.db')

    cursor = conn.cursor()

    users = cursor.execute("""
    SELECT name, age FROM users WHERE age > 30
    """)

    return users


if __name__ == '__main__':
    create_and_populate_db('users.db', 100)

    users = parse_db()

    for user in users:

        print(f"{user[0]}: {user[1]}")
