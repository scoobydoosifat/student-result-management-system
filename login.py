import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from dashboard import RMS 


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("500x400+400+200")
        self.root.config(bg="white")

        # ===== DB =====
        self.create_db()

        # ===== TITLE =====
        tk.Label(self.root, text="Teacher Login",
                 font=("times new roman", 20, "bold"),
                 bg="#033054", fg="white").pack(fill="x")

        # ===== LOGIN FRAME =====
        frame = tk.Frame(self.root, bg="white")
        frame.pack(pady=40)

        tk.Label(frame, text="Username", font=("Arial", 14), bg="white").grid(row=0, column=0, pady=10)
        self.txt_user = tk.Entry(frame, font=("Arial", 14))
        self.txt_user.grid(row=0, column=1, padx=10)

        tk.Label(frame, text="Password", font=("Arial", 14), bg="white").grid(row=1, column=0, pady=10)
        self.txt_pass = tk.Entry(frame, font=("Arial", 14), show="*")
        self.txt_pass.grid(row=1, column=1, padx=10)

        tk.Button(self.root, text="Login",
                  font=("Arial", 14),
                  bg="#2196f3", fg="white",
                  command=self.login).pack(pady=20)

    # ===== CREATE TABLE =====
    def create_db(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
        """)

        # default teacher account
        cur.execute("SELECT * FROM users WHERE username=?", ("teacher",))
        if not cur.fetchone():
            cur.execute("INSERT INTO users (username, password, role) VALUES (?,?,?)",
                        ("teacher", "1234", "teacher"))

        con.commit()
        con.close()

    # ===== LOGIN FUNCTION =====
    def login(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        cur.execute("""
        SELECT * FROM users
        WHERE username=? AND password=? AND role=?
        """, (username, password, "teacher"))

        row = cur.fetchone()
        con.close()

        if row:
            messagebox.showinfo("Success", "Login Successful")

            # close login window
            self.root.destroy()

            # open dashboard
            new_root = tk.Tk()
            app = RMS(new_root)
            new_root.mainloop()

        else:
            messagebox.showerror("Error", "Invalid Username or Password")


# ===== RUN =====
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()