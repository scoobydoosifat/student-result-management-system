import tkinter as tk

# Import all modules (integration responsibility)
from login import LoginSystem
from create_db import create_db

# Optional: preload modules to show full integration
from dashboard import RMS
from course import CourseClass
from student import studentClass
from enrollment import EnrollmentClass
from result import resultClass
from report import reportClass


class AppController:
    """
    This class is responsible for initializing
    and controlling the full application flow.
    """

    def __init__(self):
        # Step 1: Initialize database
        create_db()

        # Step 2: Start login system
        self.root = tk.Tk()
        self.app = LoginSystem(self.root)

    def run(self):
        # Step 3: Run the application
        self.root.mainloop()


# Entry point of the system
if __name__ == "__main__":
    controller = AppController()
    controller.run()