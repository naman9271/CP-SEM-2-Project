from auth import signup, login
from donor import add_donor, view_donors, search_donor, delete_donor
from db import create_tables

def print_welcome():
    print("===============================================")
    print("   Welcome to the Blood Donation Management System")
    print("===============================================")
    print()

def print_footer():
    print("\n-----------------------------------------------")
    print("     Thank you for using our System!")
    print("         Stay Healthy, Stay Safe!")
    print("-----------------------------------------------\n")

def main():
    create_tables()
    print_welcome()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            signup()
        elif choice == '2':
            if login():
                while True:
                    print("\n--- Donor Management ---")
                    print("1. Add Donor")
                    print("2. View Donors")
                    print("3. Search Donor by Blood Group")
                    print("4. Delete Donor")
                    print("5. Logout")
                    
                    user_choice = input("Enter choice: ")
                    
                    if user_choice == '1':
                        add_donor()
                    elif user_choice == '2':
                        view_donors()
                    elif user_choice == '3':
                        search_donor()
                    elif user_choice == '4':
                        delete_donor()
                    elif user_choice == '5':
                        break
                    else:
                        print("Invalid choice!")
        elif choice == '3':
            print_footer()
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()