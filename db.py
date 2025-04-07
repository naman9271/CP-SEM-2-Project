import sqlite3

def get_connection():
    return sqlite3.connect("database/blood.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        blood_group TEXT,
        contact TEXT
    )''')

    conn.commit()
    conn.close()
