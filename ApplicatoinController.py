import os
import sys
from tkinter import font

from bs4 import BeautifulSoup

from GUI.LC_window import LC_window
import xml.etree.cElementTree as ET

from GUI.Moment import Moment
from Leerkracht import Leerkracht
from Les import Les
from Planner import Planner


class ApplicationController:

    def __init__(self):
        self.__root = os.path.join(os.path.abspath(os.sep), "Vergadering")
        self.planner = Planner()
        self.read_xml_file()
        self.window = LC_window(self)

        self.window.mainloop()



    def getCustomFont(self):
        return font.Font(family="Helvetica", size=12)

    def getTitleFont(self):
        return font.Font(family="Helvetica", size=20, weight="bold", slant="italic")

    def read_xml_file(self):
    # Create a folder in the script directory
    # Get the folder selected by the user
    # folder_selected = filedialog.askdirectory()

        # Reading the data inside the xml
        # file to a variable under the name
        # data    def read_xml_file(self, file):
        with open(self.resource_path(os.path.join("Data","untis.xml")), 'r') as f:
            data = f.read()

        # Passing the stored data inside
        # the beautifulsoup parser, storing
        # the returned object
        bs_data = BeautifulSoup(data, "xml")

        # Finding all instances of tag
        # `unique`
        b_teachers = bs_data.find_all('teacher')

        self.planner.leerkrachten = []
        for t in b_teachers:
            teacher = Leerkracht(t["id"], t.find("surname").text)
            self.planner.leerkrachten.append(teacher)

        b_lessons = bs_data.find_all('lesson')
        for l in b_lessons:
            if l.find("lesson_teacher") is not(None):
                if(l.find("periods") is not(None)):
                    per = l.find("periods").text
                else:
                    per = "0"
                les = Les(l.find("lesson_teacher")["id"], per, l.find("effectivebegindate").text,l.find("effectiveenddate").text)
                b_moments = l.find_all("time")
                for moment in b_moments:
                    les.momenten.append(Moment(int(moment.find("assigned_day").text),int(moment.find("assigned_period").text)))
                self.planner.lessen.append(les)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)