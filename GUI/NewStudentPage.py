import os
import tkinter as tk
import xml.etree.cElementTree as ET
from tkinter import ttk, messagebox


class NewStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        self.__controller = controller.controller
        tk.Frame.__init__(self, parent, width=1000, height=1000, padx=20, pady=20)

        self.label = ttk.Label(self, text="Add a new Student", font=self.__controller.getTitleFont())
        self.label.grid(row=0)

        self.first_name_label = ttk.Label(self, text="First name:")
        self.first_name_label.grid(row=1, column=0, sticky="w")
        self.first_name_entry = ttk.Entry(self)
        self.first_name_entry.grid(row=1, column=1)

        self.last_name_label = ttk.Label(self, text="Last name:")
        self.last_name_label.grid(row=2, column=0, sticky="w")
        self.last_name_entry = ttk.Entry(self)
        self.last_name_entry.grid(row=2, column=1)

        self.age_label = ttk.Label(self, text="Birthday:")
        self.age_label.grid(row=3, column=0, sticky="w")
        self.age_entry = ttk.Entry(self)
        self.age_entry.grid(row=3, column=1)

        self.email_label = ttk.Label(self, text="Email:")
        self.email_label.grid(row=4, column=0, sticky="w")
        self.email_entry = ttk.Entry(self)
        self.email_entry.grid(row=4, column=1)

        self.telephone_label = ttk.Label(self, text="Telephone:")
        self.telephone_label.grid(row=5, column=0, sticky="w")
        self.telephone_entry = ttk.Entry(self)
        self.telephone_entry.grid(row=5, column=1)

        self.streetname_label = ttk.Label(self, text="Street name:")
        self.streetname_label.grid(row=6, column=0, sticky="w")
        self.streetname_entry = ttk.Entry(self)
        self.streetname_entry.grid(row=6, column=1)

        self.housenumber_label = ttk.Label(self, text="housenumber:")
        self.housenumber_label.grid(row=7, column=0, sticky="w")
        self.housenumber_entry = ttk.Entry(self)
        self.housenumber_entry.grid(row=7, column=1)

        self.zipcode_label = ttk.Label(self, text="zipcode:")
        self.zipcode_label.grid(row=8, column=0, sticky="w")
        self.zipcode_entry = ttk.Entry(self)
        self.zipcode_entry.grid(row=8, column=1)

        self.city_label = ttk.Label(self, text="city:")
        self.city_label.grid(row=9, column=0, sticky="w")
        self.city_entry = ttk.Entry(self)
        self.city_entry.grid(row=9, column=1)

        self.submit_button = ttk.Button(self, text="Make new Student", command=lambda: self.submit_form())
        self.submit_button.grid(row=10, column=1,columnspan=2)

    def submit_form(self):

        self.createStudentFile(os.path.join(self.__controller.get_root(),"students"))

    def empty_form(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.housenumber_entry.delete(0, tk.END)
        self.streetname_entry.delete(0, tk.END)
        self.zipcode_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.telephone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    #create student file
    def createStudentFile(self, students_root_location):
        #checks is students folder exists
        if os.path.exists(students_root_location):
            #checks if student file exists and makes the file if not
            print("the folder exists")
            student_name_path = self.last_name_entry.get() + self.first_name_entry.get()
            student_path = os.path.join(students_root_location, student_name_path)
            if os.path.isfile(student_path):
                print("file exists")
                messagebox.showinfo("Message", "Student " + self.first_name_entry.get() + " " + self.last_name_entry.get() + " already exists")
            else:
                root = ET.Element("students")
                student = ET.SubElement(root, "student")
                ET.SubElement(student, "firstname").text = self.first_name_entry.get()
                ET.SubElement(student, "lastname").text = self.last_name_entry.get()
                ET.SubElement(student, "birthday").text = self.age_entry.get()
                ET.SubElement(student, "email").text = self.email_entry.get()
                ET.SubElement(student, "streetname").text = self.streetname_entry.get()
                ET.SubElement(student, "housenumber").text = self.housenumber_entry.get()
                ET.SubElement(student, "zipcode").text = self.zipcode_entry.get()
                ET.SubElement(student, "city").text = self.city_entry.get()
                ET.SubElement(student, "telephone").text = self.telephone_entry.get()

                tree = ET.ElementTree(root)
                tree.write(os.path.join(students_root_location, student_path))
                messagebox.showinfo("Message", "Student " + self.first_name_entry.get() + " " + self.last_name_entry.get() + " Successfully created")
                self.empty_form()



