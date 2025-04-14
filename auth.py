from passlib.hash import sha256_crypt
from db import get_connection

def signup_user(username, password):
    hashed_pass = sha256_crypt.hash(password)
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pass))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and sha256_crypt.verify(password, result[0]):
        return True
    return False
