import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from course import CourseClass


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.state("zoomed")
        self.root.config(bg="white")

        # ===== LOGO =====
        self.logo = Image.open("images/logo_p.jpg")
        self.logo = self.logo.resize((40, 40))
        self.logo = ImageTk.PhotoImage(self.logo)

        # ===== TITLE =====
        title = Label(
            self.root,
            text="   Student Result Management System",
            image=self.logo,
            compound=LEFT,
            font=("times new roman", 20, "bold"),
            bg="#033054",
            fg="white",
            anchor="center"
        )
        title.grid(row=0, column=0, columnspan=3, sticky="ew")

        # ===== MENU =====
        menu_frame = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 15),
            bg="white"
        )
        menu_frame.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        for i in range(6):
            menu_frame.columnconfigure(i, weight=1)

        Button(menu_frame, text="Course", bg="#0b5377", fg="white",command=self.add_course).grid(row=0, column=0, padx=5, pady=5, sticky="ew",ipady=10)
        Button(menu_frame, text="Student", bg="#0b5377", fg="white").grid(row=0, column=1, padx=5, pady=5, sticky="ew",ipady=10)
        Button(menu_frame, text="Result", bg="#0b5377", fg="white").grid(row=0, column=2, padx=5, pady=5, sticky="ew",ipady=10)
        Button(menu_frame, text="View Results", bg="#0b5377", fg="white").grid(row=0, column=3, padx=5, pady=5, sticky="ew",ipady=10)
        Button(menu_frame, text="Logout", bg="#0b5377", fg="white").grid(row=0, column=4, padx=5, pady=5, sticky="ew",ipady=10)
        Button(menu_frame, text="Exit", bg="#0b5377", fg="white", command=self.root.destroy)\
            .grid(row=0, column=5, padx=5, pady=5, sticky="ew",ipady=10)

        # ===== MAIN CONTENT =====
        main_frame = Frame(self.root, bg="white")
        main_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=10)

        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=3)

        # ===== LEFT PANEL (CLOCK) =====
        left_frame = Frame(main_frame, bg="#022c43", bd=2, relief=RIDGE)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        Label(left_frame, text="Analog Clock",
              font=("times new roman", 16, "bold"),
              bg="#022c43", fg="white").pack(pady=10)

        # (Clock can be added later)

        # ===== RIGHT PANEL =====
        right_frame = Frame(main_frame, bg="white")
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # IMAGE
        self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((600, 300))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        Label(right_frame, image=self.bg_img, bg="white").pack(pady=10)

        # ===== DASHBOARD BOXES =====
        box_frame = Frame(right_frame, bg="white")
        box_frame.pack(fill="x", pady=10)

        for i in range(3):
            box_frame.columnconfigure(i, weight=1)

        Label(box_frame, text="Total Students\n[0]",
              bg="#e43b06", fg="white",
              font=("goudy old style", 18), bd=5, relief=RIDGE)\
            .grid(row=0, column=0, padx=5, sticky="ew")

        Label(box_frame, text="Total Course\n[0]",
              bg="#0676ad", fg="white",
              font=("goudy old style", 18), bd=5, relief=RIDGE)\
            .grid(row=0, column=1, padx=5, sticky="ew")

        Label(box_frame, text="Total Results\n[0]",
              bg="#038074", fg="white",
              font=("goudy old style", 18), bd=5, relief=RIDGE)\
            .grid(row=0, column=2, padx=5, sticky="ew")

        # ===== FOOTER =====
        footer = Label(
            self.root,
            text="Student Result Management System",
            bg="#262626",
            fg="white"
        )
        footer.grid(row=3, column=0, columnspan=3, sticky="ew")
    

    def add_course(self):
     new_win = Toplevel(self.root)
     CourseClass(new_win)

# ===== RUN =====
if __name__ == "__main__":
    root = Tk()
    app = RMS(root)
    root.mainloop()