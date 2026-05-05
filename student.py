from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

from create_db import create_db


class studentClass:
    def __init__(self, root):
        create_db()

        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x500+60+160")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

        title = Label(
            self.root,
            text="Manage Student Details",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white",
        )
        title.place(x=10, y=15, width=1180, height=35)

        # Column 1 labels
        Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=65)
        Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=105)
        Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=145)
        Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=185)
        Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=225)
        Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=265)

        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15), bg="lightyellow")
        self.txt_roll.place(x=150, y=65, width=200)

        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=105, width=200)
        Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=145, width=200)

        self.txt_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            values=("Select", "Male", "Female", "Other"),
            font=("goudy old style", 14),
            state="readonly",
            justify=CENTER,
        )
        self.txt_gender.place(x=150, y=185, width=200)
        self.txt_gender.current(0)

        Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=225, width=140)
        Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=300, y=225)
        Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15), bg="lightyellow").place(x=350, y=225, width=120)
        Label(self.root, text="Pin", font=("goudy old style", 15, "bold"), bg="white").place(x=480, y=225)
        Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15), bg="lightyellow").place(x=520, y=225, width=150)

        # Column 2 labels
        Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=65)
        Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=105)
        Label(self.root, text="Admission", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=145)
        Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=185)

        Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow").place(x=480, y=65, width=190)
        Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=480, y=105, width=190)
        Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15), bg="lightyellow").place(x=480, y=145, width=190)

        self.course_list = []
        self.fetch_course()

        self.txt_course = ttk.Combobox(
            self.root,
            textvariable=self.var_course,
            values=self.course_list,
            font=("goudy old style", 14),
            state="readonly",
            justify=CENTER,
        )
        self.txt_course.place(x=480, y=185, width=190)
        self.txt_course.set("Select")

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=265, width=520, height=95)

        Button(self.root, text="Save", command=self.add, font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=150, y=410, width=110, height=40)
        Button(self.root, text="Update", command=self.update, font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2").place(x=270, y=410, width=110, height=40)
        Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2").place(x=390, y=410, width=110, height=40)
        Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2").place(x=510, y=410, width=110, height=40)

        Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=710, y=65)
        Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15), bg="lightyellow").place(x=840, y=65, width=190)
        Button(self.root, text="Search", command=self.search, font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=1050, y=65, width=110, height=30)

        table_frame = Frame(self.root, bd=2, relief=RIDGE)
        table_frame.place(x=710, y=105, width=470, height=360)

        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)

        self.StudentTable = ttk.Treeview(
            table_frame,
            columns=("roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)

        headings = {
            "roll": "Roll No.",
            "name": "Name",
            "email": "Email",
            "gender": "Gender",
            "dob": "D.O.B",
            "contact": "Contact",
            "admission": "Admission",
            "course": "Course",
            "state": "State",
            "city": "City",
            "pin": "PIN",
            "address": "Address",
        }
        for col, text in headings.items():
            self.StudentTable.heading(col, text=text)
            self.StudentTable.column(col, width=110)

        self.StudentTable.column("email", width=180)
        self.StudentTable.column("address", width=220)
        self.StudentTable["show"] = "headings"
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def get_connection(self):
        return sqlite3.connect(database="rms.db")

    def fetch_course(self):
        self.course_list.clear()
        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM course ORDER BY name")
            rows = cur.fetchall()
            self.course_list.extend([row[0] for row in rows])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def add(self):
        if self.var_roll.get().strip() == "":
            messagebox.showerror("Error", "Roll Number is required", parent=self.root)
            return

        try:
            int(self.var_roll.get())
        except ValueError:
            messagebox.showerror("Error", "Roll Number must be numeric", parent=self.root)
            return

        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
            if cur.fetchone() is not None:
                messagebox.showerror("Error", "Roll Number already exists", parent=self.root)
                return

            cur.execute(
                """
                INSERT INTO student
                (roll, name, email, gender, dob, contact, admission, course, state, city, pin, address)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.txt_address.get("1.0", END).strip(),
                ),
            )
            con.commit()
            messagebox.showinfo("Success", "Student added successfully", parent=self.root)
            self.show()
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        self.fetch_course()
        if hasattr(self, "txt_course"):
            self.txt_course.config(values=self.course_list)

        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student ORDER BY roll DESC")
            rows = cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, event):
        selected = self.StudentTable.focus()
        content = self.StudentTable.item(selected)
        row = content.get("values")
        if not row:
            return

        self.txt_roll.config(state="readonly")
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[11])

    def update(self):
        if self.var_roll.get().strip() == "":
            messagebox.showerror("Error", "Select student from list first", parent=self.root)
            return

        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
            if cur.fetchone() is None:
                messagebox.showerror("Error", "Student not found", parent=self.root)
                return

            cur.execute(
                """
                UPDATE student
                SET name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=?
                WHERE roll=?
                """,
                (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.txt_address.get("1.0", END).strip(),
                    self.var_roll.get(),
                ),
            )
            con.commit()
            messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
            self.show()
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        if self.var_roll.get().strip() == "":
            messagebox.showerror("Error", "Select student from list first", parent=self.root)
            return

        confirm = messagebox.askyesno("Confirm", "Do you really want to delete this student?", parent=self.root)
        if not confirm:
            return

        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
            cur.execute("DELETE FROM result WHERE roll=?", (self.var_roll.get(),))
            con.commit()
            messagebox.showinfo("Deleted", "Student deleted successfully", parent=self.root)
            self.show()
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.var_search.set("")
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.show()

    def search(self):
        if self.var_search.get().strip() == "":
            self.show()
            return

        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE roll=?", (self.var_search.get(),))
            row = cur.fetchone()
            self.StudentTable.delete(*self.StudentTable.get_children())
            if row is not None:
                self.StudentTable.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
