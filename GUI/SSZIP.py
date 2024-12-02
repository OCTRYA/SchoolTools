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


class SSZIP(tk.Frame):
    def __init__(self, parent, controller):
        self.__controller = controller.controller
        tk.Frame.__init__(self, parent, width=1000, height=1000, padx=20, pady=20)

        # Create a button to select a file
        select_button = tk.Button(self, text="Open Zipbestand...", bg="#006082", fg="white", command=self.select_file)
        select_button.grid(row = 0, pady=20)
        # Run the Tkinter event loop

        # Open the image vesalius file
        self.image = Image.open(self.resource_path("Images/VesaliusLogo.png"))
        self.image = self.image.resize((80, 50))
        # Convert the Image object into a Tkinter-compatible object
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create a label widget to display the image
        self.labelVesalius = tk.Label(self, image=self.tk_image, bg="white")
        self.labelVesalius.grid(row=5)

        # Open the image DOS file
        self.imageDos = Image.open(self.resource_path("Images/dos.png"))
        self.imageDos = self.imageDos.resize((80, 80))
        # Convert the Image object into a Tkinter-compatible object
        self.tk1_image = ImageTk.PhotoImage(self.imageDos)

        # Create a label widget to display the image
        self.labelDos = tk.Label(self, image=self.tk1_image, bg="white")
        self.labelDos.grid(row=10)

        self.file_path =""

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            print("Selected file:", self.file_path)
            self.makeDirectoryFromZippedFile()
        else:
            print("No file selected.")

    def unzip_file(self, zip_file, extract_to):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("Bestanden succesvol gekopieerd naar:", extract_to)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


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
        extract_to = self.file_path[:-4]
        print("De bestanden worden gekopieerd naar " + extract_to + ".")
        print("...")
        time.sleep(0)
        # Make sure the extraction directory exists
        os.makedirs(extract_to, exist_ok=True)
        self.unzip_file(self.file_path, extract_to)
        print("traaalalal " + os.path.basename(os.path.normpath(extract_to)))
        self.copy_folders_to_higher_directory(extract_to + "/" + os.path.basename(os.path.normpath(extract_to)), extract_to)
        # Unzip the file
        shutil.rmtree(extract_to + "/" + os.path.basename(os.path.normpath(extract_to)))









