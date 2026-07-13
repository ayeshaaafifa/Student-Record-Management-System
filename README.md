# Student Record Management System

A simple menu-driven Python program to manage student records using core data structures (list of dictionaries) — no external database required.

## Features

- ➕ Add new student records
- 📋 Display all student records
- ✏️ Update an existing student's details (search by Student ID)
- 🗑️ Delete a student's record (search by Student ID)
- 🔁 Continuous menu loop until the user chooses to exit

## How It Works

Each student is stored as a dictionary with the following fields:

- `Student ID`
- `Name`
- `Age`
- `Grade`

All student dictionaries are stored together in a single list (`records`), which acts as an in-memory database for the session.

## Menu Options
===== Student Record Menu =====

Add New Record
Display All Records
Update Record
Delete Record
Exit
## Requirements

- Python 3.x
- No external libraries needed

## How to Run

```bash
python student_record_system.py
```
## Project Structure
Student-Record-Management-System/
│
├── student_record_system.py   # Main program file
└── README.md                  # Project documentation
## Future Improvements

- Save/load records to a file (CSV or JSON) so data persists between runs
- Input validation (e.g., ensure age is numeric)
- Search records by name in addition to Student ID
- Export records to a report (PDF/Excel)

## Author

**Ayesha Afifa** — [GitHub: Afifa375](https://github.com/Afifa375)
