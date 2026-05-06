from tkinter import *
from tkinter import ttk
import sqlite3


class AnalyticsClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Analytics Dashboard")
        self.root.geometry("900x500+200+120")
        self.root.config(bg="white")

        # ===== TITLE =====
        Label(self.root, text="System Analytics",
              font=("times new roman", 20, "bold"),
              bg="#033054", fg="white").pack(fill=X)

        # ===== STATS FRAME =====
        stats_frame = Frame(self.root, bg="white")
        stats_frame.pack(fill=X, pady=20)

        self.lbl_students = Label(stats_frame, text="Total Students\n0",
                                  bg="#e43b06", fg="white",
                                  font=("goudy old style", 15), width=20)
        self.lbl_students.grid(row=0, column=0, padx=10)

        self.lbl_courses = Label(stats_frame, text="Total Courses\n0",
                                 bg="#0676ad", fg="white",
                                 font=("goudy old style", 15), width=20)
        self.lbl_courses.grid(row=0, column=1, padx=10)

        self.lbl_results = Label(stats_frame, text="Total Results\n0",
                                 bg="#038074", fg="white",
                                 font=("goudy old style", 15), width=20)
        self.lbl_results.grid(row=0, column=2, padx=10)

        # ===== TABLE =====
        table_frame = Frame(self.root, bg="white")
        table_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(table_frame, columns=("course", "students", "avg_marks"), show="headings")

        self.tree.heading("course", text="Course")
        self.tree.heading("students", text="Total Students")
        self.tree.heading("avg_marks", text="Average Marks (%)")

        self.tree.pack(fill=BOTH, expand=True)

        self.load_data()

    def load_data(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        # ===== BASIC COUNTS =====
        cur.execute("SELECT COUNT(*) FROM student")
        self.lbl_students.config(text=f"Total Students\n{cur.fetchone()[0]}")

        cur.execute("SELECT COUNT(*) FROM course")
        self.lbl_courses.config(text=f"Total Courses\n{cur.fetchone()[0]}")

        cur.execute("SELECT COUNT(*) FROM result")
        self.lbl_results.config(text=f"Total Results\n{cur.fetchone()[0]}")

        # ===== ANALYTICS QUERY =====
        query = """
        SELECT course, COUNT(roll), AVG(per)
        FROM result
        GROUP BY course
        """
        cur.execute(query)

        rows = cur.fetchall()

        self.tree.delete(*self.tree.get_children())

        for row in rows:
            self.tree.insert("", END, values=row)

        con.close()