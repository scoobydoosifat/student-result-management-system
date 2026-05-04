from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3


class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1160x500+80+160")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()

        title = Label(
            self.root,
            text="Add Student Results",
            font=("goudy old style", 20, "bold"),
            bg="orange",
            fg="#262626",
        )
        title.place(x=10, y=15, width=1140, height=50)

        self.roll_list = []
        self.fetch_roll()

        Label(
            self.root,
            text="Select Student",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(x=50, y=100)

        Label(
            self.root,
            text="Name",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(x=50, y=160)

        Label(
            self.root,
            text="Course",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(x=50, y=220)

        Label(
            self.root,
            text="Marks Obtained",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(x=50, y=280)

        Label(
            self.root,
            text="Full Marks",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(x=50, y=340)

        self.txt_student = ttk.Combobox(
            self.root,
            textvariable=self.var_roll,
            values=self.roll_list,
            font=("goudy old style", 20, "bold"),
            state="readonly",
            justify=CENTER,
        )
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        Button(
            self.root,
            text="Search",
            font=("goudy old style", 16, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.search,
        ).place(x=500, y=100, width=100, height=35)

        Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
            state="readonly",
        ).place(x=280, y=160, width=320)

        Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
            state="readonly",
        ).place(x=280, y=220, width=320)

        Entry(
            self.root,
            textvariable=self.var_marks,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
        ).place(x=280, y=280, width=320)

        Entry(
            self.root,
            textvariable=self.var_full_marks,
            font=("goudy old style", 20, "bold"),
            bg="lightyellow",
        ).place(x=280, y=340, width=320)

        Button(
            self.root,
            text="Submit",
            font=("times new roman", 15),
            bg="lightgreen",
            cursor="hand2",
            command=self.add,
        ).place(x=300, y=420, width=120, height=35)

        Button(
            self.root,
            text="Clear",
            font=("times new roman", 15),
            bg="lightgray",
            cursor="hand2",
            command=self.clear,
        ).place(x=430, y=420, width=120, height=35)

    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root,
            )

        finally:
            con.close()

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_roll.get() == "Select" or self.var_roll.get() == "":
                messagebox.showerror(
                    "Error",
                    "Please select a student roll number",
                    parent=self.root,
                )
            else:
                cur.execute(
                    "SELECT name, course FROM student WHERE roll=?",
                    (self.var_roll.get(),),
                )
                row = cur.fetchone()

                if row is not None:
                    self.var_name.set(row[0])
                    self.var_course.set(row[1])
                else:
                    messagebox.showerror(
                        "Error",
                        "No record found",
                        parent=self.root,
                    )

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root,
            )

        finally:
            con.close()

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_name.get() == "":
                messagebox.showerror(
                    "Error",
                    "Please search student record first",
                    parent=self.root,
                )
                return

            if self.var_marks.get() == "" or self.var_full_marks.get() == "":
                messagebox.showerror(
                    "Error",
                    "Marks and full marks are required",
                    parent=self.root,
                )
                return

            marks = float(self.var_marks.get())
            full_marks = float(self.var_full_marks.get())

            if full_marks <= 0:
                messagebox.showerror(
                    "Error",
                    "Full marks must be greater than 0",
                    parent=self.root,
                )
                return

            percentage = round((marks * 100) / full_marks, 2)

            cur.execute(
                "SELECT * FROM result WHERE roll=? AND course=?",
                (self.var_roll.get(), self.var_course.get()),
            )
            row = cur.fetchone()

            if row is not None:
                messagebox.showerror(
                    "Error",
                    "Result already exists for this student",
                    parent=self.root,
                )
            else:
                cur.execute(
                    """
                    INSERT INTO result
                    (roll, name, course, marks_ob, full_marks, per)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(percentage),
                    ),
                )

                con.commit()

                messagebox.showinfo(
                    "Success",
                    "Result added successfully",
                    parent=self.root,
                )

                self.clear()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Marks must be numbers only",
                parent=self.root,
            )

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root,
            )

        finally:
            con.close()

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")


if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
