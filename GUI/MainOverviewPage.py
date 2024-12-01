import os
import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import *


class MainOverviewPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller.controller
        self.toegevoegdeLeerkachten = []
        self.label = tk.Label(self,text="RoosterMatch", font=self.controller.getTitleFont())
        self.label.grid(row=0, padx=10,pady=10)
        self.labelLeerkrachtZoekvenster = tk.Label(self, text="Zoek een of meerdere collega's via hun naam", font=self.controller.getCustomFont())
        self.labelLeerkrachtZoekvenster.grid(row=1, column=0)
        self.tekstveldLeerkrachtZoekvenster = tk.Entry(self, font=self.controller.getTitleFont())
        self.tekstveldLeerkrachtZoekvenster.grid(row=1, column=1)
        self.voegLeerkrachtToeKnop = tk.Button(self, text="Voeg leekracht toe", command = self.voegLeerkrachtToeAanZoeklijst)
        self.voegLeerkrachtToeKnop.grid(row=1, column=4)
        self.lijst_van_leerkrachten = tk.Listbox(self, width=50)
        self.lijst_van_leerkrachten.grid(row=3, column=0, rowspan=4, columnspan=1)
        self.updateList(self.controller.planner.leerkrachten)
        # toon de selectie in de lijstbox bij onclick
        self.lijst_van_leerkrachten.bind("<<ListboxSelect>>", self.vulTekstveldLeerkrachtZoekventser)
        self.tekstveldLeerkrachtZoekvenster.bind("<KeyRelease>",self.checkInLijst_van_Leerkrachten)
        self.lijst_van_toegevoegde_leerkrachten = tk.Listbox(self, width=50)
        self.lijst_van_toegevoegde_leerkrachten.grid(row=3, column=1, rowspan=8, columnspan=1)
        self.genereerRoosterKnop = tk.Button(self, text="Genereer rooster", command = self.toonRooster)
        self.genereerRoosterKnop.grid(row=12, column=0)
        self.verwijderLeerkrachtKnop = tk.Button(self, text="Verwijder leekracht", command = self.verwijderLeerkrachtUitZoeklijst)
        self.verwijderLeerkrachtKnop.grid(row=3, column=4)

    def updateList(self, data):
        #Clear the listbox
        self.lijst_van_leerkrachten.delete(0, END)

        #Voeg de leerkrachten toe aan de lijst
        for leerkracht in data:
            self.lijst_van_leerkrachten.insert(END,leerkracht.naam)

    def updateListToegevoegdeLeerkrachten(self):
        #Clear the listbox
        self.lijst_van_toegevoegde_leerkrachten.delete(0, END)

        #Voeg de leerkrachten toe aan de lijst
        for leerkracht in self.toegevoegdeLeerkachten:
            self.lijst_van_toegevoegde_leerkrachten.insert(END,leerkracht.naam)

    #update zoekLeerkrachtZoekvenster met leerkrachtlijstklik
    def vulTekstveldLeerkrachtZoekventser(self, event):
        #verwijdert inhoud van zoekvenster
        self.tekstveldLeerkrachtZoekvenster.delete(0,END)
        #Voeg de geklikt item aan zoekvenster
        self.tekstveldLeerkrachtZoekvenster.insert(0, self.lijst_van_leerkrachten.get(ACTIVE))

    def checkInLijst_van_Leerkrachten(self, event):
        #neem wat er getypt wordt
        typt = self.tekstveldLeerkrachtZoekvenster.get()

        if typt == "":
            data = self.controller.planner.leerkrachten
        else:
            data = []
            for item in self.controller.planner.leerkrachten:
                if typt.lower() in item.naam.lower():
                    data.append(item)

        self.updateList(data)

    def voegLeerkrachtToeAanZoeklijst(self):
        for leerkracht in self.controller.planner.leerkrachten:
            if leerkracht.naam == self.lijst_van_leerkrachten.get(ACTIVE):
                check = False
                for leerkrachtInToegevoegdeLijst in self.toegevoegdeLeerkachten:
                    if leerkrachtInToegevoegdeLijst.naam == self.lijst_van_leerkrachten.get(ACTIVE):
                        check = True
                if check == False:
                    self.toegevoegdeLeerkachten.append(leerkracht)
        self.updateListToegevoegdeLeerkrachten()

    def verwijderLeerkrachtUitZoeklijst(self):
        for leerkrachtInToegevoegdeLijst in self.toegevoegdeLeerkachten:
            if leerkrachtInToegevoegdeLijst.naam == self.lijst_van_toegevoegde_leerkrachten.get(ACTIVE) and self.lijst_van_toegevoegde_leerkrachten.curselection():
                self.toegevoegdeLeerkachten.remove(leerkrachtInToegevoegdeLijst)
        self.updateListToegevoegdeLeerkrachten()

    def toonRooster(self):
        self.controller.planner.genereerRooster(self.toegevoegdeLeerkachten)
        rooster = self.controller.planner.rooster
        for i in range(10):
            for j in range(6):
                self.label = tk.Label(self, text=rooster[i][j], font=self.controller.getCustomFont())
                self.label.grid(row=12+i, column=j, padx=10, pady=10)
