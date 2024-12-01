import tkinter as tk
import xml.etree.cElementTree as ET

class ManageCoursesPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Manage Course")
        self.controller = controller.controller










        createCourse_button = tk.Button(self, text="Create course")
        createCourse_button.grid(row=0, columnspan=2)

        removeCourse_button = tk.Button(self, text="Remove course")
        removeCourse_button.grid(row=0, column=3, columnspan=2, padx=5)

        name_label = tk.Label(self, text="Name course:")
        name_label.grid(row=1, column=0, sticky="w")
        name_entry = tk.Entry(self)
        name_entry.grid(row=1, column=1)

        list_of_courses = tk.Listbox(self)
        list_of_courses.insert(1,"Wiskunde")
        list_of_courses.grid(row=0, column=150,rowspan=10)

