import sqlite3

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()

    # Course table
    cur.execute("""CREATE TABLE IF NOT EXISTS course(
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        duration text,
        charges text,
        description text
    )""")
    con.commit()

    # Student table
    cur.execute("""CREATE TABLE IF NOT EXISTS student(
        roll INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        email text,
        gender text,
        dob text,
        contact text,
        admission text,
        course text,
        state text,
        city text,
        pin text,
        address text
    )""")
    con.commit()

    # Result table
    cur.execute("""CREATE TABLE IF NOT EXISTS result(
        rid INTEGER PRIMARY KEY AUTOINCREMENT,
        roll text,
        name text,
        course text,
        marks_ob text,
        full_marks text,
        per text
    )""")
    con.commit()

    # Login table
    cur.execute("""CREATE TABLE IF NOT EXISTS employee(
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        f_name text,
        l_name text,
        contact text,
        email text,
        question text,
        answer text,
        password text
    )""")
    con.commit()

    # Enrollment table
    cur.execute("""CREATE TABLE IF NOT EXISTS enrollment(
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        roll text,
        student_name text,
        course text,
        enroll_date text,
        status text DEFAULT 'Active'
    )""")
    con.commit()

    con.close()

create_db()