import tkinter as tk
class StudentCourseOverviewPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login")
        label.pack(padx=10, pady=10)