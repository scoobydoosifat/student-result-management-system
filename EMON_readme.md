# Student Result Management System (SRMS)
### Python | Tkinter | SQLite3

> A desktop-based academic management application built with Python and Tkinter, using SQLite3 for local data storage.

---

## 👤 Contributor

**Name:** Nahid Hasan Emon  

**Email:** 2023200000153@seu.edu.bd

**Branch:** `emon`

**Module Contribution:** Course Enrollment Module & Database Schema Update

---

## ✅ My Contributions

### 1. `enrollment.py` — Course Enrollment Module *(New File)*

A fully functional Tkinter window class (`EnrollmentClass`) that manages student course enrollments.

**Features:**
- Select a student by roll number — name and course are **auto-filled** from the database
- Enroll a student into any available course with an enrollment date
- **Prevents duplicate** active enrollments in the same course
- Update enrollment date or status for an existing record
- **Drop** a student from a course (sets status to `Dropped`)
- Search enrollments by roll number
- Scrollable data table showing all enrollment records (ID, Roll No., Name, Course, Date, Status)
- Status options: `Active`, `Completed`, `Dropped`

**Key Methods:**

| Method | Description |
|---|---|
| `_fetch_rolls()` | Loads all student roll numbers from the `student` table |
| `_fetch_courses()` | Loads all course names from the `course` table |
| `_on_roll_select()` | Auto-fills student name and course when a roll is selected |
| `_get_row()` | Populates input fields when a table row is clicked |
| `_show_all()` | Refreshes the treeview with all enrollment records |
| `enroll()` | Inserts a new enrollment record after duplicate check |
| `update()` | Updates date and status of an existing enrollment |
| `drop()` | Sets enrollment status to `Dropped` |
| `search()` | Filters table by roll number |
| `clear()` | Resets all input fields and refreshes the table |

---

### 2. `create_db.py` — Database Schema 

Created all the table to the database.The created tables are named below.

**All Tables in `rms.db`:**

| Table | Purpose |
|---|---|
| `course` | Stores course details |
| `student` | Stores student profiles |
| `result` | Stores exam marks and percentage |
| `employee` | Stores login credentials |
| `enrollment` | Tracks student-course enrollments |

---

## 🔗 How the Enrollment Module Connects to the System

- **Reads from** `student` table → to populate the roll number dropdown
- **Reads from** `course` table → to populate the course dropdown
- **Writes to** `enrollment` table → to save, update, or drop enrollments
- **Integrated into** `python_project.py` → accessible via the `Enrollment` button in the main menu dashboard
- The main dashboard counter **"Total Enrolled"** displays the live count of active enrollments

---

## ▶️ How to Run

```bash
# Step 1: Initialise the database (run once)
python create_db.py

# Step 2: Launch the application
python python_project.py
```

**Requirements:** Python 3.x (Tkinter and SQLite3 are included in the standard library — no extra installs needed)

---
