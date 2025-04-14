from db import get_connection

def add_donor(name, age, blood_group, contact):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donors (name, age, blood_group, contact) VALUES (?, ?, ?, ?)", (name, age, blood_group, contact))
    conn.commit()
    conn.close()

def get_donors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()
    conn.close()
    return donors

def search_donors(blood_group):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors WHERE blood_group = ?", (blood_group,))
    donors = cursor.fetchall()
    conn.close()
    return donors

def delete_donor(donor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM donors WHERE id = ?", (donor_id,))
    conn.commit()
    conn.close()
