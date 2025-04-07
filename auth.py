from passlib.hash import sha256_crypt
from db import get_connection

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_pass = sha256_crypt.hash(password)

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, hashed_pass))
        conn.commit()
        print("Signup successful!")
    except:
        print("Username already exists!")
    finally:
        conn.close()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and sha256_crypt.verify(password, result[0]):
        print("Login Successful!")
        return True
    else:
        print("Invalid Credentials")
        return False
