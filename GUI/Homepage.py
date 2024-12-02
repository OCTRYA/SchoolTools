import os
import sys
import tkinter as tk

from PIL import Image, ImageTk


class Homepage(tk.Frame):
    def __init__(self,parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home page")
        label.pack(padx=10, pady=10)


        # Open the image vesalius file
        self.image = Image.open(self.resource_path("Images/VesaliusLogo.png"))
        self.image = self.image.resize((160, 100))
        # Convert the Image object into a Tkinter-compatible object
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create a label widget to display the image
        self.labelVesalius = tk.Label(self, image=self.tk_image, bg="white")
        self.labelVesalius.place(x=0, y=50)
        self.labelVesalius.pack()

        # Open the image DOS file
        self.imageDos = Image.open(self.resource_path("Images/dos.png"))
        self.imageDos = self.imageDos.resize((160, 160))
        # Convert the Image object into a Tkinter-compatible object
        self.tk1_image = ImageTk.PhotoImage(self.imageDos)

        # Create a label widget to display the image
        self.labelDos = tk.Label(self, image=self.tk1_image, bg="white")
        self.labelDos.place(x=200, y=200)
        self.labelDos.pack()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)