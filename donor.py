from db import get_connection

def add_donor():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    blood_group = input("Enter blood group: ")
    contact = input("Enter contact number: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donors (name, age, blood_group, contact) VALUES (?,?,?,?)", (name, age, blood_group, contact))
    conn.commit()
    conn.close()
    print("Donor added successfully!")

def view_donors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()
    conn.close()

    print("\n--- Donors List ---")
    for donor in donors:
        print(donor)

def search_donor():
    blood_group = input("Enter blood group to search: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors WHERE blood_group=?", (blood_group,))
    donors = cursor.fetchall()
    conn.close()

    print("\n--- Matching Donors ---")
    for donor in donors:
        print(donor)

def delete_donor():
    donor_id = int(input("Enter donor ID to delete: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM donors WHERE id=?", (donor_id,))
    conn.commit()
    conn.close()
    print("Donor deleted successfully!")
