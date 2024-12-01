import tkinter as tk
class StudentOverviewPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student Page")
        label.pack(padx=10, pady=10)
