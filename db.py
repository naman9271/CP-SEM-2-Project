import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.getenv("DB_NAME")

def get_connection():
    return sqlite3.connect(f"database/{DB_NAME}")

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
