#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'czarek'

from tkinter import *


# from tkinter.ttk import *

class Dyscyplina(Button):
    """Pojedyncza kratka z liczbą"""
    aktywny = 0
    ilosc = 0
    kolor_aktywny = "red"
    kolor_nieaktywny = "gray85"

    def zmien_aktywnosc(self, zezwolenie):
        if (self.aktywny == 0 and zezwolenie):
            self.aktywny = 1
            self.configure(bg=self.kolor_aktywny, activebackground=self.kolor_aktywny)
        else:
            self.aktywny = 0
            self.configure(bg=self.kolor_nieaktywny, activebackground=self.kolor_nieaktywny)


class Zaklad(Frame):
    """Pojedynczy zakład (kratka 7x7"""

    def __init__(self, master, ile=6, do=49):
        super().__init__(master, bd=4, bg='red')
        self.z = []
        self.do = do
        self.ile = ile
        for liczba in range(0, do):
            c = liczba // 7
            r = liczba % 7
            self.z.append(Dyscyplina(self, text=str(liczba + 1), borderwidth=1, padx=5, pady=2, height=1, width=1))
            self.z[liczba].grid(row=r, column=c)
            self.z[liczba]["command"] = lambda x=liczba: self.dupka(x)

    def dupka(self, k):
        i = self.ile_obstawionych()
        self.z[k].zmien_aktywnosc(i < self.ile)

    def ile_obstawionych(self):
        ile = 0
        for liczba in range(0, self.do):
            ile = ile + self.z[liczba].aktywny
        return (ile)

    def get_obstawione(self):
        obstawione = []
        for i in range(0, self.do):
            if self.z[i].aktywny == 1:
                obstawione.append(i + 1)
        return obstawione


class Kupon(Frame):
    """kupon zawiera 5 zakładów"""

    def __init__(self, master):
        super().__init__(master)
        self.ilosc_zakladow = 5
        self.k = []
        self.ramka_gora = Frame(self)
        self.ramka_gora.grid(row=0, column=0)
        self.ramka_dol = Frame(self)
        self.ramka_dol.grid(row=1, column=0, pady=50)
        self.etykieta1 = Label(self.ramka_dol, text="Na ile losowań?").grid(row=0, column=0)
        self.ilosc_los = Entry(self.ramka_dol).grid(row=0, column=1, sticky=S, pady=10)
        self.etykieta2 = Label(self.ramka_dol, text="Szóstek:").grid(row=1, column=1, sticky=E, pady=5)
        self.etykieta3 = Label(self.ramka_dol, text="Piątek:").grid(row=2, column=1, sticky=E, pady=5)
        self.etykieta4 = Label(self.ramka_dol, text="Czwórek:").grid(row=3, column=1, sticky=E, pady=5)
        self.etykieta5 = Label(self.ramka_dol, text="Trójek:").grid(row=4, column=1, sticky=E, pady=5)
        self.wynik6 = Label(self.ramka_dol, text="0").grid(row=1, column=2)
        self.wynik5 = Label(self.ramka_dol, text="0").grid(row=2, column=2)
        self.wynik4 = Label(self.ramka_dol, text="0").grid(row=3, column=2)
        self.wynik3 = Label(self.ramka_dol, text="0").grid(row=4, column=2)
        self.pack()

        for liczba in range(self.ilosc_zakladow):
            self.k.append(Zaklad(self.ramka_gora))
            self.k[liczba].grid(row=0, column=liczba)

        self.p = Button(self.ramka_dol, text="Start", command=self.przycisk).grid(row=6, column=0)

    def get_obstawione(self):
        obstawione = []
        for self.zaklad in self.k:
            obstawione.append(self.zaklad.get_obstawione())
        return (obstawione)

    def przycisk(self):  # tu będzie start obliczeń
        print(self.get_obstawione())


okno = Tk()
okno.title("Kupon totolotka")
x = Kupon(okno)
okno.mainloop()
