from tkinter import *
from tkinter import messagebox, filedialog
import sqlite3


class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1160x500+80+160")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_search = StringVar()
        self.var_id = ""

        title = Label(
            self.root,
            text="View Student Results",
            font=("goudy old style", 20, "bold"),
            bg="orange",
            fg="#262626",
        )
        title.place(x=10, y=15, width=1140, height=50)

        Label(
            self.root,
            text="Search By Roll No.",
            font=("goudy old style", 20, "bold"),
            bg="white",
        ).place(x=260, y=100)

        Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 20),
            bg="lightyellow",
        ).place(x=520, y=100, width=150)

        Button(
            self.root,
            text="Search",
            font=("goudy old style", 18, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.search,
        ).place(x=690, y=100, width=110, height=36)

        Button(
            self.root,
            text="Clear",
            font=("goudy old style", 18, "bold"),
            bg="gray",
            fg="white",
            cursor="hand2",
            command=self.clear,
        ).place(x=815, y=100, width=110, height=36)

        Label(
            self.root,
            text="Roll No.",
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        ).place(x=150, y=230, width=150, height=50)

        Label(
            self.root,
            text="Name",
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        ).place(x=300, y=230, width=150, height=50)

        Label(
            self.root,
            text="Course",
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        ).place(x=450, y=230, width=150, height=50)

        Label(
            self.root,
            text="Marks Obtained",
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        ).place(x=600, y=230, width=150, height=50)

        Label(
            self.root,
            text="Total Marks",
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        ).place(x=750, y=230, width=150, height=50)

        Label(
            self.root,
            text="Percentage",
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        ).place(x=900, y=230, width=150, height=50)

        self.roll = Label(
            self.root,
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.roll.place(x=150, y=280, width=150, height=50)

        self.name = Label(
            self.root,
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.name.place(x=300, y=280, width=150, height=50)

        self.course = Label(
            self.root,
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.course.place(x=450, y=280, width=150, height=50)

        self.marks_ob = Label(
            self.root,
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.marks_ob.place(x=600, y=280, width=150, height=50)

        self.full_marks = Label(
            self.root,
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.full_marks.place(x=750, y=280, width=150, height=50)

        self.per = Label(
            self.root,
            font=("goudy old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.per.place(x=900, y=280, width=150, height=50)

        Button(
            self.root,
            text="Delete",
            font=("goudy old style", 18, "bold"),
            bg="red",
            fg="white",
            cursor="hand2",
            command=self.delete,
        ).place(x=420, y=370, width=150, height=40)

        Button(
            self.root,
            text="Export Text",
            font=("goudy old style", 18, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.export_text,
        ).place(x=590, y=370, width=170, height=40)

    def search(self):
        if self.var_search.get().strip() == "":
            messagebox.showerror(
                "Error",
                "Roll Number is required",
                parent=self.root,
            )
            return

        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            cur.execute(
                "SELECT * FROM result WHERE roll=?",
                (self.var_search.get(),),
            )
            row = cur.fetchone()

            if row is not None:
                self.var_id = row[0]
                self.roll.config(text=row[1])
                self.name.config(text=row[2])
                self.course.config(text=row[3])
                self.marks_ob.config(text=row[4])
                self.full_marks.config(text=row[5])
                self.per.config(text=f"{row[6]}%")
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

    def clear(self):
        self.var_id = ""
        self.var_search.set("")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_ob.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")

    def delete(self):
        if self.var_id == "":
            messagebox.showerror(
                "Error",
                "Search student result first",
                parent=self.root,
            )
            return

        confirm = messagebox.askyesno(
            "Confirm",
            "Do you really want to delete this result?",
            parent=self.root,
        )

        if confirm:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()

            try:
                cur.execute(
                    "DELETE FROM result WHERE rid=?",
                    (self.var_id,),
                )
                con.commit()

                messagebox.showinfo(
                    "Deleted",
                    "Result deleted successfully",
                    parent=self.root,
                )

                self.clear()

            except Exception as ex:
                messagebox.showerror(
                    "Error",
                    f"Error due to {str(ex)}",
                    parent=self.root,
                )

            finally:
                con.close()

    def export_text(self):
        if self.var_id == "":
            messagebox.showerror(
                "Error",
                "Search a student result first",
                parent=self.root,
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text file", "*.txt")],
            title="Save Result",
        )

        if file_path == "":
            return

        content = (
            "Student Result\n"
            "==============\n"
            f"Roll No.: {self.roll.cget('text')}\n"
            f"Name: {self.name.cget('text')}\n"
            f"Course: {self.course.cget('text')}\n"
            f"Marks Obtained: {self.marks_ob.cget('text')}\n"
            f"Total Marks: {self.full_marks.cget('text')}\n"
            f"Percentage: {self.per.cget('text')}\n"
        )

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        messagebox.showinfo(
            "Success",
            "Result exported successfully",
            parent=self.root,
        )


if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
