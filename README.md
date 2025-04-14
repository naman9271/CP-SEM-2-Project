# Blood Donation Management System

## Project Overview
The Blood Donation Management System is a web-based application built using Python (Flask framework) and SQLite.  
It helps manage donor records, blood group availability, and user authentication efficiently.

---

## Features

- **User Authentication**: Signup and Login functionality with secure password hashing.
- **Donor Management**:
  - Add Donor Details
  - View All Donors
  - Search Donor by Blood Group
  - Delete Donor
- **Responsive Design**: User-friendly interface with a professional look.
- **Flash Messages**: Informative messages for user actions with dismiss functionality.

---

## Technologies Used

- **Backend**: Python (Flask Framework)
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Password Security**: Passlib for password hashing

---

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/naman9271/CP-SEM-2-Project
cd CP-SEM-2-Project
```

### 2. Install Dependencies

Ensure you have Python installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

---

## Application Workflow

1. **Home Page**: Navigate to the home page to access the Signup or Login options.
2. **Signup**: Create a new account using a username and password.
3. **Login**: Log in to access the dashboard.
4. **Dashboard**:
   - View all donors.
   - Add new donor details.
   - Search for donors by blood group.
   - Delete donor records.
5. **Logout**: Securely log out of the application.

---

## Folder Structure

```
Blood-Donation-Management/
│
├── app.py                # Main application file
├── auth.py               # Handles user authentication
├── donor.py              # Donor operations (Add, View, Search, Delete)
├── db.py                 # Database connection and table creation
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── static/               # Static files (CSS, images)
│   ├── styles.css        # Custom styles
│   └── logo.png          # Application logo
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Home page
│   ├── login.html        # Login page
│   ├── signup.html       # Signup page
│   ├── dashboard.html    # Dashboard
│   ├── add_donor.html    # Add donor form
│   ├── search_donor.html # Search donor form
│   └── view_donor.html   # View donor profile
└── database/             # SQLite database folder
    └── blood.db          # SQLite database file
```

---

## Developed By

- **Naman Jain**  
  *2024UIC3579*

- **Anvay Khrab**  
  *2024UIC3580*

- **Daksh Pathak**  
  *2024UIC3539*

> **CP-SEM-2 (Python + SQL)**  
> *Blood Donation Management System*
