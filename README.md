# Blood Donation Management System

## Project Overview
This is a simple Blood Donation Management System built using Python and SQLite as the database.  
This project helps to manage login/signup, donor records, and blood group availability.

---

## Features

- User Authentication (Login & Signup)
- Add Donor Details
- View All Donors
- Search Donor by Blood Group
- Delete Donor
- Exit Safely

---

## Project Architecture
```
BDMS/ 
│ 
├── main.py # Entry Point of Application 
├── auth.py # Handles Login & Signup 
├── db.py # Handles Database & Tables 
├── donor.py # Donor Operations (Add, View, Search, Delete) 
├── .gitignore # Files/Folders to Ignore in Git 
├── requirements.txt # Python Libraries to Install 
├── README.md # Project Documentation │
├── database/ # Folder to Store SQLite Database File 
│ └── blood_donation.db 
├── venv/ # Python Virtual Environment (Optional)
```

---

## Technologies Used

- Python
- SQLite (Python built-in library)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/naman9271/CP-SEM-2-Project
cd CP-SEM-2-Project
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**For Windows**
```bash
venv\Scripts\activate
```
**For Mac/Linux**
```bash
source venv/bin/activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

### 5. Run the Project

```bash
python main.py
```

---

> ### Developed By  
> **Naman Jain**  
> *2024UIC3579* 

> **Anvay Khrab**  
> *2024UIC3580*

> **Daksh Pathak**  
> *2024UIC3539*

> **CP-SEM-2 (Python + SQL)**  
> *Blood Donation Management System*
