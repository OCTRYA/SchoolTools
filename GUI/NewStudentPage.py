import os
import tkinter as tk
import xml.etree.cElementTree as ET
from tkinter import ttk, messagebox, filedialog
import sys
import zipfile
import os
import time
import shutil
from PIL import Image, ImageTk
from pip._internal.utils.unpacking import unzip_file


class NewStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        self.__controller = controller.controller
        tk.Frame.__init__(self, parent, width=1000, height=1000, padx=20, pady=20)

        # Create a button to select a file
        select_button = tk.Button(self, text="Open Zipbestand...", bg="#006082", fg="white", command=self.select_file)
        select_button.grid(row = 0, pady=20)
        # Run the Tkinter event loop

        # Open the image vesalius file
        image = Image.open(self.resource_path("Images/VesaliusLogo.png"))
        image = image.resize((80, 50))
        # Convert the Image object into a Tkinter-compatible object
        tk_image = ImageTk.PhotoImage(image)

        # Create a label widget to display the image
        labelVesalius = tk.Label(self, image=tk_image, bg="white")
        labelVesalius.place(x=0, y=50)
        labelVesalius.grid(row=5)

        # Open the image DOS file
        imageDos = Image.open(self.resource_path("Images/dos.png"))
        imageDos = imageDos.resize((80, 80))
        # Convert the Image object into a Tkinter-compatible object
        tk1_image = ImageTk.PhotoImage(imageDos)

        # Create a label widget to display the image
        labelDos = tk.Label(self, image=tk1_image, bg="white")
        labelDos.grid(row=10)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    def select_file(self):
        global file_path
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Selected file:", file_path)
            self.makeDirectoryFromZippedFile()
        else:
            print("No file selected.")

    def makeDirectoryFromZippedFile(self):
        # make directory name based on zipped file_path name
        global file_path
        extract_to = file_path[:-4]
        print("De bestanden worden gekopieerd naar " + extract_to + ".")
        print("...")
        time.sleep(0)
        # Make sure the extraction directory exists
        os.makedirs(extract_to, exist_ok=True)
        unzip_file(file_path, extract_to)
        self.copy_folders_to_higher_directory(extract_to + "/" + os.path.basename(os.path.normpath(extract_to)), extract_to)
        # Unzip the file
        shutil.rmtree(extract_to + "/" + os.path.basename(os.path.normpath(extract_to)))
    def copy_folders_to_higher_directory(self, src_dir, dest_dir):
        # Ensure the destination directory exists
        os.makedirs(dest_dir, exist_ok=True)
        print("bronmap:" + src_dir)
        print("doelmap:" + dest_dir)
        # Traverse the source directory
        print(os.walk(src_dir))
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                # Get the absolute path of the current file
                filePath = os.path.join(root, file)

                # Get the name of the parent folder
                parent_folder = os.path.basename(root)

                # Construct the destination file path with the parent folder name and unique identifier
                dest_file_path = os.path.join(dest_dir, f"{parent_folder}_{file}")

                # Copy the file to the destination directory
                shutil.copy2(filePath, dest_file_path)
    def makeDirectoryFromZippedFile(self):
        # make directory name based on zipped file_path name
        global file_path
        extract_to = file_path[:-4]
        print("De bestanden worden gekopieerd naar " + extract_to + ".")
        print("...")
        time.sleep(0)
        # Make sure the extraction directory exists
        os.makedirs(extract_to, exist_ok=True)
        unzip_file(file_path, extract_to)
        self.copy_folders_to_higher_directory(extract_to + "/" + os.path.basename(os.path.normpath(extract_to)), extract_to)
        # Unzip the file
        shutil.rmtree(extract_to + "/" + os.path.basename(os.path.normpath(extract_to)))


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



