import sqlite3
from faker import Faker


def create_and_populate_db(db_name, num_records):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')

    fake = Faker()

    users = [(fake.name(), fake.random_int(min=1, max=80)) for _ in range(num_records)]

    cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users)

    conn.commit()
    conn.close()

