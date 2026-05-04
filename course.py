from tkinter import *
from tkinter import ttk


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Course Details")
        self.root.geometry("1100x600+200+100")
        self.root.config(bg="white")

        # ===== TITLE =====
        title = Label(self.root, text="Manage Course Details",
                      font=("times new roman", 20, "bold"),
                      bg="#033054", fg="white")
        title.pack(fill=X)

        # ===== MAIN FRAME =====
        main_frame = Frame(self.root, bg="white")
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # ===== LEFT FRAME =====
        left_frame = Frame(main_frame, bg="white")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10)

        # Labels + Entry
        Label(left_frame, text="Course Name", font=("Arial", 12), bg="white").grid(row=0, column=0, sticky="w", pady=5)
        Entry(left_frame, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)

        Label(left_frame, text="Duration", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="w", pady=5)
        Entry(left_frame, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=5)

        Label(left_frame, text="Charges", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="w", pady=5)
        Entry(left_frame, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=5)

        Label(left_frame, text="Description", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="nw", pady=5)
        Text(left_frame, width=30, height=8).grid(row=3, column=1, padx=10, pady=5)

        # ===== BUTTONS =====
        btn_frame = Frame(left_frame, bg="white")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

        Button(btn_frame, text="Save", width=10, bg="#2196f3", fg="white").grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Update", width=10, bg="#4caf50", fg="white").grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Delete", width=10, bg="#f44336", fg="white").grid(row=0, column=2, padx=5)
        Button(btn_frame, text="Clear", width=10, bg="#607d8b", fg="white").grid(row=0, column=3, padx=5)

        # ===== RIGHT FRAME =====
        right_frame = Frame(main_frame, bg="white", bd=2, relief=RIDGE)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10)

        # Search bar
        Label(right_frame, text="Course Name", bg="white", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
        Entry(right_frame, font=("Arial", 12)).grid(row=0, column=1, padx=5)
        Button(right_frame, text="Search", bg="#2196f3", fg="white").grid(row=0, column=2, padx=5)

        # ===== TABLE =====
        self.course_table = ttk.Treeview(
            right_frame,
            columns=("name", "duration", "charges", "desc"),
            show="headings"
        )

        self.course_table.heading("name", text="Name")
        self.course_table.heading("duration", text="Duration")
        self.course_table.heading("charges", text="Charges")
        self.course_table.heading("desc", text="Description")

        self.course_table.grid(row=1, column=0, columnspan=3, sticky="nsew")

        # Scrollbar
        scroll_y = Scrollbar(right_frame, orient=VERTICAL, command=self.course_table.yview)
        scroll_y.grid(row=1, column=3, sticky="ns")

        self.course_table.config(yscrollcommand=scroll_y.set)

        right_frame.rowconfigure(1, weight=1)
        right_frame.columnconfigure(1, weight=1)