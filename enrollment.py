from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from datetime import date


class EnrollmentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x500+80+150")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title 
        Label(
            self.root,
            text="Manage Course Enrollments",
            font=("goudy old style", 18, "bold"),
            bg="#033054",
            fg="white"
        ).place(x=10, y=15, width=1180, height=35)

        # Variables 
        self.var_roll        = StringVar()
        self.var_name        = StringVar()
        self.var_course      = StringVar()
        self.var_enroll_date = StringVar()
        self.var_status      = StringVar()
        self.var_search      = StringVar()

        # Pre-fill today's date
        self.var_enroll_date.set(str(date.today()))

        # Left-panel labels 
        for txt, y in [("Roll No.", 65), ("Student Name", 105),
                       ("Course", 145), ("Enroll Date", 185), ("Status", 225)]:
            Label(self.root, text=txt,
                  font=("goudy old style", 14, "bold"), bg="white"
                  ).place(x=10, y=y)

        # Roll No. combo (populated from student table)
        self.roll_list = []
        self._fetch_rolls()

        self.cmb_roll = ttk.Combobox(
            self.root, textvariable=self.var_roll,
            values=self.roll_list,
            font=("goudy old style", 13, "bold"),
            state="readonly", justify=CENTER
        )
        self.cmb_roll.place(x=160, y=65, width=200)
        self.cmb_roll.set("Select")

        # Auto-fill student name & current course when roll is chosen
        self.cmb_roll.bind("<<ComboboxSelected>>", self._on_roll_select)

        # Search-and-fill button
        Button(
            self.root, text="Fetch",
            font=("goudy old style", 12, "bold"),
            bg="#03a9f4", fg="white", cursor="hand2",
            command=self._on_roll_select
        ).place(x=370, y=65, width=80, height=28)

        # Student Name (readonly – auto-filled)
        Entry(
            self.root, textvariable=self.var_name,
            font=("goudy old style", 13, "bold"),
            bg="lightyellow", state="readonly"
        ).place(x=160, y=105, width=290)

        # Course combo (all courses from DB)
        self.course_list = []
        self._fetch_courses()

        self.cmb_course = ttk.Combobox(
            self.root, textvariable=self.var_course,
            values=self.course_list,
            font=("goudy old style", 13, "bold"),
            state="readonly", justify=CENTER
        )
        self.cmb_course.place(x=160, y=145, width=290)
        self.cmb_course.set("Select")

        # Enrollment date
        Entry(
            self.root, textvariable=self.var_enroll_date,
            font=("goudy old style", 13, "bold"),
            bg="lightyellow"
        ).place(x=160, y=185, width=290)

        # Status combo
        self.cmb_status = ttk.Combobox(
            self.root, textvariable=self.var_status,
            values=("Active", "Completed", "Dropped"),
            font=("goudy old style", 13, "bold"),
            state="readonly", justify=CENTER
        )
        self.cmb_status.place(x=160, y=225, width=290)
        self.cmb_status.current(0)

        # Action buttons 
        btn_cfg = [
            ("Enroll",  "#2196f3", self.enroll,   150),
            ("Update",  "#4caf50", self.update,   270),
            ("Drop",    "#f44336", self.drop,     390),
            ("Clear",   "#607d8b", self.clear,    510),
        ]
        for txt, color, cmd, x in btn_cfg:
            Button(
                self.root, text=txt,
                font=("goudy old style", 14, "bold"),
                bg=color, fg="white", cursor="hand2", command=cmd
            ).place(x=x, y=300, width=110, height=40)

        Label(self.root, text="Search Roll No.",
              font=("goudy old style", 14, "bold"), bg="white"
              ).place(x=720, y=65)

        Entry(self.root, textvariable=self.var_search,
              font=("goudy old style", 13, "bold"), bg="lightyellow"
              ).place(x=880, y=65, width=160)

        Button(self.root, text="Search",
               font=("goudy old style", 13, "bold"),
               bg="#03a9f4", fg="white", cursor="hand2",
               command=self.search
               ).place(x=1050, y=65, width=110, height=28)

        # view 
        frame = Frame(self.root, bd=2, relief=RIDGE)
        frame.place(x=720, y=105, width=460, height=350)

        scrolly = Scrollbar(frame, orient=VERTICAL)
        scrollx = Scrollbar(frame, orient=HORIZONTAL)

        cols = ("eid", "roll", "name", "course", "date", "status")
        self.table = ttk.Treeview(
            frame, columns=cols,
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT,  fill=Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)

        headers = ("ID", "Roll No.", "Student Name", "Course", "Enroll Date", "Status")
        widths  = (40,   70,         130,             110,      90,            80)
        for col, hdr, w in zip(cols, headers, widths):
            self.table.heading(col, text=hdr)
            self.table.column(col, width=w)

        self.table["show"] = "headings"
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind("<ButtonRelease-1>", self._get_row)

        self._show_all()


    def _fetch_rolls(self):
        """Load all student roll numbers into the combo list."""
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            self.roll_list = [str(r[0]) for r in rows]
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching rolls: {ex}")

    def _fetch_courses(self):
        """Load all course names into the combo list."""
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT name FROM course")
            rows = cur.fetchall()
            self.course_list = [r[0] for r in rows]
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching courses: {ex}")

    def _on_roll_select(self, event=None):
        """Auto-fill student name when a roll is selected."""
        roll = self.var_roll.get()
        if roll in ("", "Select"):
            return
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT name, course FROM student WHERE roll=?", (roll,))
            row = cur.fetchone()
            con.close()
            if row:
                self.var_name.set(row[0])
                # Pre-select the student's current course if available
                if row[1] in self.course_list:
                    self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "Student not found.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {ex}")

    def _get_row(self, event=None):
        """Populate left-panel fields when a table row is clicked."""
        r = self.table.focus()
        content = self.table.item(r)
        row = content.get("values", [])
        if not row:
            return
        # row = (eid, roll, name, course, date, status)
        self.var_roll.set(str(row[1]))
        self.var_name.set(row[2])
        self.var_course.set(row[3])
        self.var_enroll_date.set(row[4])
        self.var_status.set(row[5])

    def _show_all(self):
        """Refresh the treeview with all enrollment records."""
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM enrollment")
            rows = cur.fetchall()
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert("", END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error loading data: {ex}")


    def enroll(self):
        """Insert a new enrollment record."""
        roll   = self.var_roll.get()
        name   = self.var_name.get()
        course = self.var_course.get()
        edate  = self.var_enroll_date.get()
        status = self.var_status.get()

        if roll in ("", "Select") or course in ("", "Select") or name == "":
            messagebox.showerror("Error",
                "Please select a student and course before enrolling.",
                parent=self.root)
            return

        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            # Prevent duplicate active enrollment in the same course
            cur.execute(
                "SELECT * FROM enrollment WHERE roll=? AND course=? AND status='Active'",
                (roll, course)
            )
            if cur.fetchone():
                messagebox.showerror("Error",
                    "Student is already actively enrolled in this course.",
                    parent=self.root)
                con.close()
                return

            cur.execute(
                "INSERT INTO enrollment (roll, student_name, course, enroll_date, status) "
                "VALUES (?,?,?,?,?)",
                (roll, name, course, edate, status)
            )
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Student enrolled successfully!", parent=self.root)
            self._show_all()
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Enrollment failed: {ex}")

    def update(self):
        """Update an existing enrollment's course, date, or status."""
        roll   = self.var_roll.get()
        course = self.var_course.get()
        edate  = self.var_enroll_date.get()
        status = self.var_status.get()

        if roll in ("", "Select"):
            messagebox.showerror("Error", "Please select a student first.", parent=self.root)
            return

        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM enrollment WHERE roll=? AND course=?", (roll, course)
            )
            if not cur.fetchone():
                messagebox.showerror("Error",
                    "No enrollment record found for this student-course pair.\n"
                    "Please select a row from the table first.",
                    parent=self.root)
                con.close()
                return

            cur.execute(
                "UPDATE enrollment SET enroll_date=?, status=? WHERE roll=? AND course=?",
                (edate, status, roll, course)
            )
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Enrollment updated successfully!", parent=self.root)
            self._show_all()
        except Exception as ex:
            messagebox.showerror("Error", f"Update failed: {ex}")

    def drop(self):
        """Mark enrollment status as 'Dropped'."""
        roll   = self.var_roll.get()
        course = self.var_course.get()

        if roll in ("", "Select") or course in ("", "Select"):
            messagebox.showerror("Error",
                "Please select an enrollment record first.", parent=self.root)
            return

        op = messagebox.askyesno(
            "Confirm", f"Drop student {self.var_name.get()} from {course}?",
            parent=self.root
        )
        if op:
            try:
                con = sqlite3.connect("rms.db")
                cur = con.cursor()
                cur.execute(
                    "UPDATE enrollment SET status='Dropped' WHERE roll=? AND course=?",
                    (roll, course)
                )
                con.commit()
                con.close()
                messagebox.showinfo("Dropped",
                    "Enrollment status set to Dropped.", parent=self.root)
                self._show_all()
                self.clear()
            except Exception as ex:
                messagebox.showerror("Error", f"Drop failed: {ex}")

    def search(self):
        """Filter table by roll number."""
        roll = self.var_search.get().strip()
        if not roll:
            messagebox.showerror("Error", "Please enter a Roll No. to search.", parent=self.root)
            return
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM enrollment WHERE roll=?", (roll,))
            rows = cur.fetchall()
            con.close()
            self.table.delete(*self.table.get_children())
            if rows:
                for row in rows:
                    self.table.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "No enrollment record found.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Search failed: {ex}")

    def clear(self):
        """Reset all input fields and refresh the table."""
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("Select")
        self.var_enroll_date.set(str(date.today()))
        self.var_status.set("Active")
        self.var_search.set("")
        self._show_all()


if __name__ == "__main__":
    root = Tk()
    obj = EnrollmentClass(root)
    root.mainloop()
